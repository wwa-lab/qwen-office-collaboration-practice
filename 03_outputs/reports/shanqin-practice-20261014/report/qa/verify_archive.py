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
import sys
import tempfile
import zipfile
from urllib.parse import unquote, urlsplit

ARCHIVE = Path(__file__).resolve().parents[2]
OUT = ARCHIVE / 'report'
RECEIPT = OUT / 'qa/archive_checks.json'
sha = lambda data: hashlib.sha256(data).hexdigest()
load = lambda p: json.loads(p.read_text(encoding='utf-8'))
manifest = load(ARCHIVE / 'publication_files.json')
files = manifest['files']
assets = load(OUT/'html_src/operational_image_manifest.json')
image_paths = {'report/' + a['original'] for a in assets}
assert len(files) == len(set(files))
for name in files:
    path = ARCHIVE / name
    assert not Path(name).is_absolute() and '..' not in Path(name).parts, name
    assert path.is_file() or path == RECEIPT, name
    assert not any(part in {'.local-only', 'evidence_supplement', 'fonts', 'fontcache', 'operations'} for part in path.parts), name
    assert path.suffix.lower() not in {'.jsonl', '.skill', '.zip', '.ttc', '.ttf', '.pdf', '.docx'}, name
    if path.suffix.lower() in {'.jpg', '.png'}:
        assert name in image_paths, name

page = (OUT / '04_final_report.html').read_text(encoding='utf-8')
model = json.loads(re.search(r'<script[^>]*id="deck-data"[^>]*>(.*?)</script>', page, re.S).group(1))
config = json.loads(re.search(r'<script[^>]*id="corporate-config"[^>]*>(.*?)</script>', page, re.S).group(1))
content = load(OUT / 'html_src/content_map.json')
assert content['html_sha256'] == sha(page.encode())
assert content['report_sha256'] == sha((OUT/'04_final_report.md').read_bytes())
assert content['matrix_sha256'] == sha((OUT/'02_evidence_matrix.md').read_bytes())
assert model['theme']['id'] == 'hk-technology' and content['default_view'] == 'report'
assert 'data-view="report"' in page or 'data-initial-view="report"' in page, 'Default report mode not found'
assert len(model['slides']) == content['slides'] and content['source_blocks'] == 69
assert content['language'] == model['i18n']['defaultLanguage'] == model['i18n']['language'] == 'en'
assert content['languages'] == ['en', 'zh-Hans', 'zh-Hant']
assert content['locales_sha256'] == sha((OUT/'html_src/report_locales.json').read_bytes())
bundles = model['i18n']['translations']
assert all(set(bundles[lang]) == set(bundles['en']) for lang in content['languages'])
assert not any(model['i18n']['stale'].values())
assert not re.search('[\u3400-\u9fff]', '\n'.join(bundles['en'].values())), 'Untranslated English content'
assert not content['missing_content']
assert len([s for s in model['slides'] if re.fullmatch('e[0-9]{2}',s['id'])]) == 24

plain = lambda value: re.sub(r'\s+', '', value.replace('**','').replace('`',''))
source_bundle = bundles['zh-Hans']
source_value = lambda parts: source_bundle[json.dumps(parts,ensure_ascii=False,separators=(',',':'))]
visible_parts = [source_value(['title'])]
for slide in model['slides']:
    prefix = ['slides', slide['id']]
    visible_parts.extend([source_value(prefix+['title']), source_value(prefix+['section'])])
    for element in slide['elements']:
        path = prefix+['elements',element['id']]
        if 'paragraphs' in element:
            visible_parts.append('\n'.join(''.join(source_value(path+['paragraphs',i,'runs',j,'text']) for j,_ in enumerate(p['runs'])) for i,p in enumerate(element['paragraphs'])))
        elif 'text' in element:
            visible_parts.append(source_value(path+['text']))
        for i,row in enumerate(element.get('rows', [])):
            visible_parts.extend(source_value(path+['rows',i,j]) for j,_ in enumerate(row))
visible = '\n'.join(visible_parts)
visible = plain(visible)
for source in ['04_final_report.md', '02_evidence_matrix.md']:
    for line in (OUT/source).read_text().splitlines():
        line = line.strip()
        if line.startswith(('<!-- screenshot:', '![')): continue
        if source.startswith('02'):
            if not re.match(r'\|\s*E[0-9]{2}\s*\|',line): continue
        if not line: continue
        values = line.strip('|').split('|') if line.startswith('|') else [line.lstrip('#').strip()]
        for value in values:
            value=plain(value)
            if not value or re.fullmatch('[:-]+',value): continue
            assert value in visible, (source,value[:100])

