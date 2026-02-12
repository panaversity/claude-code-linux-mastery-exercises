# Exercise 1.1 -- Agent Server Recon

**Build** -- Map a running agent server's filesystem and create a complete server inventory

## Goal

You have just been given SSH access to a server running 3 AI agents. Before making any changes, you need to map the entire server layout: where are the agent binaries, configs, logs, data directories, and systemd service files? Your deliverable is a `SERVER-MAP.md` that a new team member could use to understand every agent on this server without exploring the filesystem themselves.

## What You Have

- `agent-server/` -- A simulated server filesystem with 3 deployed agents (a weather-bot, a support-agent, and a data-processor). Files are spread across standard Linux locations (`/etc`, `/opt`, `/var`, `/home`, `/tmp`). No documentation exists. No handoff notes. Just a running system.

## Your Tasks

### Step 1: Launch Claude Code
Open a terminal in this exercise directory and run `claude` to start a Claude Code session.

### Step 2: Total File Count and Classification
Ask Claude Code to count all files in `agent-server/`, including hidden files. Get a breakdown by type: scripts, configs, logs, data files, service files, environment files, and other.

### Step 3: Find All Agent Binaries and Scripts
Search standard Linux binary locations for the agent executables. Check `opt/`, `usr/local/bin/`, `home/*/scripts/`, and anywhere else scripts might live.

### Step 4: Find All Configuration Files
Locate every configuration file across the server. Check `etc/`, home directories, `.env` files, YAML/JSON configs, and environment overrides.

### Step 5: Find All Log Locations
Map where each agent writes its logs. Check `var/log/`, any journald references in service files, and any other log paths mentioned in configs.

### Step 6: Find All Systemd Service Files
Locate the service definitions in `etc/systemd/system/`. Read each one to extract: the user that runs the agent, the binary path, restart policy, and any dependencies.

### Step 7: Find All Data Directories
Identify persistent data storage for each agent. Check `var/lib/`, `home/*/data/`, and any paths referenced in configs or pipeline definitions.

### Step 8: Map Agent-to-User Assignments
Determine which Linux user runs each agent by cross-referencing service files, home directories, and file ownership hints (bashrc files, crontabs, notes).

### Step 9: Create SERVER-MAP.md
Compile everything into a structured `SERVER-MAP.md` in this exercise directory. Include:
- Agent inventory (3 agents with name, purpose, language/runtime)
- File locations organized by category (binaries, configs, logs, data, services)
- User mapping (which user runs which agent)
- Port assignments (which port each agent listens on)
- At least 3 operational recommendations (security concerns, cleanup opportunities, monitoring gaps)

## Expected Results

A `SERVER-MAP.md` file that someone could read to fully understand every agent on this server. It should include:
- Complete inventory of all 3 agents with their tech stack
- Every file location categorized by purpose
- User-to-agent mapping with home directories
- Port assignments extracted from configs and service files
- Identification of temporary/cache files that could be cleaned
- Actionable recommendations for server hygiene

## Reflection

1. Which agent's files were hardest to find? What made them scattered across the filesystem?
2. How many different directories did you need to check? Could you write a single script to automate this server mapping?
3. What would happen if you started modifying configs without building this map first?
