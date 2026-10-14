#!/usr/bin/env python3
"""Static archive checks. No browser, business system, or network access."""
import base64
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import struct
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit

ARCHIVE = Path(__file__).resolve().parents[2]
OUT = ARCHIVE / 'report'
RECEIPT = OUT / 'qa/archive_checks.json'
sha = lambda data: hashlib.sha256(data).hexdigest()
load = lambda p: json.loads(p.read_text(encoding='utf-8'))
manifest = load(ARCHIVE / 'publication_files.json')
files = manifest['files']
assert len(files) == len(set(files))
for name in files:
    path = ARCHIVE / name
    assert not Path(name).is_absolute() and '..' not in Path(name).parts, name
    assert path.is_file() or path == RECEIPT, name
    assert not any(part in {'.local-only', 'evidence_supplement', 'fonts', 'fontcache', 'operations'} for part in path.parts), name
    assert path.suffix.lower() not in {'.jsonl', '.skill', '.zip', '.ttc', '.ttf', '.pdf', '.docx', '.jpg'}, name

page = (OUT / '04_final_report.html').read_text(encoding='utf-8')
model = json.loads(re.search(r'<script[^>]*id="deck-data"[^>]*>(.*?)</script>', page, re.S).group(1))
config = json.loads(re.search(r'<script[^>]*id="corporate-config"[^>]*>(.*?)</script>', page, re.S).group(1))
content = load(OUT / 'html_src/content_map.json')
assert content['html_sha256'] == sha(page.encode())
assert content['report_sha256'] == sha((OUT/'04_final_report.md').read_bytes())
assert content['matrix_sha256'] == sha((OUT/'02_evidence_matrix.md').read_bytes())
assert model['theme']['id'] == 'hk-technology' and content['default_view'] == 'report'
assert 'data-view="report"' in page or 'data-initial-view="report"' in page, 'Default report mode not found'
assert len(model['slides']) == 54 and content['source_blocks'] == 69
assert not content['missing_content']
assert len([s for s in model['slides'] if re.fullmatch('e[0-9]{2}',s['id'])]) == 24

plain = lambda value: re.sub(r'\s+', '', value.replace('**','').replace('`',''))
visible_parts = [model['title']]
for slide in model['slides']:
    visible_parts.extend([slide['title'], slide['section']])
    for element in slide['elements']:
        visible_parts.append(element.get('text', '\n'.join(' | '.join(row) for row in element.get('rows', []))))
visible = '\n'.join(visible_parts)
visible = plain(visible)
for source in ['04_final_report.md', '02_evidence_matrix.md']:
    for line in (OUT/source).read_text().splitlines():
        line = line.strip()
        if source.startswith('02'):
            if not re.match(r'\|\s*E[0-9]{2}\s*\|',line): continue
        if not line: continue
        values = line.strip('|').split('|') if line.startswith('|') else [line.lstrip('#').strip()]
        for value in values:
            value=plain(value)
            if not value or re.fullmatch('[:-]+',value): continue
            assert value in visible, (source,value[:100])

assets=load(OUT/'html_src/operational_image_manifest.json')
image_checks=[]
ids=[s['id'] for s in model['slides']]
for asset in assets:
    data=(OUT/asset['original']).read_bytes()
    assert sha(data)==asset['sha256']
    assert data[:8]==b'\x89PNG\r\n\x1a\n'
    assert list(struct.unpack('>II',data[16:24]))==asset['pixels']
    assert asset['crop']==[0,0,*asset['pixels']]
    identity='operation-photo-'+asset['id'].lower()
    assert ids.index(identity)==ids.index(asset['anchor'])+1
    slide=model['slides'][ids.index(identity)]
    images=[e for e in slide['elements'] if e['type']=='image']
    assert len(images)==1 and images[0]['src'].startswith('data:image/png;base64,')
    assert base64.b64decode(images[0]['src'].split(',',1)[1])==data
    image_checks.append({'id':asset['id'],'sha256':asset['sha256'],'pixels':asset['pixels'],'embedded_excerpt_matches':True,'after':asset['anchor']})
source_hashes={a['source_sha256'] for a in assets}
for encoded in re.findall(r'data:image/(?:png|jpeg|gif|svg\+xml);base64,([A-Za-z0-9+/]+={0,2})(?=[\"\'])',page):
    assert sha(base64.b64decode(encoded)) not in source_hashes, 'Full original screenshot embedded'

