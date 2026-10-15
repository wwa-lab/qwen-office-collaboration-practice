# Shanqin Collaboration Practice

**English** · [简体中文](README.zh-Hans.md) · [繁體中文](README.zh-Hant.md)

Reports, evidence and essential materials from the Qwen Office and DingTalk collaboration demonstration. Practice date: 10 October 2026. Report date: 14 October 2026. Additional real interface captures: 15 October 2026. Practitioner: **Leo Zhang**.

**Start with the [full English report](report/04_final_report_EN.md) or the [offline HTML report](report/04_final_report.html).** The HTML uses the HK Technology theme and opens in English in continuous Report view. The Language selector switches to Simplified or Traditional Chinese. Images, styles and scripts are embedded, and browser printing is supported. GitHub displays HTML source; download the raw file and open it in a browser.

This is personal practice analysis for management discussion, using synthetic business data. It is not an official institutional assessment, deployment decision or product endorsement. HK Technology is the visual theme selected for this material.

## Reading guide

English Markdown editions are linked first. Chinese originals remain unchanged for source comparison. The two HTML reports support English, Simplified Chinese and Traditional Chinese.

| Document | English / Chinese original | Purpose |
| --- | --- | --- |
| Full report | [English](report/04_final_report_EN.md) / [简体中文](report/04_final_report.md) | Corrected management assessment and scenario analysis, with all six real screenshots. |
| Material inventory | [English](report/01_material_inventory_EN.md) / [简体中文](report/01_material_inventory.md) | Actual review scope, source categories and materials not obtained. |
| Evidence matrix | [English](report/02_evidence_matrix_EN.md) / [简体中文](report/02_evidence_matrix.md) | E01–E24: separates facts, observations, analysis and hypotheses. |
| Independent management analysis | [English](report/03_management_analysis_EN.md) / [简体中文](report/03_management_analysis.md) | Workflow changes, incremental value and evaluation methods. |
| Open questions | [English](report/05_open_questions_EN.md) / [简体中文](report/05_open_questions.md) | Missing evidence and matters requiring human judgment. |
| HTML use and maintenance | [English](report/06_html_readme_EN.md) / [简体中文](report/06_html_readme.md) | Offline reading, printing, build dependencies and verification boundaries. |
| Screenshot guide | [English](report/07_operational_screenshot_evidence_EN.md) / [简体中文](report/07_operational_screenshot_evidence.md) | Sources, capture dates, cropping and evidential limits. |
| Record index | [English](report/evidence/record_index_EN.md) / [简体中文](report/evidence/record_index.md) | Locations in historical sessions and available factual extracts. |
| File catalog | [English](report/evidence/file_catalog_EN.md) / [简体中文](report/evidence/file_catalog.md) | The 98 file objects originally reviewed and their public availability; not 98 independent pieces of evidence. |
| Essential source materials | [English guide](source_materials/README.md) / [简体中文说明](source_materials/README.zh-Hans.md) | English translations and unchanged originals of the same-day recap and simulated agreement. |

| Presentation / evidence | Purpose |
| --- | --- |
| [Management brief HTML](report/08_management_brief.html) | Native corporate-web-slides Report: three-system workflow, business value to test, candidate uses for technology teams and next steps. English by default; both Chinese variants, Slides and browser editing supported. Five real screenshots; practitioner Leo Zhang. |
| [Brief: English PPTX](report/08_management_brief_EN.pptx) / [简体 PPTX](report/08_management_brief_SC.pptx) / [繁體 PPTX](report/08_management_brief_TC.pptx) / [English POTX](report/08_management_brief_EN.potx) | 17 editable slides with speaker notes. Structure, images and master inheritance checked; rendering in PowerPoint unverified. |
| [Full report HTML](report/04_final_report.html) | Complete trilingual report, six screenshots and E01–E24. |
| [Full report: English PPTX](report/04_final_report_EN.pptx) / [简体 PPTX](report/04_final_report_SC.pptx) / [繁體 PPTX](report/04_final_report_TC.pptx) / [English POTX](report/04_final_report_EN.potx) | 74 slides with native text, tables, separate images and speaker notes. Rendering in PowerPoint unverified. |
| [Factual extracts](report/evidence/selected_factual_extracts.json) / [Source fingerprints](report/evidence/source_manifest.json) | Essential returned business fields and original file fingerprints. |
| [Archive checks](report/qa/archive_checks.json) | Current HTML fingerprint, content coverage, image, link and script checks. |

## Versions and factual boundaries

The current analysis is defined by `report/04_final_report.md` and `report/02_evidence_matrix.md`. The English full report uses the same reviewed translations as the HTML. English editions are translations, not additional independent evidence.

