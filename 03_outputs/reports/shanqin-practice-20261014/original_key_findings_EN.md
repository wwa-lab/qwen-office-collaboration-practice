# Key Findings and Management Implications — Historical Draft

**English** · [简体中文原文](核心发现与管理启示-2026-10-14.md)

> **Historical working draft M3.** The following translates its original claims; it is not the current accepted assessment. Assertions of a complete workflow, enforced controls, a fixed day-seven issue and sustained unattended operation were later qualified or corrected. Read the [current formal report](report/04_final_report_EN.md) and [evidence matrix](report/02_evidence_matrix_EN.md). Practitioner: Leo Zhang.

Original note: working paper two. Each finding cites the practice inventory's identifiers and original records; no unmeasured efficiency or cost conclusions are intended.

## Finding 1: value lies in connecting input, judgment, action and review in one conversation

- **Finding in the draft:** the change was not merely document reading or messaging. Group/document input → extraction/aggregation → ledger action → group/to-do collaboration → next-day review occurred in one AI conversation, without manual transfer across systems.
- **Evidence cited:** S2–S8, seven scenarios in approximately 45 minutes on 10 October, 15:27–16:12; six group messages across document sharing, correction, briefing and inspection; cron logs showing activity after the demo.
- **Management implication proposed:** evaluate overall workflow improvement rather than scoring isolated functions. Existing tools already cover summaries and translation; connected workflows should be the pilot's focus.

## Finding 2: where AI stops matters more for enterprise usability than a capability list

- **Finding in the draft:** the valuable pauses were waiting for confirmation before contract entry, keeping customer decisions private, reading documents/messages back before declaring success, and correcting a blocked mention format without leaving discarded messages. It claimed no unconfirmed ledger writes in the main demo.
- **Evidence cited:** S3's confirmation gate and no ledger entry before 16:12; S6 distribution rules; S7 rejection/resend; the recap's three gates.
- **Management implication proposed:** acceptance for bank AI office tools should include write-confirmation gates, distribution rules and readback-based completion, as versioned skills/rules rather than verbal expectations.

## Finding 3: skills distribute procedures—and their defects

- **Finding in the draft:** seven business workflows, wording boundaries and card layouts were packaged for installation, with the first scenario working in about ten minutes and no repeated individual tuning. It also claimed a day-seven rule defect caused a missed item and was corrected.
- **Evidence cited:** S1 ZIP-to-seven-skill installation; S2–S8 scripted execution; S8 prompt update and schedule-status check.
- **Management implication proposed:** govern scenario skills as organizational assets through versioning, boundary tests, release approval and named maintenance/repair ownership.

## Finding 4: structured instructions and current data reduce retelling and stale-definition risk

- **Finding in the draft:** “have the owner explain within a week” became project, requirement, deadline and owner, consistently represented across three systems. Overdue/near-due values used the execution date and current returns rather than August–September script dates; the 14 October report showed 135/36/34/29 overdue days.
- **Evidence cited:** S5 parsing and cross-system consistency; S4/S8 date calculations and increasing day counts; treatment of the script/date mismatch.
- **Management implication proposed:** replace verbal relaying with structured records, and use current system data plus current date as the reference. The method is not tied to a product.

## Finding 5: unattended automation has operating prerequisites

- **Finding in the draft:** inspections continued for four days, but two were missed because the desktop was offline/asleep. No report appeared on those days and the errors were visible in run logs; delivery resumed on day three.
- **Evidence cited:** five cron records—two missed (`too_late`, `sleep`), two scheduled `ok`, one manual-demo `ok`; no reports on 11/12 October, reports on 13/14 October.
- **Management implication proposed:** before production reminders, define the execution host, missed-run alerts, catch-up and support owner. Treat the gap between desktop-resident operation and enterprise requirements as an evaluation topic, not a general product-defect conclusion.

## The draft's three management takeaways

1. **Claimed verified:** AI, messaging and business systems can complete a management workflow in the demo environment, with confirmation, distribution and readback controls.
2. **Claimed verified:** workflows can be packaged and run unattended; availability, organization boundaries and rule quality determine reliability.
3. **Unverified even in the draft:** suitability for real bank systems/data, quantified efficiency, and fit with enterprise scheduling/permissions. No measured data supported positive or negative conclusions on those three matters.

The “verified” labels above belong to the historical draft and are superseded where the current report qualifies them.