scripts=re.findall(r'<script\b([^>]*)>(.*?)</script>',page,re.S)
styles=re.findall(r'<style\b[^>]*>(.*?)</style>',page,re.S)
csp=html.unescape(re.search(r'<meta http-equiv="Content-Security-Policy" content="([^"]+)"',page).group(1))
node=shutil.which('node')
assert node, 'Node.js is required for script syntax checks'
count=0
with tempfile.TemporaryDirectory(prefix='shanqin-static-') as temp:
    for attrs,script in scripts:
        if 'application/json' in attrs: continue
        signature="'sha256-"+base64.b64encode(hashlib.sha256(script.encode()).digest()).decode()+"'"
        assert signature in csp
        js=Path(temp)/f'{count}.js'; js.write_text(script)
        result=subprocess.run([node,'--check',str(js)],capture_output=True,text=True)
        assert result.returncode==0,result.stderr
        count+=1
for style in styles:
    assert "'sha256-"+base64.b64encode(hashlib.sha256(style.encode()).digest()).decode()+"'" in csp
assert "connect-src 'none'" in csp
assert not re.search(r'(?:src|href)="(?:https?://|file:|/Users/)',page)

# The ECC hook's AWS pattern also occurs in the known HK Technology PNG.
# Its exception is limited to an entire, byte-exact contentLogo data-URI line.
aws_pattern = re.compile(r'AKIA[0-9A-Z]{16}')
logo_hash = 'b93109ee0088041ae853a4e15dce5fd895d823f6134a725d7ce8213b2d821035'
logo_false_positives = 0
for line in page.splitlines():
    if not aws_pattern.search(line):
        continue
    match = re.fullmatch(r'\s*"contentLogo": "data:image/png;base64,([A-Za-z0-9+/=]+)",?', line)
    assert match, 'Unexpected credential-pattern location'
    assert sha(base64.b64decode(match[1], validate=True)) == logo_hash
    logo_false_positives += 1
assert logo_false_positives == 2


links=0
for name in files:
    if not name.endswith('.md'): continue
    path=ARCHIVE/name; text=path.read_text()
    text=re.sub(r'```.*?```','',text,flags=re.S)
    text=re.sub(r'`[^`]*`','',text)
    for target in re.findall(r'!?\[[^\]]*\]\((<[^>]+>|[^)]+)\)',text):
        target=target.strip('<>'); parsed=urlsplit(target)
        if parsed.scheme or not parsed.path: continue
        dest=(path.parent/unquote(parsed.path)).resolve()
        assert dest.is_file() or dest == RECEIPT, (name,target)
        assert str(dest.relative_to(ARCHIVE)) in files, (name,'not published',target)
        links+=1
sources=load(OUT/'evidence/source_manifest.json')
assert len(sources['sources'])==98
bundled=0
for source in sources['sources']:
    if source['path']:
        p=OUT/'evidence'/source['path']
        assert sha(p.read_bytes())==source['sha256'],source['id']
        bundled+=1
assert bundled==5
# Screen literal text files for common credential forms and personal absolute paths.
for name in files:
    path=ARCHIVE/name
    if path==RECEIPT or not path.exists() or path.suffix=='.png': continue
    text=path.read_text()
    assert not re.search(r'/Users/[A-Za-z0-9_.-]+/',text),name
    assert not re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',text),name

receipt={'date':'2026-10-15','status':'static_checks_passed','html_sha256':sha(page.encode()),'theme':'hk-technology','default_view':'report','slides':len(model['slides']),'source_blocks':69,'evidence_items':24,'images':image_checks,'full_original_screenshots_embedded':False,'relative_links_checked':links,'bundled_source_hashes_verified':bundled,'scripts_syntax_checked':count,'csp_hashes_verified':True,'external_resource_references':0,'public_files':len(files),'ecc_aws_false_positives':{'count':logo_false_positives,'png_sha256':logo_hash,'scope':'exact contentLogo data URI lines only'},'not_verified':['browser visual layout','browser interaction and save/reopen','PDF print pagination'],'files_sha256':{name:sha((ARCHIVE/name).read_bytes()) for name in files if ARCHIVE/name != RECEIPT}}
RECEIPT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in {'files_sha256','images'}},ensure_ascii=False,indent=2))
