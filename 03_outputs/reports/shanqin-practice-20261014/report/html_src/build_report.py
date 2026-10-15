#!/usr/bin/env python3
"""Derive the offline report from the corrected Markdown and evidence matrix.

The corporate-web-slides model remains the only browser content source.
Task-local CSS/JS change reading and printing, not the shared skill runtime.
"""
import base64
import copy
import hashlib
import html
import json
import math
import os
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
SKILL = Path(os.environ.get('CORPORATE_WEB_SLIDES_SKILL', str(Path.home() / '.codex/skills/corporate-web-slides'))).expanduser()
if not (SKILL / 'scripts/build.py').is_file():
    raise SystemExit('Set CORPORATE_WEB_SLIDES_SKILL to the installed corporate-web-slides 1.3.0 directory.')
sys.path.insert(0, str(SKILL / 'scripts'))
import build
import localization

LOCALES = json.loads((HERE / 'report_locales.json').read_text())['translations']
LANGUAGES = ('en', 'zh-Hans', 'zh-Hant')

def translate_atom(value, language):
    if language == 'zh-Hans':
        return value
    bundle = LOCALES[language]
    if value in bundle:
        return bundle[value]
    if value.endswith('（续）'):
        return translate_atom(value[:-3], language) + (' (cont.)' if language == 'en' else '（續）')
    raise ValueError(f'Missing {language} translation: {value}')

def translate_model(model, language):
    result = copy.deepcopy(model)
    result['title'] = translate_atom(result['title'], language)
    for slide in result['slides']:
        for field in ('title', 'section'):
            slide[field] = translate_atom(slide[field], language)
        for element in slide['elements']:
            if 'paragraphs' in element:
                for paragraph in element['paragraphs']:
                    for run in paragraph['runs']:
                        run['text'] = translate_atom(run['text'], language)
                element['text'] = '\n'.join(''.join(r['text'] for r in p['runs']) for p in element['paragraphs'])
            elif 'text' in element:
                element['text'] = translate_atom(element['text'], language)
            for field in ('alt', 'altText'):
                if field in element:
                    element[field] = translate_atom(element[field], language)
            if 'rows' in element:
                element['rows'] = [[translate_atom(cell, language) for cell in row] for row in element['rows']]
        # These notes are the complete source content, as in the monolingual report.
        slide['notes'] = '\n\n'.join(el.get('text', '\n'.join(' | '.join(r) for r in el.get('rows', []))) for el in slide['elements'])
    return result

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def plain(value):
    return value.replace('**', '').replace('`', '').strip()

def units(value):
    return sum(1 if ord(c) > 255 else .55 for c in value)

def paragraphs(value):
    result = []
    for line in value.split('\n'):
        runs = []
        for i, part in enumerate(line.replace('`', '').split('**')):
            for token in re.split(r'(E\d{2}|U[123])', part):
                if not token:
                    continue
                run = {'text': token}
                if i % 2:
                    run['bold'] = True
                if re.fullmatch(r'E\d{2}', token):
                    run.update(hyperlink='#' + token.lower(), color='B80010')
                elif re.fullmatch(r'U[123]', token):
                    run.update(hyperlink='#sources-1', color='B80010')
                runs.append(run)
        result.append({'runs': runs or [{'text': ''}]})
    return result

def text_element(identity, value, y, height, font=32, width=1440, x=80):
    ps = paragraphs(value)
    return {'id': identity, 'type': 'text', 'text': '\n'.join(''.join(r['text'] for r in p['runs']) for p in ps),
            'paragraphs': ps, 'x': x, 'y': y, 'w': width, 'h': height,
            'fontSize': font, 'color': '222222'}

def text_height(value, font=32, width=1440):
    versions = ['\n'.join(''.join(translate_atom(r['text'], lang) for r in p['runs']) for p in paragraphs(value)) for lang in LANGUAGES]
    lines = max(sum(max(1, math.ceil(units(p) / (width / font - 2))) for p in text.split('\n')) for text in versions)
    return math.ceil(lines * font * 1.32 + 12)

