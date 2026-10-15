# Practice Materials and Factual Inventory — Historical Draft

**English** · [简体中文原文](实践素材与事实清单-2026-10-14.md)

> **Historical working draft M2, not the current assessment.** This translation preserves the draft's S1–S10 and C-1–C-3 statements, including claims later corrected. U3 establishes that Leo Zhang observed AI contract entry throughout and did not click the agreement. Consult the [current evidence matrix](report/02_evidence_matrix_EN.md) and [formal report](report/04_final_report_EN.md) for accepted boundaries.

Original purpose: working paper supporting the first report draft.\
Prepared: 14 October 2026, Asia/Shanghai.\
Compiler: AI assistant, comparing session records, local files, DingTalk messages, business-ledger queries and scheduled-task logs.

## 0. Definitions used in the draft

- **Main practice session:** `mv22nwqf5tdz5b7u`, titled “Go to this DingTalk group and look at this document,” 10 October 2026, 15:27–20:39; 26 messages; completed.
- **Environment:** a **simulated business environment** supplied by the event organizer: shanqin-mcp demo ledgers, tenant demo30. All contracts, projects and customers are demo data, **not real customer or business data**. All business figures are limited to that environment.
- **Original working method:** an inferred generic manual comparator, not a measured baseline or efficiency comparison.
- **Original validation labels:** A = executed with direct evidence; B = executed but with conflicting evidence in some steps; C = missing detail, oral account or no evidence. These differ from the corrected report's A–D categories.
- All times: Asia/Shanghai, UTC+8.

## 1. Factual inventory as originally drafted

| ID | Scenario | Inferred manual method | Qwen Office / DingTalk use | Result stated in the draft | Original rating | Conditions / limits | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | Obtain materials and install capabilities | Read event material and configure tools manually | Group screenshot → AI locates Qwen Office group and Project Manager manual card; unpack ZIP, install and recognize seven skills | Located/installed during 15:27–15:38. Manual belonged to Alibaba organization; server denied cross-organization reading. No bypass; suggested organization login change or owner-provided local copy | A | Organization boundaries; skill quality defines behavior | Session #25–#20; skillpack with seven .skill files and README; seven installed shanqin-* skills |
| S2 | Prepare environment | Request environment, create group, upload document | “I am number 30” → demo30 via MCP/SSE; reset to three contracts/three projects/three customers/zero tracking; create collaboration group and agreement document; share | Seven steps during 15:40–15:45. Read-only host prevented `--content-file`; inline content creation and readback used | A | Simulated ledger; local tenant-list file absent, address inferred from a fixed pattern and checked through reset | Session #19–#18; group message 10 October 15:45:10 |
| S3 | Extract contract fields and confirmation gate | Read contract and enter fields manually | Locate group agreement, read, extract number/Party A/project/amount/expiry/status; **wait for human confirmation** before ledger write | Values matched HT-2026-0007, Qinchuan, RMB 850,000, expiry 09-10. At 16:12 still three contracts. Later ledger shows creation 10 October 16:13:39; no matching confirmation in the message record, and 20:33 recap still says pending (C-1) | B | Human confirmation required; past reminder times skipped with explanation | Session #17–#16; `contract_list_by_expiry` query on 14 October; recap |
| S4 | Risk review | Read ledgers and calculate/sort overdue items manually | “Any recent problems?” → scan contracts/projects/tracking, rank urgency and suggest action | Three overdue contracts, 131/32/25 days; two projects, RMB 250,000 overspend plus 15% lag, and 7% lag. Results private unless asked to post | A | Current date and returns rather than script dates | Session #15–#14 |
| S5 | Spoken instruction to tracking workflow | Record instruction, reminder and group notice manually | Owner to explain within a week → project/requirement/deadline (+7 days, 10-17)/owner; RT-001, 17 October 18:00 to-do and correction card | Draft claimed consistency across ledger, personal to-do and group card, read back after 15:56:23 delivery; no instruction expansion. On 14 October tracking count was zero; RT-001's absence unexplained (C-2) | B | Explicit instruction precedes tracking write; MCP toolset had no delete/close tracking tool | Session #13–#12; 15:56:23 group message; 14 October `risk_track_list` |
| S6 | Customer decision support | Review relationship history manually | “Is it worth it? Show me the background” → five projects, RMB 15.6 million, major customer; report expiry and overspend with advice | Private reply only; framed as information for the manager to decide | A | Private distribution is a skill convention that must be defined in advance | Session #11–#10 |
| S7 | Briefing and pending decisions | Aggregate ledgers, draft and distribute manually | Summarize today, post and mark decisions → three-source reads; four-section card, manager mention, next-day to-do | Delivered 16:03:01. First send rejected for missing mention placeholder; corrected resend; final card only; three decisions highlighted red | A | Finalized card template and platform mention rules | Session #9–#8; 16:03:01 group message |
| S8 | Unattended daily inspection | Daily manual queries or no inspection | Run each morning, notify only on issues → daily 09:00 task plus immediate demo | Demo delivered 16:12:09. Draft claimed a day-seven defect found/fixed. Four later days: 11 October too_late, 12 October sleep, neither with a report; 13/14 October around 09:11, overdue counts 135/36/34/29 | A | Desktop availability/wake and connector login; draft described missed days as silent except in logs | Five cron logs; reports at 16:12:09, 13 October 09:11:57, 14 October 09:11:38; session #7–#6 |
| S9 | Retrospective and upward reporting | Write recap and reporting material manually | AI recap from session; related WeChat article merged into another and not separately published; 13-slide internal deck on 11 October with anonymized comparison | Recap/deck completed and locally rendered. Deck theme: coding-agent practice; whether it included Shanqin was then marked unresolved | A for file existence | Anonymized wording omitted internal product names; no PowerPoint application check | Local recap; presentation README; memory notes dated 10/11 October |
| S10 | Manager demonstration and report request | — | User said results were demonstrated to the manager, who supported the exercise and requested this report | No session record or written feedback located | C, missing details | M-2 | User's request, 14 October |

