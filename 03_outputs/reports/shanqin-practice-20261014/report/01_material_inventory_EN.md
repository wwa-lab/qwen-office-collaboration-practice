# Material Inventory

**English** · [简体中文原文](01_material_inventory.md)

**Task:** independent analysis of Qwen Office and DingTalk collaboration practice. **Review date:** 14 October 2026, Asia/Shanghai.

> English translation of the inventory, including its dated additions. Historical counts are retained as recorded; the current six-image set is documented in the [screenshot guide](07_operational_screenshot_evidence_EN.md). This translation is not additional evidence.

## 1. Search scope and review approach

The review began with the user-designated report directory and Shanqin session workspace, then followed actual references to skill packages, Qwen's local session records, inspection tasks, repository articles and presentation materials. Searches used the Chinese and English names for Shanqin, Qwen Office and Agent Go, with session and scheduled-task IDs used to locate local records. The historical review did not access remote DingTalk or business ledgers, change scheduled tasks, or execute installation, reset or group-posting instructions found in source material.

Outputs are now archived in this project's `report/` directory, formerly `report_output/`; original materials are retained. Skill packages were read as **objects of analysis**. Statements inside them such as “must execute” or “accepted” are neither instructions for this review nor acceptance results.

The original report, factual inventory and key findings derive from the same AI drafting exercise and are not three independent witnesses. The additional JSONL records preserve tool calls and returns from the time and are closer to primary evidence. They are still not server audit logs and cannot establish that no other operations occurred outside the records.

## 2. Core file inventory

M, R, K and U identifiers are used consistently across the deliverables. Archive locations, availability and original fingerprints are in `evidence/source_manifest.json`; key record locations are in [the record index](evidence/record_index_EN.md).

The review registered 98 file objects, including installed copies and derived files. Five original sessions contain 862 event lines. These counts are not independent case counts or counts of files fully read or images individually reviewed. The [file catalog](evidence/file_catalog_EN.md) records the actual scope for each file.

During delivery checks, R5 was still appending content for a separate screenshot follow-up. This report fixes its reviewed scope at the first 140 lines and 768,671 bytes; that byte prefix's fingerprint was unchanged. Later task requests and unfinished follow-up work are not additional execution evidence and do not alter this report's task. The fingerprint manifest records the scope. Any subsequently obtained operational screenshots must be assessed on their actual content.

