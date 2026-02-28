# Exercise 3.2 — The Cascading Failure (Debug)

## Scenario

Ali wakes up to three alerts at once. The competitor-tracker is down. The social-media-monitor is down. The report-generator is down. Three agents, all failed within the same hour. Ali's instinct says "the server is broken" but each agent shows a different error message. He needs to find the single root cause.

## Your Task

Start with the system-level check (read `system-check.txt` first), then investigate each agent's logs. Trace all three failures back to the single root cause.

1. Read `system-check.txt` — check disk, memory, load
2. Read `competitor-tracker-logs.txt` — what error does it show?
3. Read `social-monitor-logs.txt` — what error does it show?
4. Read `report-generator-logs.txt` — what error does it show?
5. Read `disk-usage.txt` — what filled the disk?

Create a `CASCADE-ANALYSIS.md` documenting: the root cause, how it caused three different symptoms, what filled the disk, and how to prevent recurrence.

## Success Criteria

- [ ] Started with system-level check (not individual agents)
- [ ] Identified root cause: disk 100% full
- [ ] Connected each agent's error to the full disk
- [ ] Found what filled the disk (unrotated log files)
- [ ] Proposed prevention: log rotation + disk monitoring

## Reflection

Ali saw three different error messages from three different agents. How did starting with System (the S in LNPS) lead him to the single root cause faster than investigating each agent separately?
