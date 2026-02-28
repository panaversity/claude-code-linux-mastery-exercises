# Exercise 3.1 — The Silent Agent (Debug)

## Scenario

Ali checks his competitor-tracker Monday morning. The systemd service shows "active (running)" — green light, everything looks fine. But the daily report email never arrived. The dashboard shows no new data since Friday. The agent is running but not doing anything. This is the most dangerous kind of failure: silent.

## Your Task

Apply the LNPS method to the files in `broken-state/`. Follow the order strictly — even if you think you know the answer after step 1:

1. **Logs** — Read `journalctl-output.txt`. What is the last meaningful log entry?
2. **Network** — Read `network-check.txt`. Can the agent reach the database?
3. **Process** — Read `process-state.txt`. Is the agent process alive? What is it doing?
4. **System** — Read `system-resources.txt`. Are disk/memory/CPU okay?

Create a `ROOT-CAUSE-ANALYSIS.md` documenting each LNPS step and what it revealed.

## Success Criteria

- [ ] Followed LNPS in order (did not skip to a guess)
- [ ] Found the repeating "Waiting for database connection..." in logs
- [ ] Found that port 5432 is unreachable (firewall change)
- [ ] Noted the process is alive but stuck in retry loop
- [ ] Confirmed system resources are fine
- [ ] Explained why restarting the agent would NOT fix this

## Reflection

Why is a "silent failure" more dangerous than a crash? If the agent had crashed instead of retrying silently, would Ali have noticed sooner?