Correction U3 remains unchanged: Leo observed the AI complete contract entry throughout in Qwen Office and did not click the supplementary agreement. The reviewed logs still lack the specific write call and confirmation context. A single-person demonstration does not establish a completed multi-person workflow; successful tool calls do not establish efficiency gains or sustained reliability.

The three original Qwen drafts are retained as **historical drafts requiring verification**. Their English editions preserve their historical claims, which must be read alongside the corrected report. Strong claims of a complete workflow, a fixed boundary issue or a verified confirmation gate have been qualified or corrected in the formal report.

| Historical draft | English translation | Chinese original |
| --- | --- | --- |
| Original report draft | [English](original_report_draft_EN.md) | [简体中文](千问办公与钉钉协同实践-基于陕秦项目的场景观察与应用建议-初稿-2026-10-14.md) |
| Practice materials and factual inventory | [English](practice_materials_and_facts_EN.md) | [简体中文](实践素材与事实清单-2026-10-14.md) |
| Key findings and management implications | [English](original_key_findings_EN.md) | [简体中文](核心发现与管理启示-2026-10-14.md) |

The old PDF and Word exports predate the six operational screenshots and are retained only in `report/.local-only/prior-exports/`. Earlier browser and print checks apply only to their earlier versions. The current full report has been checked in three languages, two views and five viewport sizes. A test copy passed editing, serialization and reopening checks; native export content and screenshots were also checked. Actual browser download delivery, rendering in PowerPoint and printed pagination remain unverified.

## Archive scope

```text
shanqin-practice-20261014/
├── README.md / README.zh-Hans.md / README.zh-Hant.md
├── .gitignore / publication_files.json
├── Three original Qwen drafts and their English translations
├── source_materials/             # M4 recap; M5 simulated agreement; translations
└── report/
    ├── 01…08 documents, full report and management brief
    ├── *_EN.md                  # English editions of the Markdown documents
    ├── assets/published/        # 6 real interface screenshots and excerpts
    ├── evidence/                # Source fingerprints, index and factual extracts
    ├── html_src/                # Task-local builders and content mappings
    └── qa/                     # Verification scripts and receipts
```

`publication_files.json` lists the public files. Raw JSONL records, skill packages containing demo accounts and personal identifiers, full-window captures, preparation screenshots, font copies, duplicate previews and old exports are excluded. Full originals remain local. Published PNGs retain the rectangular excerpts needed for the report; the additional JPEGs show the business webpage region or full business page. The HTML embeds only published images. Screenshots retain scenario-relevant display names and demo data and are not claimed to be fully anonymized.

Original file hashes and historical record line numbers are retained. Unpublished sources are marked as locally retained; those references alone do not let public readers independently reproduce the whole review. The published factual extracts are not server audit logs.

Related WeChat articles and sharing presentations remain in the personal knowledge base under `03_outputs/articles/` and `03_outputs/presentations/`. They are derived materials and have not been copied here as additional evidence. The former local `report_output/` directory moved to this archive's `report/`; interpret old paths in historical logs accordingly.

## Maintenance

Update the Markdown, evidence and image source manifest first, then generate the HTML using the [build instructions](report/06_html_readme_EN.md). Preserve historical originals. Record the capture date, source and scope of new evidence. Update `publication_files.json` when the public file set changes.

Maintain all three README editions together. Review English translations when their Chinese sources change. Translation source fingerprints are recorded in `report/html_src/markdown_translations.json`. The English full-report builder reuses `report/html_src/report_locales.json` and stops if a translation is missing; it requires only Python 3 and does not rebuild the HTML. Run from this archive directory:

```sh
python3 report/html_src/build_english_report.py
python3 report/qa/verify_archive.py
```

The management brief is a derived reading entry point, not additional independent evidence. Its single content source is `report/html_src/management_brief_model.json`; the three languages share layout and screenshots. `build_management_brief.py` calls the native corporate-web-slides 1.3.0 Report builder without modifying the shared skill or browser runtime. Reading needs no dependencies; rebuilding requires Python 3, Node.js and the installed skill:

```sh
python3 report/html_src/build_management_brief.py
python3 report/qa/verify_management_brief.py
python3 report/qa/verify_archive.py
```

After changing the model, rebuild the HTML, export each language using Export PPTX / Export POTX in the webpage, then run the verification scripts. The Office verifier checks existing files; it does not generate them. Rebuilding resets browser and Office verification records, so old passing results cannot be reused automatically. See [HTML use and maintenance](report/06_html_readme_EN.md) and the [management brief checks](report/qa/management_brief_checks.json).

The archive verification command performs static checks only, without accessing the business system or DingTalk. It requires Python 3 and Node.js. Public repository: [wwa-lab/qwen-office-collaboration-practice](https://github.com/wwa-lab/qwen-office-collaboration-practice).
