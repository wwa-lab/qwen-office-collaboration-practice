# Qwen Office and DingTalk Collaboration: Shanqin Observations and Application Proposals — Original Draft

**English** · [简体中文原文](千问办公与钉钉协同实践-基于陕秦项目的场景观察与应用建议-初稿-2026-10-14.md)

> **Historical draft M1, not the current assessment.** Its original claims and self-review verdicts are translated below for comparison. Later review qualified or corrected assertions about complete workflows, enforced controls, a day-seven fix, scheduling causes and reliability. U3 confirms that Leo Zhang observed AI contract entry throughout and did not click the agreement. Use the [corrected formal report](report/04_final_report_EN.md) and [evidence matrix](report/02_evidence_matrix_EN.md) for current conclusions.

**Document type:** internal report draft for management review.\
**Report date:** 14 October 2026.\
**Perspective:** business and management needs of a bank technology department.\
**Material:** 10 October session records, DingTalk messages, demo-ledger queries, task run logs and local recap; see Appendix A.\
**Practitioner:** Leo Zhang.

## Part I. Background and purpose

On Saturday, 10 October 2026, I attended a Qwen Office event on behalf of the company. Its community was the Qwen Office DingTalk group; the official event name remained to be confirmed. I received the Shanqin Project Manager manual and skills, and experienced the seven scripted scenarios in the demo environment during 15:27–16:12, approximately 45 minutes. The draft described the daily inspection as continuing unattended over the following four days. I subsequently demonstrated results orally to my manager, who supported the exercise and requested this report; no written demonstration record was available.

Two boundaries apply:

1. **The organizer supplied a simulated environment**, tenant demo30. All contracts, projects and customers were demo data. The subject is workflow capability, not real business outcomes.
2. **No manual baseline was measured.** No efficiency percentage or cost saving is claimed; figures require sources and definitions.

The exercise asked which work steps change when an AI office client connects a messaging platform and business system, whether those changes can help technology teams, and what conditions a bank enterprise environment would require.

## Part II. Scenarios and observations in the draft

These five scenarios were selected from execution records. “Original method” is an inferred comparator, not a measured baseline.

### Scenario 1. Skills distribute capabilities; first scenario in about ten minutes

- **Manual comparator:** read material and configure tools/accounts individually.
- **Action:** AI located the group/manual card from a screenshot, then unpacked a ZIP, installed and recognized seven skills during 15:27–15:38.
- **Reported result:** about ten minutes from installation to the first working scenario. Cross-organization manual access was denied; no bypass was attempted. Suggested routes were changing organization login or an owner-provided copy.
- **Original validation label:** executed.
- **Limits:** organization-level data boundaries; skill quality determines behavior boundaries.

### Scenario 2. Group agreement → extraction → confirmation → ledger

- **Manual comparator:** read a contract and enter fields.
- **Action:** AI retrieved group messages, located/read the agreement, extracted number/Party A/project/amount/expiry/status and **waited for human confirmation** before writing.
- **Reported result:** values matched HT-2026-0007, RMB 850,000 and expiry 09-10. The draft treated the three-contract count at 16:12 as evidence of the confirmation gate. A ledger record was later timestamped 10 October 16:13:39, but no triggering dialogue was located; the evening recap still said pending. C-1 recorded the conflict, and the draft did not treat it as a fully closed confirmation process.
- **Original validation label:** extraction and confirmation gate executed; write trigger unresolved.
- **Limits:** human confirmation before writes; expired reminder times skipped with an explanation.

### Scenario 3. Spoken instruction → structured registration → three-system tracking

- **Manual comparator:** record the manager's request, set a reminder and draft a group notice.
- **Action:** the manager requested an explanation within a week for metro-project overspend and how to recover money, asking for system registration and a due-time reminder. AI extracted project, requirement, seven-day deadline and owner; created RT-001 and a 17 October 18:00 to-do; posted a correction card.
- **Reported result:** ledger, personal to-do and group notice were described as consistent, without expanding or rewriting the instruction; message readback followed 15:56:23 delivery. The item was absent on 14 October, with reason unresolved in C-2. The draft nevertheless retained its claim that the 10 October instruction-registration-notification-to-do workflow occurred.
- **Original validation label:** workflow executed; subsequent state unresolved.
- **Limits:** explicit instruction before registration; AI should not expand or narrow the manager's scope.

### Scenario 4. Current data → briefing → explicit decisions

