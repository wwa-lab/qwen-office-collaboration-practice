# Management Analysis

**English** · [简体中文原文](03_management_analysis.md)

**Analysis date:** 14 October 2026. Factual basis: E01–E24 in the [evidence matrix](02_evidence_matrix_EN.md). Selections, priorities and experiments here are independent analysis or proposals, not implemented measures.

## 1. Overall assessment

A bounded evaluation is worthwhile; current evidence does not support deployment or wider use. The useful observation is that natural-language requests can call existing business tools and place results into documents, group messages and to-dos. The next test is whether those connections reduce human effort, including review and rework, without reducing delivery quality. [E04, E07, E11, E20–E22]

This was a short demonstration with one operator, synthetic data and preset skills. Some operations worked; incorrect explanations and inconsistent states also appeared. A model's completion reply, a successful API return, an `ok` task status and a properly resolved business matter are distinct outcomes. The records establish some of the first three, but not the last. [E01, E09–E10, E12, E15]

## 2. How the work changed

The manual methods below are reasonable hypotheses for designing a comparator. They were not measured on site and do not describe HSBC's current processes.

| Stage | Manual comparison task | Demonstrated replacement or connection | Human responsibility / unfinished work |
| --- | --- | --- | --- |
| Locate inputs | Find messages and attachments; confirm version | Qwen used a connector to find the contract link and read its content | Correct business object, legitimate source and version |
| Process documents | Read and enter fields | Structured fields and a confirmation request; user observed AI contract entry | Amounts, dates, parties and omissions; confirmation-to-write call chain still to check |
| Summarize risks | Query ledgers, combine lists, prepare reporting | API supplied rule calculations; Qwen organized the narrative and decisions needed | Coverage, meaning and business judgment |
| Register action | Record instructions, set to-dos, notify | One request produced tracking, a personal to-do and a group message | Named owner, acceptance, handling and closure; unverified |
| Repeat checks | Query on time and follow up exceptions | Qwen scheduled reads and daily reports to DingTalk | Missed runs, differing states, catch-up, duplicate sends and incorrect root-cause claims |

Some cross-interface entry moved into tool calls. People could focus on confirming fields, checking meaning and handling exceptions. Whether total effort falls depends on whether saved copying exceeds configuration, waiting, review and recovery effort; the records cannot answer that. [E20–E21]

## 3. Four observed scenarios

### 3.1 Contract extraction and confirmation

The input was a short agreement built into the preparation skill and then created as a DingTalk document. The assistant read the group link, proposed the number, customer, project, amount and expiry date, separately explained status, and requested confirmation. Key values matched the source. However, input and example shared a source and were highly structured; unfamiliar formats, missing fields, ambiguous amounts and contradictory clauses were untested. [E04]

The user's latest clarification is that they did not click the supplementary agreement and watched the AI complete entry throughout in Qwen Office. The earlier manual-web-operation explanation is therefore withdrawn. AI entry is a direct personal observation, supported at the outcome level by the later ledger record. The reviewed main session still lacks the matching write call; confirmation context, call and receipt are needed to validate the execution chain. A confirmation request alone does not prove enforced control, and not clicking the agreement does not imply unauthorized AI action. Refusal, reconfirmation after changes and duplicate entry need testing. [E05, E14; U3]

Technology teams could apply the method of extracting fields from defined material, attaching source references and asking a person to confirm—for example, project-document inventories or handoff information. Use materials permitted by the relevant owners. This is a useful first test because fields and acceptance standards can be explicit; the example contract value is not a bank business benefit.

### 3.2 Ledger risks and decision briefings

The assistant read contracts, at-risk projects and tracking lists, prepared a group briefing, and distinguished an archived document from a pending ledger entry. This status distinction is more useful to management than card colors: it separates completed outputs from decisions still required. [E11]

The risk API already calculated `days_left`, `overrun_wan` and `lag_pct`. The model mainly called, aggregated and expressed the results; not all risk detection belongs to the model. Actual progress of 45% versus 60% planned is a 15-percentage-point gap. Contract expiry differs from overdue payment. Customer-analysis statements about incomplete formalities and revenue lacking contractual protection exceeded the returned data. Review must check both numbers and the basis for judgments. [E06, E12, E23]

Prioritize testing draft project-status and decision briefings with identical input scope and acceptance standards. Check omissions, incorrect attribution and unsupported advice. Colored cards, automatic mentions and polished wording are ordinary features; real recipients must establish whether they improve reading and response.

### 3.3 One instruction creates tracking and notification objects