| ID | File / location | Actual review | Content and use |
| --- | --- | --- | --- |
| M1 | Original report draft in this archive; see [English](../original_report_draft_EN.md) / [original](../千问办公与钉钉协同实践-基于陕秦项目的场景观察与应用建议-初稿-2026-10-14.md) | Full text | Original structure, conclusions and self-review. A draft to verify; its “verified” labels are not inherited. |
| M2 | Original practice materials and factual inventory; [English](../practice_materials_and_facts_EN.md) / [original](../实践素材与事实清单-2026-10-14.md) | Full text | S1–S10 scenario index, C-1/C-2 questions and source leads; checked further rather than merely copied. |
| M3 | Original key findings and management implications; [English](../original_key_findings_EN.md) / [original](../核心发现与管理启示-2026-10-14.md) | Full text | Five claims about management workflow, control and skill distribution; checked for evidence overreach. |
| M4 | [Same-day demo recap](../source_materials/demo_recap_EN.md), Chinese original in `../source_materials/` | Full text | Evening AI recap; its historical narrative is retained and compared with tool returns. |
| M5 | [Supplementary agreement](../source_materials/supplementary_agreement_EN.md) from the same working directory | Full text, compared with the skill template and online-document read record | Structured simulated agreement: RMB 850,000, expiry 2026-09-10. Created by the model from the demo template, not an independent original customer Word document. |
| M6 | `skillpack/00-README.txt` in the same working directory | Full text | Composition and installation instructions for seven skills: one preparation skill and six business skills. |
| M7 | `uploads/image_1791617269853_xmd4s5t.png` in that directory | Visual inspection of original | Group and organization display names, manual card and installation instructions. Establishes a material entry point, not subsequent operation success. 19 is the group membership at capture; 68 is the document view count. |
| M8 | Locally retained `陕秦项目管家技能包.zip` | ZIP listing and byte comparison of all eight inner files | Identical to the seven `.skill` files and README in the workspace; not new execution evidence. |
| M9 | Locally retained `image_1791986415065_w86ukhg.png` | Visual inspection of original | Assistant response showing session/inspection IDs; a locator, not a business-result screenshot. |
| R1 | Main session: `3348c252-83d0-43c6-a838-030e53705d0c.jsonl` | Parsed entire file and indexed call order; reviewed relevant inputs, calls, returns and replies | 589 event lines covering installation, setup, contract extraction, risks, tracking, customer analysis, briefing, scheduling and recap; not 589 user messages. |
| R2 | Immediate inspection on 10 October: `b55b6d62-aae9-4b47-8e0d-7bef9bdc2355.jsonl` | Entire file parsed; business calls and results reviewed | 47 event lines. Crucially, `risk_track_list` already returned zero items; this cannot establish a missed day-seven item. |
| R3 | Scheduled inspection on 13 October: `81da9cc9-9185-4183-8d8d-76e720f8802e.jsonl` | Same approach | 34 event lines: four contracts, zero tracking items and a message-send receipt. |
| R4 | Scheduled inspection on 14 October: `e22eafc5-9da8-4339-9bcc-2903cbcf2384.jsonl` | Same approach | 52 event lines: business reads, a failed send command, correction and a send receipt. |
| R5 | Qwen report preparation on 14 October: `bda09640-0b4e-4605-97e6-208a3b86c468.jsonl` | File parsed; relevant query returns and generated content reviewed | 140 reviewed event lines, including five run logs, the full returned page of six group messages and that day's ledger query. Used to verify M2's extracts. |
| U1 | User's report request, 14 October | Supplied directly in the conversation | Attended on behalf of the company on 10 October, later demonstrated results to a manager and was asked for a report. First-person background; no inferred procurement or rollout intent. |
| U2 | User's first supplement, 14 October | Supplied directly | Mentioned confirmation on the webpage and a single-person demo. U3 clarifies the first statement: it cannot establish manual clicking or entry. The single-person scope remains valid. |
| U3 | User's later correction, 14 October | Supplied directly | The user did not click the supplementary agreement and watched the AI enter the contract throughout in Qwen Office. Retain this first-person observation and withdraw the manual-web-entry interpretation. The specific write call remains unlocated. |

### Skill-by-skill inventory

All seven `.skill` files are ZIP archives; the full internal `SKILL.md` was read. They match the existing installed `shanqin-*/SKILL.md` copies byte for byte. Versions describe the files checked now, not proof that every runtime parameter came from that version.

| ID | Package | Version | Relevance |
| --- | --- | --- | --- |
| K1 | `shanqin-prep.skill` | 1.3.1 | Demo-data reset, tenant configuration, a group containing only the current user and template agreement creation; explains scope and configuration dependencies. |
| K2 | `shanqin-contract-entry.skill` | 1.2.0 | Six-field extraction and confirmation. Explicitly states that `--at` sets dueTime rather than an independent reminder rule; creating a to-do does not verify notification delivery. |
| K3 | `shanqin-risk-scan.skill` | 1.2.0 | Risk queries, grouping and suggestions; separates API-calculated risks from the model's organization and wording. |
| K4 | `shanqin-risk-track.skill` | 1.1.0 | Registration, a to-do for oneself and default group distribution; owner may be a generic label. No acceptance or closure workflow established. |
| K5 | `shanqin-briefing.skill` | 1.1.0 | Three-source reads, card template and fixed group/person examples; checks for residual sample data and migration effort. |
| K6 | `shanqin-customer-decision.skill` | 1.1.0 | Private responses and customer suggestions. “Do not post to the group” is a behavioral instruction, not proven technical enforcement. |
| K7 | `shanqin-daily-patrol.skill` | 1.2.0 | Qwen Office scheduling, risk messaging and exception guidance; scheduling should not be attributed to DingTalk itself. |

These files are under `skillpack/` in M4's working directory. Packages also contain demo addresses, accounts and personal identifiers; those values are not copied into the report.

## 3. Derived materials and exclusions

