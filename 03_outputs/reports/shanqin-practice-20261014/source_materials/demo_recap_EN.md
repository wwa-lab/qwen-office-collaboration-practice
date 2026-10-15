# Shanqin Project Manager: Three-System Demonstration Recap

**English** · [简体中文原文](陕秦三端联动演示复盘-2026-10-10.md)

> **Historical AI-generated source (M4), not the current assessment.** This translation retains the recap's claims, including claims later qualified or corrected. The current [formal report](../report/04_final_report_EN.md) and [evidence matrix](../report/02_evidence_matrix_EN.md) govern. In particular, a complete workflow, enforced confirmation, delivered reminders and a successful day-seven fix were not established. Scheduling was provided by Qwen Office. Practitioner: Leo Zhang.

**Demo date:** 10 October 2026, 15:27–16:12, approximately 45 minutes.\
**Demo tenant:** demo30.\
**Participating systems, as described in the recap:** Qwen Office AI; DingTalk groups/documents/to-dos/scheduled tasks; Shanqin business system (Project Manager MCP ledgers).

## I. Background and objective

The demo began with a Shanqin Project Manager manual and accompanying skills shared in the “Qwen Office” DingTalk group. After installation, the scripted workflow connected the business system, collaboration group and manager's instructions: contract entry → risk review → instruction tracking → business briefing → automatic daily inspection.

The recap aimed to exercise the manual's seven skill scenarios, assess three-system usability and record problems and responses for later customer demonstrations and implementation delivery.

## II. Timeline

| Time | Action / skill | Main output |
| --- | --- | --- |
| 15:27 | Locate group messages and manual | Identified the Qwen Office group and manual card; read sharing context from the implementation consultant's 15:17 post |
| 15:37 | Install skills | Installed seven skills: preparation, contract entry, risk scan, risk tracking, briefing, customer decisions and daily inspection |
| 15:40 | Preparation, shanqin-prep | Connected demo30; reset to baseline: three contracts, three projects, three customers, zero tracking items; created Shanqin collaboration group; archived and shared HT-2026-0007 metro-monitoring agreement |
| 15:48 | Contract entry | Located agreement, extracted number/Party A/project/amount/expiry/status; requested human confirmation before writing |
| 15:50 | Risk scan | Three overdue contracts: 131/32/25 days; two at-risk projects: RMB 250,000 overspend plus 15% lag, and 7% lag; prioritized suggestions |
| 15:55 | Risk tracking | “Give me an explanation within a week” became RT-001, due 17 October; created a due-time to-do and group correction card |
| 15:58 | Customer decision | Qinchuan history: five projects, RMB 15.6 million, major customer; presented expiry and overspend and suggested retaining the relationship while addressing both; **private reply only** |
| 16:00 | Business briefing | Four sections—new, risk, handled, decisions—with a manager mention; three pending decisions highlighted red; next-day follow-up to-do |
| 16:10 | Daily inspection | Created daily 09:00 task; immediate demo report arrived at 16:12; notify on issues, stay quiet otherwise |

## III. Highlights reported in the recap

**Business system:** the recap claimed real-time reads/writes across contracts, projects, customers and tracking, with all report figures taken from current returns rather than old or invented values.

**DingTalk:** it described six capabilities—groups, archived documents, colored Markdown cards, mentions, to-do reminders and scheduled tasks—and four formatted messages: contract sharing, correction notice, briefing and inspection report.

**AI:**

- **Understand business language:** parsed a weekly-response instruction into project, requirement, seven-day deadline and owner without embellishment.
- **Confirmation and write safety:** claimed it waited for manager approval before contract entry, with no mistaken ledger writes; group posts, group creation and to-dos used confirmation or finalized formatting gates.
- **Distribution boundaries:** customer decisions stayed in private conversation; notices, briefings and daily reports went to the group.
- **Complete workflow:** claimed manager instruction → ledger → group notice → personal to-do → next-day reinspection formed a complete management cycle.

## IV. Problems and responses recorded at the time

1. **Cross-organization isolation:** the manual belonged to an Alibaba organization while the connector was signed into the demo organization. The server denied access. The AI did not bypass it and suggested changing organization login or having the owner provide a copy in the current organization. Local-organization messages and skills remained available.
2. **Read-only working directory:** the command host could not use the skill's recommended `--content-file` method. Inline content created the document instead. The recap claimed content and byte-count readback matched before success was confirmed.
3. **Mention formatting:** a mentioned member required a body placeholder. The first send was blocked, then corrected and resent. The recap reported only the final message remained.
4. **Day-seven boundary:** the recap attributed RT-001's absence to the first inspection excluding items due exactly seven days later. It said the rule was changed to include day seven and the schedule remained enabled, predicting the item would appear in the next day's report.
5. **Script dates versus actual date:** template contracts dated August–September were already overdue on 10 October. The recap said the AI used current dates, reported actual overdue days and skipped reminder times already in the past with an explanation.
6. **Confirmation design:** it claimed contract writes and correction deadlines had human confirmation or explicit instructions, with no unconfirmed ledger writes, validating the “AI executes, manager decides” division.

## V. Outputs listed in the recap

- Seven skills reported as verified, covering seven script steps.
- Four finalized Markdown group cards: document sharing, correction, briefing and inspection.
- One tracking item: RT-001, metro-project overspend correction, due 17 October.
- Two to-do reminders: 17 October 18:00 and 11 October 09:00.
- One daily 09:00 inspection task, notifying only on issues.
- One demo30 environment with baseline data plus that day's demonstration increments.

## VI. Open items and next steps recorded at the time

1. Three highlighted decisions: renew or recover the RMB 3.10 million Yan'an Energy & Chemical contract, 131 days overdue; renew or stop losses on the RMB 5.12 million Qinchuan metro contract, 32 days overdue with project overspend; confirm entry of HT-2026-0007, RMB 850,000.
2. Contract entry remained described as awaiting confirmation: six fields ready, with “confirm” intended to trigger entry and a receipt.
3. Full manual access would require changing organization login or an owner-provided copy.
4. The recap expected the first scheduled 09:00 run the next day to include RT-001's six-days-remaining warning.

## Appendix: reusable implementation lessons proposed in the recap

- Define private-versus-group distribution rules in the skill before use.
- Finalize card colors, sections and mention placement in templates to reduce demonstration rework.
- Use the execution date and system returns for overdue/near-due values; treat script wording only as structural guidance.
- Require human confirmation for ledger writes, runtime format checks for mentions, and readback for documents/messages before claiming success.

These are the recap's historical statements. Later corrections and unresolved evidence gaps are recorded in the current report linked above.
