# Exercise 5.2 -- Why Won't It Start?

**Debug** -- Diagnose 3 service startup failures from logs and config

## Goal

The `support-agent` service fails to start. The admin says "it was working yesterday." You have the service file, the journal logs from the failed startup attempts, and the current server state. Your job: find the 3 separate issues preventing startup, explain each one, and provide the exact fix commands.

## What You Have

- `support-agent.service` -- The current service file (has issues baked in from recent server changes)
- `journalctl-output.txt` -- Journal logs from three separate failed startup attempts, showing different errors each time
- `server-state.txt` -- Current state of the server: users, filesystem, ports, and recent change history
- `previous-working-config.txt` -- What the configuration looked like when the service was running correctly on Feb 8

## Your Tasks

### Step 1: Launch Claude Code
Open a terminal in this exercise directory and run `claude` to start a Claude Code session.

### Step 2: Read the Journal Logs
Ask Claude Code to read `journalctl-output.txt` and identify the distinct error patterns. The logs contain three separate startup attempts, each failing for a different reason. Pay attention to the exit status codes -- they are diagnostic.

### Step 3: Read the Service File
Have Claude Code read `support-agent.service` and note every directive. This is the file that systemd is currently using.

### Step 4: Compare with Previous Working Config
Ask Claude Code to read `previous-working-config.txt` and compare it against the current service file. The notes in this file explain what changed and when.

### Step 5: Read the Server State
Have Claude Code read `server-state.txt` to understand what the server looks like right now: which users exist, what is on the filesystem, and what is listening on which ports.

### Step 6: Diagnose Issue 1 -- The Missing User
The first startup attempt fails with exit status 217/USER. Cross-reference the journal log with server-state.txt to confirm the user is missing, and find evidence of when and why it was deleted.

### Step 7: Diagnose Issue 2 -- The Wrong Path
After the user is recreated, the second attempt fails with exit status 203/EXEC. Cross-reference the ExecStart path in the service file with what actually exists on the filesystem.

### Step 8: Diagnose Issue 3 -- The Port Conflict
After the path is fixed, the third attempt gets further -- the application starts but immediately dies because the port is already in use. Use the server state to identify what process holds the port.

### Step 9: Write the Diagnosis
Create a `DIAGNOSIS.md` file documenting all 3 issues. For each issue, include: the symptom (what the log says), the root cause (what actually went wrong and when), and the exact fix commands.

### Step 10: Fix the Service File
Create a corrected version of the service file that addresses the path issue. (The user and port issues require server-side commands, not service file changes.)

## Expected Results

- `DIAGNOSIS.md` -- A structured document with symptom, cause, and fix for each of the 3 issues
- `support-agent-fixed.service` -- The corrected service file with the right ExecStart path

## Reflection

1. In what order should you fix these 3 issues? Does the order matter, and why?
2. What single command gives you the most diagnostic information when a service fails to start?
3. How would you prevent each of these 3 issues from recurring? Think about automation, monitoring, and process.
