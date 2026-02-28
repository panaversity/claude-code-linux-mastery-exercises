# Exercise 3.4 — Spec vs Reality (Debug)

## Scenario

Ali wrote a deployment spec and handed it to Claude Code. The deployment completed "without errors." But when he runs the verification checklist from the spec, three checks fail. The spec said one thing; the server shows another.

## Your Task

Compare `deployment-spec.md` (what was planned) against `actual-state.txt` (what exists on the server). Find all THREE gaps:

1. Compare the spec's User= setting against what `systemctl show` reports
2. Compare the spec's .env permissions against what `ls -la` shows
3. Compare the spec's boot startup setting against what `systemctl is-enabled` reports

For each gap, document: what the spec says, what reality shows, WHY the gap exists, and the fix.

## Success Criteria

- [ ] Found gap 1: service runs as root (daemon-reload never ran after unit file edit)
- [ ] Found gap 2: .env has 644 permissions (chmod applied to wrong file)
- [ ] Found gap 3: service not enabled for boot (systemctl enable was skipped)
- [ ] Explained the cause of each gap (not just the symptom)
- [ ] Provided fix commands for all three
- [ ] Re-verified all checks pass after fixes

## Reflection

The deployment "completed without errors" but three checks failed. What does this tell you about the difference between "no errors" and "correct"? Why is the verification checklist the most important part of the spec?
