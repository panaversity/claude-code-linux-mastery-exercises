# Capstone B -- Server Rescue

**Integration** -- Fix 7 simultaneous server problems under pressure

## Goal

A production server with 2 running agents has gone critical. Multiple things are broken simultaneously. Customer-facing services are down, disk space is nearly exhausted, and there are signs of unauthorized access. Your job: triage, prioritize, and fix all 7 issues systematically.

This capstone tests your ability to investigate under pressure, prioritize by severity, and apply fixes from across the entire chapter -- systemd, logs, cron, SSH, disk management, and process control.

## What You Have

- `sick-server/` -- Simulated server state with all the problems baked into its files
- `incident-report.txt` -- The alert that triggered this investigation

## Your Tasks

### Step 1: Read the Incident Report

Start by reading `incident-report.txt`. This is your only starting information -- everything else you must discover through investigation.

### Step 2: Systematic Investigation

Open Claude Code and systematically investigate the server state. Check these areas:

- **Services**: Read the systemd service files in `sick-server/etc/systemd/system/`
- **Disk**: Look at log file sizes, cache files, any unexpectedly large files
- **Security**: Check SSH configuration, read auth logs for suspicious activity
- **Scheduled jobs**: Read cron configurations for errors
- **Processes**: Check for zombie or orphaned processes
- **Logs**: Read application and system logs for errors and warnings
- **Admin history**: Check what the admin was doing recently

Do NOT skip areas just because the incident report does not mention them. Some problems are hidden.

### Step 3: Discover All 7 Issues

As you investigate, catalog each issue you find. For each one, document:

- What the problem is
- Where you found evidence of it (which file, which line)
- What the impact is (service down, data risk, degraded performance, minor)

### Step 4: Triage by Severity

Assign a priority to each issue:

| Priority | Meaning | Action |
|----------|---------|--------|
| P0 | Service down or data loss imminent | Fix immediately |
| P1 | Security breach or data risk | Fix within the hour |
| P2 | Degraded performance | Fix today |
| P3 | Minor issue | Fix this week |

### Step 5: Fix Each Issue

Work through fixes in priority order. For each fix:

1. Edit the relevant file in `sick-server/` to apply the fix
2. Document what you changed and why
3. Note how you would verify the fix on a real server

### Step 6: Write INCIDENT-POSTMORTEM.md

Create a postmortem document with:

- **Timeline**: When each problem likely started (use log timestamps and bash history)
- **Root causes**: What caused each of the 7 issues
- **Fixes applied**: Exactly what you changed for each issue
- **Verification steps**: How to confirm each fix worked
- **Prevention**: What monitoring or process would catch each issue before it becomes critical

### Step 7: Write PREVENTION-CHECKLIST.md

Create a monitoring checklist that would catch each of the 7 issues before they become incidents. For each check, specify:

- What to monitor
- What threshold triggers an alert
- How often to check
- What the response procedure is

## Estimated Time

2-3 hours

## Deliverables

- `INCIDENT-POSTMORTEM.md` -- Full postmortem with all 7 issues documented
- Fixed files in `sick-server/` -- All 7 issues corrected
- `PREVENTION-CHECKLIST.md` -- Monitoring checks that would catch each issue early

## Hints

If you get stuck, here are the areas where the 7 problems live (but NOT what the problems are):

1. Something in a systemd service file is causing excessive resource consumption
2. Something is consuming way too much disk space (check two locations)
3. Something in the SSH configuration should not be enabled on a production server
4. Something in a cron job has a syntax error
5. Something in the process list should not be there
6. Something is causing slow response times (related to a very large file)
7. Something is missing from the log management configuration

## Reflection

1. How did you decide which issue to fix first? Would a different order have been better?
2. Which issue was hardest to discover? What investigation technique found it?
3. How many of these issues could have been prevented by a single well-configured monitoring system?
4. What is the relationship between issue 1 (restart behavior) and issue 5 (zombie processes)? Could one have caused the other?