## 2. Contradictions and questions recorded at the time

| ID | Question | Evidence on each side | Original treatment |
| --- | --- | --- | --- |
| C-1 | Time and trigger of HT-2026-0007 entry | Ledger `created_at=2026-10-10 16:13:39`; contract in 13/14 October reports. No confirmation-to-write dialogue among 26 messages; 20:33 recap still says not entered, awaiting confirmation | Draft declined to choose a side: confirmation request and no entry before 16:12 were treated as established; actor/trigger at 16:13:39 unresolved. It speculated about later supplementary or environment-side action, with no record |
| C-2 | RT-001 no longer visible | Present on 10 October in write/notice/briefing; zero tracking on 14 October and in 13/14 October reports; no delete/close tool | Timing and reason unresolved; possible later session action or event environment maintenance, neither verified. Draft still claimed the 10 October instruction-registration-notification-to-do workflow occurred |
| C-3 | Official event name | Group belongs to “Agent GO·智涌创想会”; repository review asked Leo to confirm official name | Use “Qwen Office event,” with Qwen Office DingTalk group as community, until clarified |

## 3. Missing information register

- M-1: official event name, organizer, agenda and scale. Group membership was around 19–20; the manual's “68 people viewed” is a document-view count, not event attendance.
- M-2: manager-demo date, form, content and original feedback; only user account available. The 11 October coding-agent deck's relationship to Shanqin was then unresolved.
- M-3: efficiency baseline and before/after measures. **No manual baseline was measured**; no efficiency percentage or cost saving supplied.
- M-4: suitability for real bank data, systems or intranet environments: not tested.
- M-5: resolutions of C-1/C-2 ledger questions.
- M-6: authorized access to the full manual. The session read group context and package README, not the Alibaba-organization document body.

## 4. Evidence index retained from the draft

- **Session:** `mv22nwqf5tdz5b7u`, 26 messages checked; inspection subtask `5555f0e8-2583-4689-ac7d-de780fb5320f`, two messages; scheduled task `fd7535a5-af03-4acb-ac4b-3aec40d51510`, daily 09:00, enabled.
- **Five cron records:** 10 October 16:11 manual demo ok; 11 October 09:00 missed(too_late); 12 October 09:00 missed(sleep); 13 October 09:11 ok; 14 October 09:10 ok, with 53–69-second execution durations.
- **Shanqin collaboration group:** `cid5KP1WJ8FeT/cp3zL+w6Jaw==`; six messages: 10 October 15:45:10 agreement sharing, 15:56:23 correction, 16:03:01 briefing, 16:12:09 inspection; 13 October 09:11:57 and 14 October 09:11:38 inspections.
- **14 October ledger queries:** `contract_list_by_expiry(30)` returned four contracts, including HT-2026-0007 created 10 October 16:13:39; `risk_track_list` returned zero.
- **Local files:** session agreement, `skillpack/` with seven packages and README, `outputs/陕秦三端联动演示复盘-2026-10-10.md`, group screenshot in `uploads/`; merged unpublished standalone article under `03_outputs/articles/`; `03_outputs/presentations/qwen-agent-coding-agent-retro-20261010/`; `.workbuddy-ai/memory/2026-10-10.md` and `2026-10-11.md`.
- **Count note:** screenshot membership 19 versus query membership 20 on 10 October reflects different times; not used as evidence for event scale.
