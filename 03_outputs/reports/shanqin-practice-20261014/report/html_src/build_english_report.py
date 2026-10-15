#!/usr/bin/env python3
"""Build English Markdown from the corrected report and reviewed HTML translations."""
import argparse
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
OUT = HERE.parent


def render():
    catalog = json.loads((HERE / 'report_locales.json').read_text())['translations']['en']

    def translate(value):
        if value not in catalog:
            raise ValueError(f'Missing English translation: {value!r}')
        return catalog[value]

    def paragraph(value):
        segments = []
        for i, part in enumerate(value.replace('`', '').split('**')):
            translated = ''.join(translate(token) for token in re.split(r'(E\d{2}|U[123])', part) if token)
            segments.append('**' + translated + '**' if i % 2 else translated)
        result = ''.join(segments)
        for literal in re.findall(r'`([^`]+)`', value):
            result = result.replace(literal, '`' + literal + '`', 1)
        return result

    lines = []
    for original in (OUT / '04_final_report.md').read_text().splitlines():
        line = original.strip()
        if not line or line.startswith('<!-- screenshot:'):
            translated = line
        elif match := re.fullmatch(r'!\[([^]]+)\]\(([^)]+)\)', line):
            translated = f'![{translate(match[1])}]({match[2]})'
        elif match := re.match(r'^(#+) (.*)$', line):
            translated = match[1] + ' ' + translate(match[2])
        elif line.startswith('|'):
            cells = [cell.strip() for cell in line.strip('|').split('|')]
            translated = '| ' + ' | '.join(cell if re.fullmatch(r'[:\-]+', cell) else translate(cell.replace('**', '').replace('`', '')) for cell in cells) + ' |'
        else:
            translated = paragraph(line)
        lines.append(translated + ('\\' if original.endswith('  ') else ''))

    lines[2:2] = [
        '**English** · [简体中文原文](04_final_report.md) · [English / 简体中文 / 繁體中文 HTML](04_final_report.html)',
        '',
        '> English edition of the corrected report. Original evidence identifiers and all six screenshots are retained. This translation is not additional independent evidence.',
        '',
    ]
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check the existing edition without writing it.')
    args = parser.parse_args()
    target = OUT / '04_final_report_EN.md'
    expected = render()
    if args.check:
        if not target.is_file() or target.read_text() != expected:
            raise SystemExit('English full report is missing or stale; rebuild and review it.')
        print('English full report matches the source and reviewed translations.')
    else:
        target.write_text(expected, encoding='utf-8')
        print('Wrote ' + target.name)


if __name__ == '__main__':
    main()