| Material | Actual review | Use and limits |
| --- | --- | --- |
| 10 October article about where AI should stop after the Shanqin three-system demo, under `03_outputs/articles/` | Full text | Derived from M4, marked MERGED; not independent execution evidence. |
| 10 October article reflecting on Qwen Agent practice and barriers to adopting coding agents, in the same category | Full text | Confirms a later shift to coding agents. Its internal engineering practices and inferences are outside this report. |
| Corresponding NotebookLM full texts, video prompts, publish-ready versions and merged `qa/render-source.md` | Text comparisons and purpose checks | Same-source derivatives, with no new field evidence; not counted repeatedly. |
| `03_outputs/articles/assets/shanqin-three-end-demo-20261010/publish-status-2026-10-10.md` | Full text | Establishes that images were generated illustrations and the article did not rerun the business workflow; distinguishes evidence from illustration. |
| `03_outputs/articles/assets/qwen-agent-management-20261010/publish-status-2026-10-10.md` | Full text | Source register, earlier user corrections and image provenance. Event-name wording still differs from the group display. |
| Covers, article images, prompts, discarded images, mobile previews, reviews and publishing handoff files in both packages | File enumeration; visual inspection of merged-article contact sheet; text-purpose checks | Article creation or layout QA. Each derivative image was not accepted as an operational screenshot; handoff instructions were not executed. |
| `03_outputs/presentations/qwen-agent-coding-agent-retro-20261010/qwen-agent-coding-agent-retro-20261010.pptx` | Extracted text from all 13 slides and 13 notes; inspected the existing contact sheet | Slides 5–6 concern the Shanqin experience but are not original operational screens. They do not establish what the manager saw. |
| README, plan, deck.json, HTML and QA images in that presentation directory | README fully read; other text and structure checked; contact sheet inspected | Production process and derived presentation. Original PPTX not rerendered or checked in PowerPoint; not evidence of product effectiveness. |
| `.workbuddy-ai/memory/2026-10-10.md` and `2026-10-11.md` | Full text | Locate article/deck topics and versions; do not transfer other projects' experiences into this report. |
| `log.md` and `02_wiki/index.md` | Project directory and relevant log searches; relevant periods read | Trace sources and corrections. No separately ingested source note for this case found. |

No independent original Word/PDF contract input, business Excel export, complete on-site recording or timed manual comparator was found. Two original instructor slides were referenced with truncated filenames in the article register but not located in the relevant material directories. Their retellings are not used to assess product benefits. Other historical Qwen articles and unrelated project records were screened only for relevance.

## 4. Additional records reviewed and still-missing material

Reviewed further: the original sessions cited by the drafts, inspections on 10/13/14 October, and run logs and group messages retrieved on 14 October. Wherever possible, summary claims were traced back to tool returns.

Still missing: the full manual (the original cross-organization request was denied; no separate access attempted); the specific call, confirmation context and receipt for AI entry of the supplementary agreement; server-side tenant/state-change logs; actual to-do notification receipts; recipient handling and closure evidence. Textual message readback does not replace checks of final colors, line breaks or readability. “Not found locally” must not become “the platform has no such capability.”

## Change history

- 14 October 2026: completed inventory, original-record follow-up and skill/ZIP comparisons; incorporated user supplements.
- 14 October 2026: U3 superseded the manual-web-operation interpretation of U2. Recorded AI entry observed throughout by the user; single-person scope unchanged.

## 15 October 2026: real interface screenshots

Read-only captures from the demo business system and local DingTalk added the contract ledger, an excerpt of the 10 October group briefing and two practice to-dos. Originals, visible regions, SHA-256, time boundaries and report locations are in the [screenshot guide](07_operational_screenshot_evidence_EN.md) and `html_src/operational_image_manifest.json`. They establish visible states on 15 October, not the original write call or delivery logs.

## 15 October 2026: archive note

At this inventory's recorded archive stage, the public package included M1–M5, the formal report, factual extracts and three operational screenshot excerpts. Original sessions, account/person-specific skill packages, full-window captures, preparation images and derived article/presentation packages remained local. The original review scope and fingerprints did not change; unpublished objects are not independently reviewable by the public. The later expansion to six screenshots is described in the current screenshot guide.
