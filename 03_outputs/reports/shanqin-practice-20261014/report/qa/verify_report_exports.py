#!/usr/bin/env python3
"""Check the formal report's native exports; does not launch PowerPoint."""
import base64
import hashlib
import json
from pathlib import Path
import posixpath
import re
import xml.etree.ElementTree as ET
import zipfile

OUT = Path(__file__).resolve().parents[1]
page = (OUT/'04_final_report.html').read_text()
deck = json.loads(re.search(r'<script[^>]*id="deck-data"[^>]*>(.*?)</script>', page, re.S)[1])
sha = lambda b: hashlib.sha256(b).hexdigest()
compact = lambda s: re.sub(r'\s+', '', s)
key = lambda p: json.dumps(p, ensure_ascii=False, separators=(',', ':'))
ns = {'a':'http://schemas.openxmlformats.org/drawingml/2006/main', 'p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
originals = {sha(base64.b64decode(e['src'].split(',')[1])) for s in deck['slides'] for e in s['elements'] if e['type']=='image'}

def check(path, language, extra=False, title_override=None):
    bundle = deck['i18n']['translations'][language]
    value = lambda p: bundle[key(p)]
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        slides = [n for n in names if re.fullmatch(r'ppt/slides/slide\d+\.xml',n)]
        notes = [n for n in names if re.fullmatch(r'ppt/notesSlides/notesSlide\d+\.xml',n)]
        assert len(slides) == len(notes) == len(deck['slides'])+int(extra)
        pictures = shapes = tables = 0
        for i,s in enumerate(deck['slides'],1):
            root = ET.fromstring(z.read(f'ppt/slides/slide{i}.xml'))
            visible = compact(''.join(t.text or '' for t in root.findall('.//a:t',ns)))
            prefix = ['slides',s['id']]
            title = title_override if i==1 and title_override else value(prefix+['title'])
            assert compact(title) in visible, (path.name,i,'title')
            for e in s['elements']:
                ep = prefix+['elements',e['id']]
                if 'paragraphs' in e:
                    expected = '\n'.join(''.join(value(ep+['paragraphs',pi,'runs',ri,'text']) for ri,_ in enumerate(p['runs'])) for pi,p in enumerate(e['paragraphs']))
                    assert compact(expected) in visible,(path.name,i,e['id'])
                elif 'text' in e:
                    assert compact(value(ep+['text'])) in visible,(path.name,i,e['id'])
                for ri,row in enumerate(e.get('rows',[])):
                    for ci,_ in enumerate(row):
                        assert compact(value(ep+['rows',ri,ci])) in visible,(path.name,i,e['id'],ri,ci)
            note = ET.fromstring(z.read(f'ppt/notesSlides/notesSlide{i}.xml'))
            assert compact(value(prefix+['notes'])) in compact(''.join(t.text or '' for t in note.findall('.//a:t',ns)))
            pictures += len(root.findall('.//p:pic',ns))
            shapes += len(root.findall('.//p:sp',ns))
            tables += len(root.findall('.//a:tbl',ns))
        assert pictures == len(originals) == 6 and shapes > 100 and tables > 0
        assert originals <= {sha(z.read(n)) for n in names if n.startswith('ppt/media/')}
        for name in names:
            if not name.endswith('.rels'): continue
            parent = '' if name=='_rels/.rels' else posixpath.dirname(posixpath.dirname(name))
            for rel in ET.fromstring(z.read(name)):
                if rel.get('TargetMode')=='External':
                    assert 'image' not in rel.get('Type','')
                    continue
                target = rel.get('Target','')
                resolved = target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join(parent,target))
                assert resolved in names,(name,resolved)
        layout_names = [n for n in names if re.fullmatch(r'ppt/slideLayouts/slideLayout\d+\.xml',n)]
        layouts = {ET.fromstring(z.read(n)).find('p:cSld',ns).get('name'):n for n in layout_names}
        content = ET.fromstring(z.read(layouts['HSBC_CONTENT']))
        assert content.findall('.//p:ph',ns) and content.findall('.//p:pic',ns)
        if extra:
            rels = ET.fromstring(z.read(f'ppt/slides/_rels/slide{len(slides)}.xml.rels'))
            target = next(r.get('Target') for r in rels if r.get('Type','').endswith('/slideLayout'))
            assert posixpath.normpath(posixpath.join('ppt/slides',target)) == layouts['HSBC_CONTENT']
        if path.suffix=='.potx': assert b'presentationml.template.main+xml' in z.read('[Content_Types].xml')
        return {'file':path.name,'sha256':sha(path.read_bytes()),'language':language,'slides':len(slides),'notes':len(notes),'native_pictures':pictures,'native_text_shapes':shapes,'native_tables':tables,'text_notes_and_original_images_match':True,'internal_relationships_resolve':True,'content_layout_has_placeholders_and_brand':True}

if __name__=='__main__':
    results = [check(OUT/f'04_final_report_{suffix}.pptx',lang) for lang,suffix in [('en','EN'),('zh-Hans','SC'),('zh-Hant','TC')]]
    results.append(check(OUT/'04_final_report_EN.potx','en'))
    extra = OUT/'.local-only/qa-report-new-slide.pptx'
    if extra.exists(): results.append(check(extra,'en',extra=True))
    record_path = OUT/'qa/browser_checks.json'
    record = json.loads(record_path.read_text())
    assert record['html_sha256']==sha(page.encode()),'Browser receipt is stale'
    record['native_exports'] = {'method':'Unmodified skill export component in a local Node VM with native canvas; OOXML validation','files':results,'new_slide_layout_inheritance':extra.exists(),'office_ui_verified':False}
    browser = OUT/'.local-only/qa-report-browser-edited.pptx'
    if browser.exists():
        record['browser_export'] = {'method':'Native browser export of edited/reopened Traditional Chinese model; QA byte-capture transport, not actual download delivery','file':check(browser,'zh-Hant',title_override='正式報告三語驗證')}
    record_path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'exports':len(results),'slides':len(deck['slides']),'original_images':len(originals),'office_ui_verified':False}))
