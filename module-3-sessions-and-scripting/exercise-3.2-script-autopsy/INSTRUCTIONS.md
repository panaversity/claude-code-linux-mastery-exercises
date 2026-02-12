# Exercise 3.2 -- Script Autopsy

**Debug** -- Find and fix 5 bugs in a deployment script

## Goal

A teammate wrote a `deploy.sh` script to deploy an agent to a server. It "mostly works" on their machine but fails in CI and on fresh servers. The script has 5 bugs that are common bash scripting mistakes. Find and fix all 5.

## What You Have

- `deploy.sh` -- The buggy deployment script
- `agent-files/` -- The agent files that deploy.sh is supposed to deploy
- `error-log.txt` -- The error output from the last CI run
- `EXPECTED-BEHAVIOR.md` -- What the script SHOULD do at each step

## Your Tasks

### Step 1: Launch Claude Code
Open a terminal in this exercise directory and run `claude` to start a Claude Code session.

### Step 2: Understand Expected Behavior
Ask Claude Code to read `EXPECTED-BEHAVIOR.md` to understand what the script should do at each step. This is your source of truth for correct behavior.

### Step 3: Read the Buggy Script
Ask Claude Code to read `deploy.sh` carefully, noting anything suspicious. Do not fix anything yet -- just identify potential issues.

### Step 4: Analyze the Error Log
Ask Claude Code to read `error-log.txt` to see what actually happened when the script ran. Cross-reference each error with the script to locate the root cause.

### Step 5: Find Bug 1 -- Missing Safety Net
The script has no fail-fast mechanism. When one command fails, the script keeps running, making the damage worse. Find where this should be set and what the standard bash safety idiom is.

### Step 6: Find Bug 2 -- The Empty Variable Trap
One of the conditional checks will crash with a syntax error if the script is called without arguments. Find the unprotected variable expansion and fix it.

### Step 7: Find Bug 3 -- Comparing Apples to Oranges
The script compares a number using string comparison instead of numeric comparison. Find the incorrect operator and fix it.

### Step 8: Find Bug 4 -- Writing to Nowhere
The script tries to copy files into directories that do not exist yet. Find where the directory creation step was forgotten.

### Step 9: Find Bug 5 -- Wrong File Gets the Promotion
The script sets executable permissions on the wrong file. The config file gets chmod 755 (executable) while the actual program that needs to be executable gets nothing. Fix the permissions.

### Step 10: Write the Autopsy Report
Fix all 5 bugs in deploy.sh, then write `AUTOPSY-REPORT.md` documenting each bug: what it was, why it is dangerous, and the fix applied.

## Expected Results

- Fixed `deploy.sh` with all 5 bugs resolved
- `AUTOPSY-REPORT.md` with bug descriptions, danger assessments, and fixes

## Reflection

1. Which bug would cause the most damage in production? Why?
2. Would shellcheck have caught any of these? Which ones?
3. What is your personal checklist for writing safe bash scripts going forward?