A request for the owner to respond within a week became a project, corrective action, 17 October deadline and generic “project owner.” Tracking creation succeeded, with a to-do receipt and group-message readback. This is the strongest example of text becoming actionable work objects. [E07]

The owner was not resolved to another named person; the to-do belonged to the demonstrator, and the group was a single-person demo. There is no recipient acceptance, handling, escalation, closure or actual notification-delivery record. Three records do not establish connected responsibility. RT-001 was present at 16:02 but absent from another task's read at 16:11; the inconsistency remains unexplained. [E08–E09; U2]

The next step should be a sandbox test with a named initiator and recipient. Within permitted test targets, check the item ID, owner, deadline, status and acceptance, and deliberately exercise one failure/retry. Completion means the same item is traceable across objects without duplication or omission, not merely that a message was sent.

### 3.4 Daily inspection and operational health

Records contain an immediate demonstration and four scheduled executions: two errors and two completions. The two completed group messages arrived roughly 12 minutes after 09:00. Logged durations of 53 and 69 seconds are execution durations, not total scheduled-to-delivery time. [E15–E16]

The 10 October API already returned zero tracking items. The main session then changed the prompt to include day seven, without evidence of a successful rerun with the same populated input. The lesson is that an assistant may present an uninvestigated explanation as a root cause, and a later summary may turn a configuration change into a successful repair. Preserve call context, tenant and raw returns before locating a data, connection, filtering or scheduling problem. [E09–E10]

“Notify only when action is needed” is attractive, but no group message can mean either no risk or no execution. Separate business notifications from operational health: the business group may stay quiet while maintainers can see failures, delays, catch-up runs and state discrepancies. Only this group's missing reports were checked; no claim is made that the platform lacks other alert channels. [E17]

## 4. What Qwen and DingTalk each contributed

| Component | Directly observed role | Not established |
| --- | --- | --- |
| Qwen Office | Interpret requests, organize language, call tools, create and run its scheduled tasks | Independently establish business facts, guarantee correctness or complete management responsibility |
| DingTalk platform and connectors | Read online documents, carry messages, create personal to-dos; access/format checks on some requests | Multi-person workflow, complete authorization controls or guaranteed due-time delivery |
| Demo business system | Contract/project/customer/tracking data, rule calculations and tracking writes | Accepted persistence, consistency, tenant isolation or bank integration |
| Skill packages | Preset steps, templates, distribution conventions and some exception handling | Installation without adaptation across teams, or equivalence to enforced policy controls |

Standalone AI can summarize material supplied manually. DingTalk's contribution here is retrieving input from existing work objects and making output into group messages and to-dos with readable links or records. Compare “AI generation plus manual transfer” with “AI connected to the platform” on similar tasks to establish reduced copying or more complete handoffs. [E20–E21]

For fixed fields, clear rules and already structured inputs, existing templates, queries or ordinary automation should also be comparators. If ordinary automation delivers more reliably at lower cost, model calls need not be added. Unstructured inputs and language organization are more plausible areas for model value; that remains a hypothesis.

## 5. Priorities and responsibilities

| Priority | Proposal | Rationale | Who should confirm before starting / expanding |
| --- | --- | --- | --- |
| First | Defined document-field extraction; draft project-status/decision briefings | Observed operations, reviewable outputs, identifiable errors | Business/project owner defines fields and acceptance; technology selects tasks |
| Next | Instruction registration and two-person handoff sandbox | Test platform value beyond standalone AI | Business assigns receiving responsibility; platform checks identities, targets and record links; security confirms scope |
| Defer | Unattended critical expiry reminders | Missed runs, delays, state discrepancies and delivery remain unresolved | Platform/operations defines channels, monitoring, catch-up, support and takeover |
| Defer | Automated customer prioritization or contract-recovery/loss-prevention advice | Strong judgments appeared with insufficient data; demo cannot assess consequences | Business defines evidence and decision authority, with relevant control functions as needed |
| No separate initiative | Card colors, article generation or more demo skills | Little additional evidence for the current decision | Include readability and maintenance cost within existing tests |

Before any bank pilot, security/data owners confirm tools, data categories, transmission and retention. Platform teams confirm identity, least privilege, audit and integration options. Technology runs tests and measurements. Business/project owners define correct answers, tolerances and final acceptance. This is proposed responsibility allocation; the manager must identify actual owners and processes. It assumes neither the presence nor absence of any HSBC configuration. [E24]

## 6. Lightweight evaluation proposal

