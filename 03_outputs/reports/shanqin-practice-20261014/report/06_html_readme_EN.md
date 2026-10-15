# HTML Report Guide

**English** · [简体中文原文](06_html_readme.md)

Main file: [04_final_report.html](04_final_report.html). It retains the **HK Technology** theme and opens in **English**, in **Report** view. The toolbar's **Language** selector switches between English, Simplified Chinese and Traditional Chinese. Body text, captions, tables, notes, contents and evidence descriptions switch together; text inside original screenshots is unchanged. Images, content, evidence, styles and scripts are embedded for standalone sharing and offline reading. Download the raw file from GitHub and open it in a browser.

## Current version

Content and 24 evidence items come from the latest U3-corrected [formal report](04_final_report_EN.md) and [evidence matrix](02_evidence_matrix_EN.md). All six real screenshots and captions are included in the formal Markdown. Historical assessments in the evidence matrix are unchanged.

- After the background: business dashboard overview.
- After contract entry: ledger screenshot of HT-2026-0007.
- After risk aggregation: project ledger and an excerpt of DingTalk's retained 10 October briefing.
- After instruction registration/notification: the pending-decision and corrective-action to-dos, plus the currently empty risk-tracking list.

All six were captured on 15 October 2026. UI-01–UI-03 use the existing PNG pixel excerpts; the three additional images use JPEG screenshot bytes returned directly by the browser. Full DingTalk windows remain local and are not embedded. Sources, original/excerpt fingerprints and limits: [screenshot guide](07_operational_screenshot_evidence_EN.md), [image manifest](html_src/operational_image_manifest.json).

## Reading and printing

Click E01–E24 to inspect evidence, then “Back to reference” to return. Report and Slides views share the same content model. After browser editing, use Save HTML; Markdown is not updated automatically.

Print / PDF uses A4 portrait styles, expands evidence and hides controls. Images keep their proportions and are laid out with captions. Browser headers/footers can be disabled. Earlier PDF/Word files lack this version's six operational images and remain local under `.local-only/prior-exports/`, excluded from the public archive.

## Verification scope

The [archive checks](qa/archive_checks.json) bind to this HTML's fingerprint: 69 body-content blocks, 24 evidence items, six image positions and embedded contents, PNG/JPEG dimensions, script syntax, CSP hashes and archive links. No external resource dependencies were introduced.

Thirty combinations were checked: three languages × two views × five viewport sizes. Language controls were visible; all six screenshots loaded; no text or page-width overflow was detected. English evidence navigation and return were checked. A test copy used native save serialization with local byte capture instead of download transport; reopening retained the Traditional Chinese selection and edits, and switching to English and back worked. This does not verify actual browser download delivery. See [browser checks](qa/browser_checks.json). Rendering in PowerPoint, full editor regression and PDF pagination remain unverified; old print checks do not establish a pass for this version.

## Build and maintenance

Image-manifest captions must match the Markdown `screenshot:UI-xx` blocks. The builder checks both to prevent missing images or diverging descriptions.

`html_src/build_report.py` derives a unified trilingual model from the Markdown, evidence matrix, image manifest and [report_locales.json](html_src/report_locales.json), calling corporate-web-slides 1.3.0. Translations are keyed by source fragments; missing translations stop the build. Source changes require corresponding translation updates and review. Languages share screenshots, links and geometry; pagination allows space for all three, producing 74 slides while Report view retains the document hierarchy. `report.css` and `report.js` are task-local adaptations. The shared skill is neither modified nor bundled here. [Dependency fingerprints](html_src/build_dependencies.json) record the skill files used.

Reading needs no installation. Rebuilding requires Python 3 and corporate-web-slides 1.3.0. That internal skill is distributed separately, so the repository is not a self-contained build environment. Node.js is used for script syntax checks. From this archive directory:

