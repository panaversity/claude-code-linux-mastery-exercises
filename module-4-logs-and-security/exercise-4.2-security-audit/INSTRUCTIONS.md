# Exercise 4.2 -- Security Audit Report

**Apply** -- Audit a server configuration for security violations and write a remediation plan

## Goal

You have been asked to security-audit a server before it goes to production. The previous admin left it in a "works but insecure" state. Your job is to examine every configuration file, find every security violation, classify its severity, and write both a report and a remediation script. This is the kind of audit you would run before any real deployment.

## What You Have

- `insecure-server/` -- A simulated server filesystem with intentionally insecure configurations. It mirrors the structure of a real Linux server with etc/, opt/, home/, var/, and root/ directories containing SSH config, application config, systemd services, firewall rules, environment files, scripts, logs, and admin artifacts.

## Your Tasks

### Step 1: Launch Claude Code
Open a terminal in this exercise directory and run `claude` to start a Claude Code session.

### Step 2: Check SSH Configuration
Examine `insecure-server/etc/ssh/sshd_config` for insecure settings. Look for root login permissions, password authentication, default ports, and protocol versions.

### Step 3: Check File Permissions
Look for world-writable or world-readable sensitive files. Check permissions on .env files, config files, log files, and backup scripts. Use `ls -la` recursively.

### Step 4: Check for Exposed Secrets
Search all files for API keys, passwords, tokens, and other secrets that should not be stored in plaintext. Check .env files, scripts, config files, and bash history.

### Step 5: Check Service Configuration
Examine the systemd service file. Is the application running as root? Does it have a dedicated service user? Are capabilities restricted?

### Step 6: Check Firewall Rules
Examine the iptables rules. Are there any rules at all? Is the default policy permissive? Are unnecessary ports open?

### Step 7: Check for Information Leakage
Look for files that expose internal infrastructure details: deployment notes, bash history with sensitive commands, logs with session tokens.

### Step 8: Classify Each Finding
Assign a severity to every finding: CRITICAL, HIGH, MEDIUM, or LOW. Use this guide:
- **CRITICAL**: Direct path to system compromise (root SSH, exposed secrets with admin access)
- **HIGH**: Significant risk requiring immediate action (running as root, world-writable configs)
- **MEDIUM**: Should be fixed before production (no firewall, history with secrets, excessive log permissions)
- **LOW**: Best practice violations (info leakage, missing log rotation)

### Step 9: Write SECURITY-REPORT.md
Create a structured security report with: finding description, severity, file path, evidence (the specific insecure line or permission), and the exact remediation command to fix it.

### Step 10: Write fix-security.sh
Create a remediation script that applies all fixes. The script should be idempotent (safe to run multiple times) and include comments explaining each fix.

## Expected Results

- A `SECURITY-REPORT.md` with at least 8 findings, each containing:
  - Finding title and severity (CRITICAL/HIGH/MEDIUM/LOW)
  - File path where the issue was found
  - Evidence (the exact insecure configuration or permission)
  - Remediation command
- A `fix-security.sh` script that applies all remediations

## Reflection

1. Which finding would you fix first and why?
2. How many of these issues would be prevented by a deployment checklist?
3. What automated tools exist for Linux security auditing (e.g., Lynis, OpenSCAP)?