### 6.1 Tasks and comparisons

Begin with a **validation window of no more than two weeks**: a proposed timebox, not an approved plan or promised time to benefit. Limit scope to the two priority scenarios, starting with synthetic material. Any later use of anonymized or real internal material remains subject to permitted scope. Define each task package's input, output, acceptance owner and stop conditions.

Prepare six pairs of similarly difficult but different tasks per scenario: 12 pairs, 24 executions, with 12 manual and 12 AI-assisted. This is a small exploratory design, not a basis for estimating department-wide benefits or reliability. Practice separately before timing; record training and configuration outside the proficient-operation baseline.

Match each pair by length, field count, source count, ambiguity and exception difficulty. Randomly assign manual/AI methods and alternate execution order. Avoid having the same person complete a document manually and then repeat it from memory using AI. Where practical, rotate operators and have reviewers apply a common standard without knowing the method. Both groups receive equivalent information and final delivery requirements; the manual group may use its normally permitted tools.

If briefing quality is acceptable, use four to six new pairs to compare “AI draft plus manual transfer” with “AI plus collaboration connection.” Keep this phase separate to isolate connection benefits. If the advantage is unclear, retain drafting support without expanding connectors.

### 6.2 A few metrics and how to record them

| Scope | Core measure | Method |
| --- | --- | --- |
| Both priority scenarios | Active human minutes | Sum finding material, prompting, mapping fields, reviewing, confirming, transferring, editing and recovering from errors; sum effort across people |
| Both priority scenarios | Total time to acceptance | From complete inputs and task start to acceptance; separately record system/human waits and include manual takeover after failure |
| Extraction | Correct/complete fields and critical errors, in draft and final | Check against business-approved answers and missing-field rules; separate amount, date and object errors |
| Briefing | Required facts covered, unsupported judgments, revision rounds | Link every fact to a source; count unsupported causal, responsibility or business claims and critical omissions |
| Two-person sandbox | Missing handoff information and inconsistent states | Check object, named owner, deadline, ID and acceptance for the same item; record only if this phase is actually run |

Record installation/training, recurring maintenance and prompt-editing time separately. If estimating benefits over a period, allocate these using actual task volume and show both before/after allocation. Do not report generation time alone. Retain every attempt, including failures, abandoned work, reruns and manual fallback.

Blank record fields: task ID; scenario/difficulty; input version; method; operator; start/acceptance time; active effort; waiting; draft quality; revisions; final quality; failure/fallback; configuration/maintenance time; reviewer; evidence location. Leave measured fields blank until execution.

### 6.3 Controls and exception cases

Use an independent sandbox. Do not change the existing demo's scheduled task merely to create a test.

1. Missing dates, two amount definitions, identically named projects and old/new versions together: flag or leave uncertainty blank rather than inventing values.
2. Explicit refusal to write, changed content after confirmation, duplicate submissions, a request to post to the wrong group and operational instructions embedded in document text: test whether confirmation and authorization bind to the actual object and content.
3. Items due yesterday, today and in six/seven/eight days: first confirm each API response contains the same item, then test filtering. Separately test empty lists, failed reads, wrong tenants and partial data; these must not all become “no risk.”
4. In an authorized environment, simulate sleep/offline, expired login, one-side write success with the other side failing, and retries. Record alerts, duplication and manual recovery.
5. Create a separate short-term test to-do and verify actual notification delivery rather than creation alone. For two-person handoffs, record recipient confirmation and subsequent action.

### 6.4 Decide from the results

Compare final quality under the same standard first, then human effort and total duration. Report paired differences, medians and ranges, with failures. Small samples provide direction, not department-wide cost savings or annual benefit estimates.

Proposed expansion criteria: final quality meets the original requirement; no unblocked critical factual error or unauthorized write/distribution; explainable net improvement after review, fallback and maintenance; recipients find the delivery usable; usage conditions are satisfied. The task owner must set acceptable time improvements and noncritical error tolerance before seeing results; this report supplies no invented thresholds.

Stop the relevant automated action and restore manual handling after unauthorized sending/writing, silent omission of critical items or untraceable states. If drafting saves time but connection costs erase the benefit, use drafting assistance only. If net improvement is unclear, preserve evidence and revise or stop rather than adding scenarios merely to prolong the pilot.

## Change history

- 14 October 2026: completed four-scenario analysis, priorities and the proposed evaluation.
- 14 October 2026: U3 withdrew manual-web-operation attribution and incorporated observed AI entry; single-person scope unchanged.
