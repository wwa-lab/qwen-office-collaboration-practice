# Operational Screenshot Evidence

**English** · [简体中文原文](07_operational_screenshot_evidence.md)

Capture date: **15 October 2026**, Asia/Shanghai. Real screens were viewed and captured read-only from the business webpage and local DingTalk client. They supplement currently visible results, not the original 10 October operation logs, and are not results of rerunning the scenarios.

## Scope

- UI-01: current contract ledger.
- UI-02: excerpt of the 10 October group briefing retained in the current client.
- UI-03: two practice to-dos in the current client.
- UI-04: current project progress, budget and spending ledger.
- UI-05: currently empty risk-tracking list.
- UI-06: current business dashboard.
- All six appear in the formal Markdown and HTML. Figure numbers follow reading order; UI identifiers remain stable. Preparation-material images do not occupy the report body.

## Evidence mapping

| ID | Directly visible (A: captured screen state only) | Historical analysis | Not established by the screenshot alone |
| --- | --- | --- | --- |
| UI-01 | Contract number, Qinchuan Urban Construction Group, RMB 850,000, expiry 2026-09-10 and entry date 2026-10-10 | E04, E05, U3 | Later ledger state, not the write process. The account of observing AI entry throughout without clicking the agreement remains based on U3. |
| UI-02 | “New today,” “risk alerts” and “handled”; agreement still marked ledger entry awaiting confirmation | E07, E08, E11 | A historical message in the current client does not establish its initial version or later closure. Single-person demo; “automatic prompt” does not verify notification delivery. |
| UI-03 | Two to-dos, assignee and deadlines: Sunday 9:00 AM for pending decisions; Saturday 6:00 PM for corrective follow-up; both show Complete buttons | E07, E08 | Supports existence, not reminder delivery, owner acceptance or business closure. Interpret relative dates with capture date and original records; not a new effectiveness test. |
| UI-06 | Four contracts totaling RMB 11.75 million, two at-risk projects, zero tracking items, contract/project details | E01, E06, E20 | Demo tenant state on 15 October, not benefits or historical operating statistics. “Due within 30 days” shows four while contracts below are overdue; definition unverified, not four established future expiries. |
| UI-04 | Metro monitoring: 45% actual, 60% planned, RMB 3.15 million budget, RMB 3.40 million spending; Yushang progress gap also visible | E06, E23 | Later read-only state, not the 10 October API return. “15% behind” is a 15-percentage-point gap. System risk labels are not all independent model detection. |
| UI-05 | All filter selected; “no risk-tracking items” shown; no RT-001 visible | E07, E09, E10 | Current state does not prove deletion or explain the two 10 October reads. Alongside existing to-dos, it shows why each work object's state needs separate checking. |

## Time and version boundaries

1. Ledger: HT-2026-0007, RMB 850,000, entry 2026-10-10. The capture date is 2026-10-15, so overdue-day counts differ from 10 October logs. No operator field or write-call trace is shown. U3's correction—AI entry observed throughout in Qwen Office—remains unchanged.
2. The briefing is labeled 10 October and still says ledger entry awaiting confirmation. It and the ledger represent different times; this does not support manual-entry attribution. Accessible client message controls also showed an Edited marker. Edit history was not verified, so current wording is not assumed to be the initial send version. Use E11's original logs for send time/content.
3. Two tasks and assignees are visible. Deadlines and creation times use relative dates. Sunday/Saturday are directionally consistent with 11 and 17 October in the original analysis, but timezone settings and underlying dueTime were not checked.
4. Both still show Complete buttons. This does not verify reminders, owner response or business outcomes. The pending-decision item appears under Overdue. The single-person demo still does not validate responsibility through closure.
5. The current Qwen report-preparation conversation was opened, but no usable screenshot of the original contract write was obtained. A report-preparation screen was not presented as the original operation.

## Image integrity and public archive

Full JPEG originals for UI-01–UI-03 remain local. Published PNGs are lossless rectangular pixel excerpts. UI-04–UI-06 use JPEG screenshot bytes returned directly by the browser: UI-04/UI-05 show the top 1512 × 400 webpage region; UI-06 is the full business page. Nothing was redrawn, retouched, composited or relabeled. HTML embeds all six published images, excluding full DingTalk windows, unrelated conversation lists and a third unrelated to-do.

UI-01–UI-03 excerpt coordinates use the original's upper-left origin in pixels. Original JPEG and public PNG SHA-256 values are recorded as `source_sha256` and `sha256` in the [image manifest](html_src/operational_image_manifest.json). A PNG excerpt is not byte-identical to the complete original file.

| ID | Published excerpt | Original dimensions | Original rectangle x,y,w,h | Published dimensions |
| --- | --- | --- | --- | --- |
| UI-01 | [Contract ledger](assets/published/ui-01.png) | 1512 × 728 | [0, 0, 1512, 480] | 1512 × 480 |
| UI-02 | [Group briefing](assets/published/ui-02.png) | 3024 × 1898 | [1068, 112, 1900, 970] | 1900 × 970 |
| UI-03 | [Two to-dos](assets/published/ui-03.png) | 3024 × 1898 | [545, 120, 2448, 760] | 2448 × 760 |

For the additional captures, file hashes are those of the directly captured bytes; `capture_method` is `browser_screenshot`. JPEG is not claimed to be lossless encoding.

| ID | Direct capture | Region | Dimensions |
| --- | --- | --- | --- |
| UI-04 | [Project ledger](assets/published/ui-04.jpg) | Upper-left [0, 0, 1512, 400] | 1512 × 400 |
| UI-05 | [Risk tracking](assets/published/ui-05.jpg) | Upper-left [0, 0, 1512, 400] | 1512 × 400 |
| UI-06 | [Dashboard](assets/published/ui-06.jpg) | Complete business webpage | 1512 × 1081 |

Pages were viewed read-only in the already signed-in demo tenant 30, and the contract page was restored afterward. No baseline reset or business write occurred. The dashboard's 30-day count was not treated as a future-expiry count; the empty tracking list does not establish a historical deletion or root cause.

Images retain scenario-relevant display names, group names and demo business data; complete anonymization is not claimed. Full captures, additional task details, the briefing's lower section and old SVGs remain local and ignored. Some unused lower-section originals contain temporary text-selection highlighting.

No contracts were submitted, messages sent, to-dos modified or completed, or demonstrations rerun during this capture.
