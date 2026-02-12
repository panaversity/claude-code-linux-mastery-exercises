# Exercise 5.1 -- Systemd Service from Scratch

**Build** -- Write a complete production-grade systemd service file

## Goal

You have an agent application (a FastAPI app) that currently runs manually with `python main.py`. Your job: turn it into a proper systemd service that starts on boot, restarts on crash, runs as a dedicated non-root user, has resource limits, and logs to journald.

## What You Have

- `agent-app/` -- A simple FastAPI agent application with `main.py`, `requirements.txt`, and `.env.example`
- `REQUIREMENTS.md` -- Exact requirements for the service file (user, paths, restart policy, resource limits, security hardening)
- `service-template.txt` -- A bare-bones template with TODO comments explaining each section you need to fill in

## Your Tasks

### Step 1: Launch Claude Code
Open a terminal in this exercise directory and run `claude` to start a Claude Code session.

### Step 2: Understand the Application
Ask Claude Code to read the agent application in `agent-app/` to understand what it needs: which port it binds to, what environment variables it expects, what its working directory should be, and how it starts.

### Step 3: Read the Requirements
Have Claude Code read `REQUIREMENTS.md` to understand every requirement for the service file: the service user, working directory, start command, environment file path, restart policy, resource limits, and security hardening.

### Step 4: Fill in the Service Template
Work through `service-template.txt` section by section with Claude Code, replacing every TODO with the correct directive:
- **[Unit]** section: Description, After dependencies, Documentation URL
- **[Service]** section: User, WorkingDirectory, ExecStart, Type, EnvironmentFile, Restart policy, Resource limits, Security hardening, Logging
- **[Install]** section: WantedBy target

### Step 5: Add Restart Protection
Make sure the service file includes restart storm protection:
- `RestartSec=5` -- wait 5 seconds between restart attempts
- `StartLimitBurst=5` -- maximum 5 restarts allowed
- `StartLimitIntervalSec=60` -- within a 60-second window

### Step 6: Add Resource Limits
Add directives that prevent a runaway agent from killing the server:
- `MemoryMax=512M` -- hard memory ceiling
- `CPUQuota=200%` -- maximum of 2 CPU cores

### Step 7: Write Verification Commands
Create a `VERIFY-COMMANDS.md` file documenting every command needed to manage and verify the service:
- How to check the service file for syntax errors
- How to start, stop, restart, and enable the service
- How to check status and read logs
- How to verify resource limits are applied

### Step 8: Write the Setup Script
Create a `setup-service.sh` script that automates the full installation: creates the dedicated user, copies application files, creates the virtual environment, installs the service file, enables it, and starts it.

## Expected Results

- `agent-app.service` -- A complete, production-grade systemd service file with all sections filled in correctly
- `VERIFY-COMMANDS.md` -- All commands needed to manage, verify, and troubleshoot the service
- `setup-service.sh` -- A one-command setup script that provisions everything from scratch

## Reflection

1. Why `Restart=on-failure` instead of `Restart=always`? What is the practical difference when your agent exits cleanly with code 0?
2. What happens if your agent crashes 6 times in 60 seconds? Walk through the math with `StartLimitBurst=5` and `StartLimitIntervalSec=60`.
3. Why is `MemoryMax` important for an AI agent that loads models? What happens to the process when it exceeds the limit?
