# Open Questions

**English** · [简体中文原文](05_open_questions.md)

**Updated:** 14 October 2026. This list separates user clarifications already obtained, missing original records and decisions needed before further testing. Unanswered questions are qualified in the report and do not prevent delivery.

## 1. Clarifications received

| ID | Original question | User response and treatment | Remaining boundary |
| --- | --- | --- | --- |
| Q01 / former C-1 | Why did the agreement appear in the ledger while the main session still said confirmation was pending? | U3: the user did not click the agreement and watched AI entry throughout in Qwen Office. Withdraw manual-web-entry attribution; retain AI entry as a personal observation. | Locate the write call, confirmation context and receipt and match them to the 16:13:39 ledger record. The gap neither establishes unauthorized action nor negates the observation. |
| Q02 | Did multiple people actually receive and handle tasks? | User confirmed a single-person demonstration; this scope is used throughout. | No multi-person acceptance, handling or closure results. No need to ask again whether multi-person testing had already happened. |

## 2. Questions affecting reliability

| ID | Question and evidence location | Needed to answer | Suggested provider / reviewer | Decision impact |
| --- | --- | --- | --- | --- |
| Q03 / former C-2 | RT-001: R1 L438 returned one item at 16:02; R2 L33 returned zero at 16:11 | Actual tenant/connection scope for both calls; intervening reset/change audit; server persistence records | Demo platform maintainer and operator | Tracking continuity; do not rely on automated follow-up until explained |
| Q04 | Did the day-seven change work? | Before/after outputs with RT-001 present, plus six/seven/eight-day and overdue cases | Technology testers, platform if needed | Only a prompt change is established; do not claim a successful fix |
| Q05 | Did the to-do have a due-time notification, and was it delivered? | Final configuration, dueTime readback, reminder settings, notification and receipt evidence | User/platform team | Creation is not delivery; defer critical reminders |
| Q06 | Exact causes of 11 October `too_late` and 12 October `sleep`, and catch-up behavior | Scheduling decision times, host status, wake/recovery logs, actual `run_latest` rules | Platform/operations | Do not guess that too_late means offline or generalize recovery to long-term reliability |
| Q07 | Source of the delay from 09:00 to about 09:12 | Queue start, task start, API durations and delivery time | Platform/operations | Assess business timeliness, not only 53/69-second execution durations |
| Q08 | Did other channels report missed runs? | Personal notifications, system messages and maintainer alerts at the time | User/platform team | This group lacked reports; that does not establish platform-wide silence |
| Q09 | How are confirmation, target binding, retries and distribution boundaries enforced? | Tests of refusal, reconfirmation after change, retries, wrong groups, insufficient rights and document-injected instructions | Technology/platform/security owners | Separate prompt conventions from enforceable controls; informs write-access decisions |
| Q10 | Was coverage sufficient for a complete daily briefing? | Coverage definition, date window, missing/failed data handling and merging of operations outside the session | Business/project and platform teams | Risk queries and session increments do not establish coverage of every business matter |
| Q11 | Can contract status, renewal and payment be interpreted further? | Terms, renewal/payment records and business definitions | Business data owner | Unsupported business conclusions were removed; do not invent real facts to complete a demo |

Q03 candidates include changed state, connection scope and environment maintenance; none is confirmed. The absence of a dedicated delete tool does not rule out resets or changes by another actor: K1 explicitly includes `reset_baseline`. Do not rerun a reset to “verify” a historical event.

## 3. Human decisions before further testing

| ID | Decision | Suggested starting position | Decision owner |
| --- | --- | --- | --- |
| Q12 | Which two actual tasks and current methods? | Begin with field extraction and draft project briefings, based on real needs rather than copying demo contracts | Manager, business/project owner |
| Q13 | Permitted tools, accounts, data and environments? | Synthetic material first; anonymization does not itself authorize uploading | Security, data and platform owners |
| Q14 | Operator, reviewer, time and resource limit? | Proposed window within two weeks and two scenarios; six pairs per scenario is a starting design, not an obligation or approved budget | Manager, evaluation lead |
| Q15 | Critical errors, acceptable improvement and stop conditions? | Critical errors must not pass acceptance; stop unauthorized writes/distribution; agree time thresholds before results | Business/project reviewer and relevant control owner |
| Q16 | If drafting works, is a platform connection needed? | Compare AI drafting plus manual transfer with connected AI before deciding | Business/project and platform teams |
| Q17 | Who owns maintenance and recovery? | Assign configuration, templates, monitoring, takeover and version responsibility | Technology, platform/operations |

## 4. Background details that do not affect the current assessment

- Official event and organizer names: group/error displays use “Agent GO·智涌创想会”; existing articles/status records use “Agent Go 智勇创享会.” Use “a Qwen Office event” until resolved. Group membership and document views do not establish event size.
- Date and scope of the manager demonstration: the user's account establishes that it happened and prompted the report; written proof is unnecessary. Ask for scope only if the report must list it.
- Full manual: the original read was denied. An authorized copy could be obtained from its owner if the complete workflow later needs checking. Missing the manual does not mean skill/execution evidence is absent.
- Instructor photographs: original photos referenced with truncated filenames were not located in the relevant directories. Instructor claims about benefits or organizational rollout are not used.

## 5. Conclusions not made in this review

No measured efficiency improvement, cost saving, adoption willingness or satisfaction; no conclusion about bank production suitability or compliance; no overall product failure/correctness rate; no attribution of contract entry to manual webpage operation or equation of personal observation with full write-control acceptance; no equation of an `ok` log or delivered message with business closure.

## Change history

- 14 October 2026: user clarified Q01/Q02; other questions organized by impact and owner, with unverified status retained.
- 14 October 2026: Q01 revised under U3 to observed AI entry. Remaining questions concern the execution chain and confirmation context, not whether the user clicked manually.