source = OUT / '04_final_report.md'
matrix = OUT / '02_evidence_matrix.md'
image_manifest = json.loads((HERE / 'operational_image_manifest.json').read_text())
source_text = source.read_text()
# Markdown and HTML share the same figures and captions. Preserve source line
# numbers while removing figure blocks from the prose pagination pass.
for asset in image_manifest:
    expected = (f"![{asset['caption']}]({asset['original']})\n\n"
                f"**{asset['caption']}**\n\n{asset['source']}\n\n"
                f"{asset['observation']}\n\n{asset['limit']} 对应：{asset['evidence']}。")
    pattern = rf"<!-- screenshot:{asset['id']}:start -->\n(.*?)\n<!-- screenshot:{asset['id']}:end -->"
    matches = list(re.finditer(pattern, source_text, re.S))
    assert len(matches) == 1 and matches[0][1] == expected, asset['id']
    source_text = re.sub(pattern, lambda m: '\n' * m[0].count('\n'), source_text, flags=re.S)
assert '<!-- screenshot:' not in source_text
lines = source_text.splitlines()
blocks = []
i = 0
while i < len(lines):
    value = lines[i].strip()
    if not value:
        i += 1
        continue
    start = i + 1
    if value.startswith('#'):
        level = len(value) - len(value.lstrip('#'))
        blocks.append({'type': 'heading', 'level': level, 'text': value[level:].strip(), 'line': start})
        i += 1
    elif value.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].strip().startswith('|'):
            cells = [plain(v) for v in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?', c.replace(' ', '')) for c in cells):
                rows.append(cells)
            i += 1
        blocks.append({'type': 'table', 'rows': rows, 'line': start})
    else:
        parts = []
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(('#', '|')):
            parts.append(lines[i].strip())
            i += 1
        # Numbered paragraphs retain their numbering as authored.
        value = '\n'.join(parts) if len(parts) > 1 else parts[0]
        blocks.append({'type': 'text', 'text': value, 'line': start})

theme = copy.deepcopy(next(t for t in build.CONFIG['themes'] if t['id'] == 'hk-technology'))
deck = {'version': 1, 'modelVersion': '1.1', 'id': 'shanqin-management-report-20261014-u3',
        'title': blocks[0]['text'], 'brand': copy.deepcopy(build.CONFIG['brand']), 'theme': theme,
        'slides': [], 'warnings': []}
deck['brand']['footer'] = 'HK Technology'
coverage = []

def add_slide(identity, title, section, elements, layout='content', notes=None):
    slide = {'id': identity, 'title': title, 'section': section, 'layout': layout,
             'titleStyle': {'fontSize': 40}, 'elements': elements,
             'notes': notes or '\n\n'.join(el.get('text', '\n'.join(' | '.join(r) for r in el.get('rows', []))) for el in elements)}
    deck['slides'].append(slide)
    return slide

cover = add_slide('cover', deck['title'], '封面',
                  [text_element('cover-meta', blocks[1]['text'], 320, 190, 30, 1350)], 'cover')
cover['titleBox'] = {'x': 60, 'y': 35, 'w': 1480, 'h': 230}
cover['titleStyle'] = {'fontSize': 64}
coverage.extend([{'line': blocks[0]['line'], 'slide': 'cover'}, {'line': blocks[1]['line'], 'slide': 'cover'}])

# Preserve the authored hierarchy, splitting only where the Slides canvas needs it.
groups = []
section = title = ''
for block in blocks[2:]:
    if block['type'] == 'heading':
        if block['level'] == 2:
            section = block['text']
        title = block['text']
        groups.append({'section': section, 'title': title, 'heading': block, 'blocks': []})
    else:
        groups[-1]['blocks'].append(block)

group_no = 0
for group in groups:
    if not group['blocks']:
        continue
    group_no += 1
    section, title = group['section'], group['title']
    prefix = 'sources' if title.startswith('附录D') else 'body-' + str(group_no).zfill(2)
    chunk, height, part = [], 0, 0
    def emit():
        global chunk, height, part
        if not chunk:
            return
        part += 1
        identity = f'{prefix}-{part}'
        display_title = title if part == 1 else title + '（续）'
        elements, y = [], 210
        for n, item in enumerate(chunk):
            block, size = item
            eid = f'{identity}-item-{n}'
            if block['type'] == 'text':
                el = text_element(eid, block['text'], y, size)
            else:
                el = {'id': eid, 'type': 'table', 'x': 80, 'y': y, 'w': 1440, 'h': size,
                      'fontSize': 26, 'rows': block['rows']}
            elements.append(el)
            coverage.append({'line': block['line'], 'slide': identity, 'element': eid})
            y += size + 20
        add_slide(identity, display_title, section, elements)
        if part == 1:
            coverage.append({'line': group['heading']['line'], 'slide': identity})
        chunk, height = [], 0

    for block in group['blocks']:
        if block['type'] == 'text':
            # A numbered list is split between complete items if necessary.
            texts = block['text'].split('\n') if re.match(r'\d+\.', block['text']) else [block['text']]
            for value in texts:
                b = {**block, 'text': value}
                h = text_height(value)
                if height + h > 555:
                    emit()
                assert h <= 555, (title, h)
                chunk.append((b, h))
                height += h + 20
        else:
            emit()
            header, pending = block['rows'][0], block['rows'][1:]
            while pending:
                count = min(5, len(pending))
                while True:
                    rows = [header, *pending[:count]]
                    cell_units = 1440 / len(header) / 26 - 2
                    row_height = max(math.ceil(units(translate_atom(c, lang)) / cell_units) * 32 + 26 for row in rows for c in row for lang in LANGUAGES)
                    h = max(210, row_height * len(rows))
                    if h <= 550 or count == 1:
                        break
                    count -= 1
                chunk = [({**block, 'rows': rows}, h)]
                emit()
                pending = pending[count:]
    emit()

def cards_slide(identity, title, section, cards, source_text):
    elements = []
    for n, (head, body) in enumerate(cards):
        elements.append({'id': f'{identity}-card-{n}', 'type': 'shape', 'shape': 'rect',
                         'x': 80 + (n % 2) * 740, 'y': 210 + (n // 2) * 255, 'w': 700, 'h': 240,
                         'fontSize': 28, 'color': '222222', 'fill': 'F4F4F4', 'align': 'left',
                         'text': head + '\n\n' + body})
    elements.append(text_element(identity + '-source', source_text, 715, 85, 26))
    return add_slide(identity, title, section, elements, 'comparison')

# Actual operation results supplement the existing analysis without rewriting it.
# Prior preparation-material images remain on disk, but are not shown in the body.
for asset in image_manifest:
    identity = 'operation-photo-' + asset['id'].lower()
    crop_w, crop_h = asset['crop'][2:]
    tall = crop_h / crop_w > .6
    width = min(940 if tall else 1440, (560 if tall else 350) * crop_w / crop_h)
    height = width * crop_h / crop_w
    image_el = {'id': identity + '-image', 'type': 'image',
                'src': str((OUT / asset['original']).resolve()),
                'alt': asset['caption'], 'altText': asset['caption'] + '。' + asset['limit'],
                'x': 80, 'y': 210, 'w': width, 'h': height, 'fit': 'contain'}
    caption = '**' + asset['caption'] + '**\n' + asset['source'] + '\n' + asset['observation'] + '\n' + asset['limit'] + ' 对应：' + asset['evidence'] + '。'
    elements = [image_el, text_element(identity + '-caption', caption,
                210 if tall else 590, 560 if tall else 210, 23,
                width=540 if tall else 1440, x=980 if tall else 80)]
    slide = add_slide(identity, asset['title'], asset.get('section', '三 典型场景分析'), elements)
    deck['slides'].remove(slide)
    at = next(i for i, s in enumerate(deck['slides']) if s['id'] == asset['anchor'])
    deck['slides'].insert(at + 1, slide)

# Derived visual summaries reference the same evidence; no synthetic metrics.
flow = cards_slide('roles', '信息如何在工具之间流转', '四 核心发现', [
    ('输入与资料', '群内在线文档、业务台账查询结果\n材料质量与口径仍需核对'),
    ('千问办公', '理解请求、组织内容、调用工具\n创建定时任务'),
    ('业务系统', '保存、查询业务记录\n返回部分规则计算结果'),
    ('钉钉', '承载在线文档、群消息与个人待办\n多人接单、执行与办结尚未验证')
], '依据 E20、E07–E09 归纳分工；各场景路径不同，不代表完整闭环已获验证。')
deck['slides'].remove(flow)
at = next(i for i, s in enumerate(deck['slides']) if s['section'].startswith('四'))
deck['slides'].insert(at + 1, flow)
patrol = cards_slide('patrol-records', '四次计划巡检的实际记录', '三 典型场景分析', [
    ('10月11日 · 执行错误', '日志：too_late\n不据此推定设备未在线'),
    ('10月12日 · 执行错误', '日志：sleep\n恢复与其他告警渠道待核'),
    ('10月13日 · 有完成记录', '群消息：09:11:57\n计划时间：09:00'),
    ('10月14日 · 有完成记录', '群消息：09:11:38\n计划时间：09:00')
], 'E15–E17；另有10月10日手动演示。仅描述这四次计划，不估计产品总体可靠率。')
deck['slides'].remove(patrol)
at = max(i for i, s in enumerate(deck['slides']) if s['section'].startswith('三'))
deck['slides'].insert(at + 1, patrol)

evidence_titles = ['演示范围', '技能包与准备', '组织访问控制', '合同提取', 'AI合同录入与本人更正', '风险数据与计算归属',
                   '跟踪登记与分发', '待办与提醒触达', '跨次读取差异', '根因解释与修复证据', '三路数据简报', '客户分析的解释边界',
                   '@格式校验', '确认请求与控制验收', '计划巡检运行记录', '计划与送达时点', '业务静默与运行健康', '发送异常与重试',
                   '技能移植依赖', '三类工具的分工', '效果基线缺失', '有限验证的优先级', '数字与业务口径', '银行使用条件']
evidence_rows = []
for line in matrix.read_text().splitlines():
    if re.match(r'^\| E\d{2} \|', line):
        evidence_rows.append([plain(c) for c in line.strip('|').split('|')])
assert len(evidence_rows) == 24
labels = ['关键发现', '证据来源', '事实或推论', '可信程度', '尚存疑问', '对报告的意义']
for index, row in enumerate(evidence_rows):
    identity = row[0].lower()
    elements, y = [], 210
    for n, (label, value) in enumerate(zip(labels, row[1:])):
        content = '**' + label + '：**' + value
        h = text_height(content, 27)
        elements.append(text_element(f'{identity}-{n}', content, y, h, 27))
        y += h + 10
    assert y < 802, (identity, y)
    add_slide(identity, row[0] + ' · ' + evidence_titles[index], '证据详情 E01–E24', elements)

source_deck = copy.deepcopy(deck)
projections = {lang: translate_model(source_deck, lang) for lang in LANGUAGES}
deck = projections['en']
deck['i18n'] = {'version': 1, 'defaultLanguage': 'en', 'language': 'en',
                'translations': {lang: localization.fields(projections[lang]) for lang in LANGUAGES}, 'stale': {}}
deck = build.normalize(deck, SKILL / 'assets/themes')
html_text = build.render_html(deck, view='report')
extra_css = (HERE / 'report.css').read_text()
# Display the published PNG excerpts at their full extent in Report and Slides.
# Full-window JPEG originals are local-only and are never embedded.
for asset in image_manifest:
    x, y, cw, ch = asset['crop']
    iw, ih = asset['pixels']
    selector = '[data-element-id="operation-photo-' + asset['id'].lower() + '-image"]'
    extra_css += f'\n{selector}{{overflow:hidden;aspect-ratio:{cw}/{ch}!important}}'
    extra_css += f'\n{selector}>img{{position:absolute!important;max-width:none!important;width:{iw/cw*100}%!important;height:auto!important;left:{-x/cw*100}%!important;top:{-y/ch*100}%!important;object-fit:fill!important}}'

extra_js = (HERE / 'report.js').read_text()
# The skill app initializes synchronously. Install the report wrapper before it.
app_src = (SKILL / 'assets/app.js').read_text()
assert html_text.count(app_src) == 1
save_return = "    return '<!doctype html>\\n'+copy.outerHTML;"
assert app_src.count(save_return) == 1
# Serialized transient style attributes are unnecessary: the model recreates them.
# Removing them avoids CSP warnings on reopen without weakening the policy.
patched_app = app_src.replace(save_return, "    copy.querySelectorAll('[style]').forEach(node=>node.removeAttribute('style'));\n" + save_return)
html_text = html_text.replace(app_src, extra_js + '\n;\n' + patched_app)
html_text = html_text.replace('</style>', '\n' + extra_css + '\n</style>', 1)

# Keep JSON fields on separate lines for review and precise secret-scan exceptions.
# Parsed values are unchanged, including the embedded image bytes.
def readable_json(match):
    obj = json.loads(match[2])
    value = json.dumps(obj, ensure_ascii=False, indent=2).replace('<', '\\u003c').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
    assert json.loads(value) == obj
    return match[1] + '\n' + value + '\n' + match[3]
html_text = re.sub(r'(<script\b[^>]*type="application/json"[^>]*>)(.*?)(</script>)', readable_json, html_text, flags=re.S)

# Refresh strict CSP hashes after adding the local reading/print enhancement.
def csp_hash(text):
    return "'sha256-" + base64.b64encode(hashlib.sha256(text.encode()).digest()).decode() + "'"
scripts = re.findall(r'<script\b([^>]*)>(.*?)</script>', html_text, re.S)
js_hashes = [csp_hash(text) for attrs, text in scripts if 'application/json' not in attrs]
css_hashes = [csp_hash(text) for text in re.findall(r'<style\b[^>]*>(.*?)</style>', html_text, re.S)]
csp = "default-src 'none'; script-src " + ' '.join(js_hashes) + '; style-src ' + ' '.join(css_hashes) + "; img-src data: blob:; font-src 'none'; connect-src 'none'; media-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; frame-src 'none'; worker-src 'none'"
html_text = re.sub(r'(<meta http-equiv="Content-Security-Policy" content=")[^"]*(">)', lambda m: m[1] + csp + m[2], html_text)

# Content completeness covers visible text and table cells, never hidden notes.
visible = '\n'.join([source_deck['title'], *[s['title'] + '\n' + s['section'] + '\n' + '\n'.join(el.get('text', '\n'.join(' | '.join(r) for r in el.get('rows', []))) for el in s['elements']) for s in source_deck['slides']]])
canonical = lambda v: re.sub(r'\s+', '', plain(v))
missing = []
for b in blocks:
    candidates = [c for row in b['rows'] for c in row] if b['type'] == 'table' else b['text'].split('\n')
    for value in candidates:
        if canonical(value) not in canonical(visible):
            missing.append({'line': b['line'], 'text': value})
for row in evidence_rows:
    for value in row:
        if canonical(value) not in canonical(visible):
            missing.append({'evidence': row[0], 'text': value})
assert not missing, missing
assert not re.search(r'/Users/[^/]+/', html_text)
refs = re.findall(r'(?:src|href)="([^"]+)"', html_text)
assert not [r for r in refs if re.match(r'https?://|file:|/Users/', r)]

(HERE / 'deck.json').write_text(json.dumps(deck, ensure_ascii=False, indent=2) + '\n')
(OUT / '04_final_report.html').write_text(html_text)
record = {'report_source': source.name, 'report_sha256': digest(source), 'matrix_source': matrix.name,
          'matrix_sha256': digest(matrix), 'theme': 'hk-technology', 'default_view': 'report',
          'language': 'en', 'languages': list(LANGUAGES), 'translation_fields_per_language': len(localization.fields(deck)),
          'locales_sha256': digest(HERE/'report_locales.json'), 'slides': len(deck['slides']), 'evidence_items': 24,
          'source_blocks': len(blocks), 'missing_content': missing, 'mapping': coverage,
          'published_images': [{key:a[key] for key in ('id','sha256','original','source_sha256','source_crop','capture_date')} for a in image_manifest],
          'skill_version': '1.3.0', 'html_sha256': digest(OUT / '04_final_report.html')}
(HERE / 'content_map.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in record.items() if k != 'mapping'}, ensure_ascii=False, indent=2))