def jpeg_size(data):
    assert data[:2] == b'\xff\xd8'
    offset = 2
    while offset < len(data):
        assert data[offset] == 255
        while data[offset] == 255: offset += 1
        marker = data[offset]; offset += 1
        length = int.from_bytes(data[offset:offset+2], 'big')
        if marker in {0xc0, 0xc1, 0xc2}:
            height, width = struct.unpack('>HH', data[offset+3:offset+7])
            return [width, height]
        assert length >= 2
        offset += length
    raise AssertionError('JPEG dimensions missing')

image_checks=[]
ids=[s['id'] for s in model['slides']]
for asset in assets:
    data=(OUT/asset['original']).read_bytes()
    assert sha(data)==asset['sha256']
    if asset['mime'] == 'image/png':
        assert data[:8]==b'\x89PNG\r\n\x1a\n'
        pixels = list(struct.unpack('>II',data[16:24]))
    else:
        assert asset['mime'] == 'image/jpeg' and asset['capture_method'] == 'browser_screenshot'
        pixels = jpeg_size(data)
    assert pixels == asset['pixels']
    assert asset['crop']==[0,0,*asset['pixels']]
    identity='operation-photo-'+asset['id'].lower()
    assert ids.index(identity)==ids.index(asset['anchor'])+1
    slide=model['slides'][ids.index(identity)]
    images=[e for e in slide['elements'] if e['type']=='image']
    assert len(images)==1 and images[0]['src'].startswith('data:'+asset['mime']+';base64,')
    assert base64.b64decode(images[0]['src'].split(',',1)[1])==data
    image_checks.append({'id':asset['id'],'sha256':asset['sha256'],'pixels':asset['pixels'],'embedded_excerpt_matches':True,'after':asset['anchor']})
source_hashes={a['source_sha256'] for a in assets if a.get('capture_method') != 'browser_screenshot'}
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


REPO = ARCHIVE.parents[2]
readme_names = ('README.md', 'README.zh-Hans.md', 'README.zh-Hant.md')
readme_paths = [folder / name for folder in (REPO, ARCHIVE, ARCHIVE/'source_materials') for name in readme_names]
for path in readme_paths:
    nav = path.read_text().splitlines()[2]
    active = {'README.md': 'English', 'README.zh-Hans.md': '简体中文', 'README.zh-Hant.md': '繁體中文'}[path.name]
    assert f'**{active}**' in nav, path
    for other in readme_names:
        if other != path.name:
            assert f']({other})' in nav, (path, other)

translation_manifest = load(OUT/'html_src/markdown_translations.json')
translations = translation_manifest['files']
assert len(translations) == 14
assert len({entry['source'] for entry in translations}) == len(translations)
assert len({entry['english'] for entry in translations}) == len(translations)
english_files = {entry['english'] for entry in translations}
original_markdown = {name for name in files if name.endswith('.md') and not Path(name).name.startswith('README') and name not in english_files}
assert original_markdown == {entry['source'] for entry in translations}, 'Markdown translation coverage mismatch'
for entry in translations:
    for key in ('source', 'english'):
        assert entry[key] in files, entry[key]
        assert sha((ARCHIVE/entry[key]).read_bytes()) == entry[key+'_sha256'], ('Translation fingerprint is stale', entry[key])
    source = ARCHIVE/entry['source']
    target = ARCHIVE/entry['english']
    assert str(source.name) in target.read_text().splitlines()[2], ('Missing original-language link', target)
result = subprocess.run([sys.executable, str(OUT/'html_src/build_english_report.py'), '--check'], capture_output=True, text=True)
assert result.returncode == 0, result.stdout + result.stderr
english_report = (OUT/'04_final_report_EN.md').read_text()
original_report = (OUT/'04_final_report.md').read_text()
assert re.findall(r'!\[[^\]]*\]\(([^)]+)\)', english_report) == re.findall(r'!\[[^\]]*\]\(([^)]+)\)', original_report)
assert 'Practitioner: Leo Zhang' in english_report

links=0
markdown_paths = [ARCHIVE/name for name in files if name.endswith('.md')] + [REPO/name for name in readme_names]
published_paths = {ARCHIVE/name for name in files} | {REPO/name for name in readme_names}
for path in markdown_paths:
    name=str(path.relative_to(REPO)); text=path.read_text()
    text=re.sub(r'```.*?```','',text,flags=re.S)
    text=re.sub(r'`[^`]*`','',text)
    for target in re.findall(r'!?\[[^\]]*\]\((<[^>]+>|[^)]+)\)',text):
        target=target.strip('<>'); parsed=urlsplit(target)
        if parsed.scheme or not parsed.path: continue
        dest=(path.parent/unquote(parsed.path)).resolve()
        assert dest.is_file() or dest == RECEIPT, (name,target)
        assert dest in published_paths, (name,'not published',target)
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
    if path==RECEIPT or not path.exists() or name in image_paths: continue
    if path.suffix in {'.pptx', '.potx'}:
        with zipfile.ZipFile(path) as package:
            text='\n'.join(package.read(part).decode('utf-8') for part in package.namelist() if part.endswith(('.xml', '.rels')))
    else:
        text=path.read_text()
    assert not re.search(r'/Users/[A-Za-z0-9_.-]+/',text),name
    assert not re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',text),name