- **Manual comparator:** aggregate daily ledgers, draft and distribute a report.
- **Action:** “Summarize today, post it to the group, and mark what I must decide.” AI read contracts/projects/tracking, posted a four-section card—new, risks, handled, decisions—with a manager mention, and created next-day follow-up.
- **Reported result:** delivery at 16:03; three decisions highlighted red: renew/recover or stop losses on two overdue contracts, and whether to enter the supplementary agreement. The draft described this as making management decisions explicit in structured form. The first send was blocked by mention-format validation; correction left only the final version.
- **Original validation label:** executed.
- **Limits:** finalized reusable card layout; platform distribution-format rules.

### Scenario 5. Unattended inspection, with four subsequent days recorded

- **Manual comparator:** inspect ledgers daily, or leave them unchecked.
- **Action:** automatically inspect each morning, notify on issues, remain quiet otherwise; created daily 09:00 scheduling and immediately demonstrated it.
- **Reported result:** demo report arrived 16:12. The draft attributed a missing tracking item to an exact-day-seven boundary and claimed correction restored behavior. It described four subsequent days: missed on 11/12 October due to an offline/asleep desktop, no report except logged errors; normal reports around 09:11 on 13/14 October, with overdue days increasing, for example 131 to 135.
- **Original validation label:** executed, with four-day logs and two missed runs.
- **Limits:** online execution host and connector login; draft claimed no active missed-run alert. Rule boundaries require testing and versioning.

## Part III. Findings and potential value as originally stated

**1. Incremental value in the connected workflow.** The draft described input → processing → ledger action → collaboration → inspection within one conversation, removing manual transfer. It proposed evaluating whole-process improvement because isolated summary/translation functions already exist.

**2. Control design matters more than a capability list.** Waiting for write confirmation, keeping decisions private, checking readback and blocking invalid formats were emphasized. The draft claimed no unconfirmed ledger writes in the main flow and proposed confirmation, distribution boundaries and readback as bank acceptance criteria.

**3. Procedures can be distributed with their defects.** Skills were described as enabling installation and immediate use, with a first scenario in about ten minutes. The claimed day-seven omission illustrated the need for asset versioning, boundary tests and named ownership.

**4. Structured language and current definitions reduce relaying loss.** The draft said a spoken instruction became four consistent fields across systems, using current dates/returns rather than expired script definitions. It proposed the method independently of any product.

| Work area | What the draft labeled demonstrated | Further exploration |
| --- | --- | --- |
| Project communication | Structured notices/briefings/reports, mentions and linked to-dos | Information classification and audit in real project groups |
| Requirements and preparation | Document extraction and six structured fields | Accuracy on internal requirements templates |
| Documents and reporting | Recap and reporting deck generated from session records | Suitability for formal institutional documents |
| Task coordination and progress | Instruction-registration-to-do-inspection workflow | Integration with internal project management |
| Knowledge and reuse | Skill packages, recaps and evidence indexes | Organizational skill-library governance |
| AI-assisted development | Outside this practice; separate coding-agent recap exists | Separate evaluation required |

## Part IV. Constraints and adoption conditions

Except for observations explicitly identified, these are **evaluation topics**, not asserted product defects.

1. **Security and sensitive data:** only demo organization/data were used. Assess residency, transmission, model retention and demo/production isolation. A cross-organization read was blocked, but bank permission-mapping granularity needs separate validation.
2. **Permissions and access:** demo writes used a personal account. Enterprise use requires service identity, least privilege, retained audit logs and traceability.
3. **Accuracy and review:** the draft cited a corrected day-seven rule and human confirmation of extraction as observed controls. Reviewer ownership, review evidence and correction deadlines still need evaluation.
4. **Integration:** MCP over SSE connected a public demo ledger. Internal APIs, authentication and networking differ; feasibility untested.
5. **Execution host and scheduling:** the draft linked missed, silent days to desktop unavailability/sleep. Assess server execution, missed-run alerts, catch-up and operational ownership.
6. **Adoption and cost:** skills were described as reducing individual rollout effort, but require maintenance/testing/release governance. No rollout cost was measured.
7. **Benefit measurement:** no baseline exists. Establish one and measure before reporting efficiency; do not use promotional claims.

**Relationship to existing work:** do not assume a new tool is superior. The draft favored assistance for transfer, repeated aggregation, formatting and date calculations. Decisions, external commitments, sensitive distribution and final acceptance remain with people and existing approval processes. “AI executes, manager decides” was proposed as a target division of responsibility.

## Part V. Recommendations in the historical draft