```sh
export CORPORATE_WEB_SLIDES_SKILL="/path/to/corporate-web-slides"
python3 report/html_src/build_report.py
python3 report/qa/verify_archive.py
```

Without the environment variable, the builder uses `~/.codex/skills/corporate-web-slides`. `content_map.json` records body/evidence/image mappings and translation fingerprints. Generated `deck.json` duplicates image data and is ignored. See the [project README](../README.md) for public entries and scope.

The full report includes [English PPTX](04_final_report_EN.pptx), [Simplified Chinese PPTX](04_final_report_SC.pptx), [Traditional Chinese PPTX](04_final_report_TC.pptx) and an [English POTX](04_final_report_EN.potx). The [native export verifier](qa/verify_report_exports.py) checked trilingual content, tables, notes across 74 slides and all six original images. An OOXML simulation checked new-slide content-layout inheritance; this is not a PowerPoint application check. Reading mode has a simplified toolbar; Export PPTX / POTX is available in Edit mode. After changing HTML, export again, then run `python3 report/qa/verify_report_exports.py` and the archive check. Old exports cannot stand in for new results.

## Trilingual management brief

[08_management_brief.html](08_management_brief.html) uses **native corporate-web-slides 1.3.0 Report mode** and is maintained separately. It organizes the business-value analysis into 17 reading sections/slides, retaining five real screenshots, evidence boundaries and lessons for technology teams. Practitioner: **Leo Zhang**.

English is the default. Language switches the body, captions, notes and editor between English and both Chinese variants. Original screenshot text remains unchanged. View switches Report / Slides. Edit changes the selected language; Save HTML preserves the complete editable file. Watch for stale-translation indicators after changing a language. Export PPTX / Export POTX exports the current language and latest edited model as presentation layouts, not screenshots of the scrolling Report page.

The delivered [English PPTX](08_management_brief_EN.pptx), [Simplified Chinese PPTX](08_management_brief_SC.pptx), [Traditional Chinese PPTX](08_management_brief_TC.pptx) and [English POTX](08_management_brief_EN.potx) contain native text, flow shapes, separate screenshots, 17 sets of speaker notes and a shared content master. Branding/theme definitions remain in the model for maintenance.

The sole content source is [management_brief_model.json](html_src/management_brief_model.json). [build_management_brief.py](html_src/build_management_brief.py) calls the skill's native Report renderer, with no second report DOM or translation source. Build dependencies and the environment variable above also apply. Saved browser-edited HTML contains its own latest model; it does not update the repository JSON.

Checks covered three languages, Report/Slides and five viewports: 30 combinations with no detected text or page-width overflow. All five screenshots loaded and matched source bytes. Title/body/notes editing, stale-translation indicators, duplicate/delete/undo/redo were checked. A serialized test copy reopened with edits; actual browser download delivery was not confirmed.

Office files were generated locally using the unmodified skill exporter. The [verifier](qa/verify_management_brief.py) checked translations/notes, original image bytes, package relationships, native objects and new-slide layout inheritance. PowerPoint rendering, `file://` opening, PDF pagination and the complete drag/crop editing combinations remain unverified. Results bind to the current HTML fingerprint in the [brief checks](qa/management_brief_checks.json).

## Commit-check note

The same HK Technology PNG logo is embedded once in the HTML configuration and once in the content model. Its Base64 happens to match the local ECC AWS-key pattern. The root `.ecc-allowlist` matches only this image's complete, exact `contentLogo` data line, not other fields or an entire file. Static checks also verify the match count and decoded PNG fingerprint. Global Git hooks were not disabled or rewritten.

## English Markdown editions

The [project README](../README.md) links the English Markdown translations and their Chinese originals. `html_src/build_english_report.py` regenerates the full English report from the corrected Markdown and reviewed HTML translations without rebuilding HTML. Other English documents are maintained as translations with source fingerprints in `html_src/markdown_translations.json`. After changing a source, review its English edition and refresh the fingerprint only after reconciliation.