receipt={'date':'2026-10-15','status':'static_checks_passed','html_sha256':sha(page.encode()),'theme':'hk-technology','default_view':'report','slides':len(model['slides']),'source_blocks':69,'evidence_items':24,'images':image_checks,'full_original_screenshots_embedded':False,'relative_links_checked':links,'bundled_source_hashes_verified':bundled,'scripts_syntax_checked':count,'csp_hashes_verified':True,'external_resource_references':0,'public_files':len(files),'ecc_aws_false_positives':{'count':logo_false_positives,'png_sha256':logo_hash,'scope':'exact contentLogo data URI lines only'},'not_verified':['browser visual layout','browser interaction and save/reopen','PDF print pagination'],'files_sha256':{name:sha((ARCHIVE/name).read_bytes()) for name in files if ARCHIVE/name != RECEIPT}}
brief_checks = load(OUT/'qa/management_brief_checks.json')
assert brief_checks['html_sha256'] == sha((OUT/'08_management_brief.html').read_bytes())
assert brief_checks['model_sha256'] == sha((OUT/'html_src/management_brief_model.json').read_bytes())
assert brief_checks['skill'] == 'corporate-web-slides'
assert brief_checks['native_skill_renderer_unmodified'] and brief_checks['default_view'] == 'report'
assert brief_checks['default_language'] == 'en'
assert brief_checks['languages'] == ['en', 'zh-Hans', 'zh-Hant']
assert brief_checks['report_sha256'] == sha((OUT/'04_final_report.md').read_bytes())
assert brief_checks['matrix_sha256'] == sha((OUT/'02_evidence_matrix.md').read_bytes())
if brief_checks['browser']['html_sha256'] != brief_checks['html_sha256']:
    # Preserve the original browser-test fingerprint. Reuse is justified only
    # by a recorded JSON-whitespace-only change, with identical runtime/data.
    formatting = brief_checks['json_formatting_equivalence']
    assert formatting['from_html_sha256'] == brief_checks['browser']['html_sha256']
    assert formatting['to_html_sha256'] == brief_checks['html_sha256']
    brief_page = (OUT/'08_management_brief.html').read_text()
    json_pattern = r'(<script\b[^>]*type="application/json"[^>]*>)(.*?)(</script>)'
    canonical = re.sub(json_pattern, lambda m: m[1] + json.dumps(json.loads(m[2]), ensure_ascii=False, sort_keys=True, separators=(',', ':')) + m[3], brief_page, flags=re.S)
    assert sha(canonical.encode()) == formatting['canonical_html_sha256']
    assert formatting['decoded_json_equal'] and formatting['outside_json_bytes_equal']
    assert formatting['browser_rerun'] is False
brief_logo_hits = 0
for line in (OUT/'08_management_brief.html').read_text().splitlines():
    if not aws_pattern.search(line): continue
    match = re.fullmatch(r'\s*"contentLogo": "data:image/png;base64,([A-Za-z0-9+/=]+)",?', line)
    assert match and sha(base64.b64decode(match[1], validate=True)) == logo_hash
    brief_logo_hits += 1
assert brief_logo_hits == 2
for office_file in brief_checks['office']['files']:
    if 'report/' + office_file['file'] in files:
        assert office_file['sha256'] == sha((OUT/office_file['file']).read_bytes())
receipt['management_brief_checks'] = 'management_brief_checks.json'
receipt['markdown_translations'] = {'pairs': len(translations), 'source_and_english_fingerprints_verified': True, 'english_report_matches_reviewed_catalog': True, 'six_screenshot_paths_preserved': True}
receipt['readme_languages'] = {'default': 'en', 'available': ['en', 'zh-Hans', 'zh-Hant'], 'entry_points': 3, 'files_checked': len(readme_paths), 'root_readme_sha256': {name: sha((REPO/name).read_bytes()) for name in readme_names}}
browser_checks = load(OUT/'qa/browser_checks.json')
assert browser_checks['html_sha256'] == receipt['html_sha256'], 'Browser checks are stale'
for office_file in browser_checks['native_exports']['files']:
    if 'report/' + office_file['file'] in files:
        assert office_file['sha256'] == sha((OUT/office_file['file']).read_bytes())
receipt['browser_checks'] = 'browser_checks.json'
receipt['not_verified'] = browser_checks['not_verified']
# The excluded originals are private full-window captures, not the newly
# published business webpage screenshots captured directly by the browser.
receipt['private_full_window_screenshots_embedded'] = receipt.pop('full_original_screenshots_embedded')
receipt['direct_browser_screenshots'] = sum(a.get('capture_method') == 'browser_screenshot' for a in assets)
RECEIPT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in {'files_sha256','images'}},ensure_ascii=False,indent=2))