1. **Four-week pilot with low-sensitivity, anonymized scenarios.** Candidates: minutes-to-to-do tracking, weekly project-data briefings, document-field checklists. Use anonymized/synthetic data without real customer information; name one owner per scenario.
2. **Baseline before efficiency claims.** Week one: manual time, rework and omissions. Later weeks: comparable measures plus AI correction rate, missed/silent runs and confirmation-gate invocation/pass rates. No efficiency reporting before baseline data.
3. **Written controls.** Define write-confirmation gates, private/group distribution, readback completion, AI identity, least privilege and audit requirements before starting.
4. **Skill governance.** Versioning, boundary tests—including dates, empty data and organization boundaries—release approval and ownership.
5. **Expand based on results.** At four weeks, review against preset metrics. If criteria and controls work, consider anonymized real-project data and integration; otherwise document limits/improvements and pause expansion. Resolve host and missed-run alert issues first.

These are the old draft's proposals. The corrected report instead recommends a smaller, bounded evaluation with its own stated conditions.

## Part VI. The draft's management summary

The draft claimed that connecting an AI office client, messaging platform and business ledger completed information input → decision support → action → notification → reinspection within one conversation, across seven scenarios in approximately 45 minutes. It also claimed confirmation, private distribution and readback controls worked, with no unconfirmed main-flow writes. Four subsequent days of unattended scheduling exposed dependence on the execution host, including two missed days.

Potential value was described as less copying and repeated aggregation, explicit pending decisions and unattended inspection. Real-bank suitability, quantified efficiency and fit with enterprise scheduling/permissions were **unverified**, with no measured evidence for positive or negative conclusions. The proposed next step was a reversible four-week, two-to-three-scenario anonymized pilot, using manual baselines and preset expansion criteria.

## Appendix A. Evidence index from the draft

- Practice session: `mv22nwqf5tdz5b7u`, 10 October 15:27–20:39, 26 messages checked; inspection subtask `5555f0e8-…`; daily 09:00 task `fd7535a5-…`.
- Five logs: 10 October 16:11 demo ok; 11 October 09:00 missed(too_late); 12 October 09:00 missed(sleep); 13 October 09:11 ok; 14 October 09:10 ok.
- Six collaboration-group messages: 10 October 15:45:10 / 15:56:23 / 16:03:01 / 16:12:09; 13 October 09:11:57; 14 October 09:11:38.
- 14 October demo queries: four contracts, including HT-2026-0007 created 10 October 16:13:39; zero tracking items.
- Local materials: Shanqin recap, seven skill packages, group screenshot; merged article not separately published; 13-slide internal coding-agent adoption recap dated 11 October, with anonymized comparison for frontline/middle/senior audiences.
- Working drafts: [practice inventory](practice_materials_and_facts_EN.md), [key findings](original_key_findings_EN.md).

## Appendix B. Contradictions and missing details

- **C-1:** contract creation timestamp 10 October 16:13:39 conflicts with session/evening pending-confirmation narrative; trigger unresolved. The draft treated only its main-flow confirmation gate as verified.
- **C-2:** RT-001 present on 10 October, zero tracking on 14 October; time/reason unresolved, no demo delete-tool record.
- **C-3:** official event name unresolved; use “Qwen Office event.”
- **M-2:** no written manager-demo date, format or feedback, only the user's account.
- **M-3/M-4:** no efficiency baseline or real internal-environment evaluation; no quantified benefit.

## Appendix C. Original management-view self-review

The original draft recorded the following **self-review verdicts**. They are retained as historical text, not fresh or independent acceptance:

1. **Too much product introduction?** Scenario/evidence-led, capabilities within examples rather than a feature list. Original verdict: Pass.
2. **Missing real cases/evidence?** Five scenarios with message times, run logs and ledger fields. Original verdict: Pass.
3. **Confusing validation with future ideas?** Scenario labels, evaluation topics and demonstrated/exploratory table. Original verdict: Pass.
4. **Unsupported efficiency/cost claims?** No savings percentages or amounts; 45 minutes used only as demo duration. Original verdict: Pass.
5. **Ignoring bank-enterprise constraints?** Seven topics: security, permissions, accuracy, integration, host, rollout cost and measurement, with missed-run evidence. Original verdict: Pass.
6. **Can management quickly understand the next step?** A one-page, conclusion-first summary and actionable small steps. Original verdict: Pass.

Issues the draft said it corrected during self-review:

- Replaced “inspection replaces manual daily review” with unattended review in the demo environment, adding operating prerequisites after two missed runs.
- Removed “68 people viewed” from the argument about event reach because it measured only one document's views.
- Registered C-1/C-2 instead of ignoring conflicts or choosing one narrative, and disclosed them in the relevant scenarios.
