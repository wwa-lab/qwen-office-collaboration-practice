#!/usr/bin/env python3
"""Build the trilingual brief with corporate-web-slides' native Report renderer.

management_brief_model.json is the sole editable content model. The HTML,
Report/Slides views and Office exports are derived from it.
"""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
SKILL = Path(os.environ.get('CORPORATE_WEB_SLIDES_SKILL', str(Path.home() / '.codex/skills/corporate-web-slides'))).expanduser()
if not (SKILL / 'scripts/build.py').is_file():
    raise SystemExit('Set CORPORATE_WEB_SLIDES_SKILL to the installed corporate-web-slides directory.')
sys.path.insert(0, str(SKILL / 'scripts'))
import build
import localization

sha = lambda data: hashlib.sha256(data).hexdigest()
source = HERE / 'management_brief_model.json'
model = json.loads(source.read_text())
assert model['i18n']['defaultLanguage'] == model['i18n']['language'] == 'en'
assert set(model['i18n']['translations']) == {'en', 'zh-Hans', 'zh-Hant'}
assert not any(model['i18n']['stale'].values())
fields = localization.fields(model)
assert all(set(bundle) == set(fields) for bundle in model['i18n']['translations'].values())
# Native skill validation resolves the local pictures and validates all locales.
deck = build.normalize(model, HERE)
manifest = json.loads((HERE / 'operational_image_manifest.json').read_text())
expected = {a['sha256']:a for a in manifest if a['id'] != 'UI-06'}
images = [el for slide in deck['slides'] for el in slide['elements'] if el['type'] == 'image']
assert len(images) == 5
used = []
for image in images:
    digest = sha(base64.b64decode(image['src'].split(',', 1)[1]))
    assert digest in expected, 'Screenshot bytes changed'
    asset = expected[digest]
    used.append({k:asset[k] for k in ('id', 'original', 'sha256')})
assert len({a['id'] for a in used}) == 5
page = build.render_html(deck, view='report')
# Format data only, leaving the native renderer/runtime and decoded values intact.
# Separate fields let the repository's exact known-image allowlist match only
# the approved logo rather than an entire JSON script containing other content.
def readable_json(match):
    value = json.loads(match[2])
    formatted = json.dumps(value, ensure_ascii=False, indent=2).replace('<', '\\u003c').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
    assert json.loads(formatted) == value
    return match[1] + '\n' + formatted + '\n' + match[3]
page = re.sub(r'(<script\b[^>]*type="application/json"[^>]*>)(.*?)(</script>)', readable_json, page, flags=re.S)
assert 'data-view="report"' in page and 'id="deck-data"' in page
assert not re.search(r'(?:src|href)=[\"\'](?:https?://|file:|/Users/)', page)
scripts = [s for attrs,s in re.findall(r'<script\b([^>]*)>(.*?)</script>', page, re.S) if 'application/json' not in attrs]
with tempfile.TemporaryDirectory() as td:
    for i, script in enumerate(scripts):
        p = Path(td)/f'{i}.js'; p.write_text(script)
        subprocess.run(['node', '--check', str(p)], check=True, capture_output=True)
output = OUT / '08_management_brief.html'
output.write_text(page)
components = ['scripts/build.py', 'scripts/contracts.py', 'scripts/localization.py', 'scripts/raster.py',
              'assets/shell.html', 'assets/style.css', 'assets/report.css', 'assets/contracts.json',
              'assets/layouts.json', 'assets/brands/hsbc/brand.json', 'references/upstream-LICENSE.txt']
components += ['assets/' + name + '.js' for name in ('theme', 'ui-translations', 'i18n', 'model', 'qa', 'editor', 'render', 'report', 'export', 'app')]
components += [str(p.relative_to(SKILL)) for p in (SKILL/'assets/vendor').iterdir() if p.is_file()]
for theme in sorted((SKILL/'assets/themes').glob('*.json')):
    components.append(str(theme.relative_to(SKILL)))
    for media in json.loads(theme.read_text()).get('media', {}).values():
        if isinstance(media, str) and not media.startswith('data:'):
            components.append(str((theme.parent/media).resolve().relative_to(SKILL.resolve())))
components = sorted(set(components))
record = {'date':'2026-10-15', 'skill':'corporate-web-slides', 'skill_version':'1.3.0', 'renderer':'build.render_html(deck, view="report")', 'default_view':'report', 'default_language':'en', 'languages':['en','zh-Hans','zh-Hant'], 'sections':len(deck['slides']), 'translation_fields_per_language':len(fields), 'model_source':source.name, 'model_sha256':sha(source.read_bytes()), 'html_sha256':sha(output.read_bytes()), 'report_sha256':sha((OUT/'04_final_report.md').read_bytes()), 'matrix_sha256':sha((OUT/'02_evidence_matrix.md').read_bytes()), 'images':used, 'standalone':True, 'scripts_syntax_checked':len(scripts), 'native_skill_renderer_unmodified':True, 'build_dependencies':{name:sha((SKILL/name).read_bytes()) for name in components}, 'not_verified':['browser layout and interactions after this build','file:// opening','Office application rendering','PDF pagination']}
(OUT/'qa/management_brief_checks.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:record[k] for k in ('skill','default_view','default_language','sections','translation_fields_per_language','html_sha256')}))
