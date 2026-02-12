# Exercise 3.1 -- Tmux Control Center

**Build** -- Create a persistent monitoring environment for agent operations

## Goal

You manage 3 agents on a production server. You need a tmux session that survives SSH disconnections with dedicated windows for: (1) live agent logs, (2) system metrics, and (3) a deployment shell. Your deliverable is a `setup-monitoring.sh` script that recreates this layout with one command.

## What You Have

- `sample-logs/` -- Sample log files for 3 agents to tail
- `metrics-commands.txt` -- The monitoring commands to run in the metrics window
- `reference-layout.txt` -- ASCII diagram of what the final tmux layout should look like

## Your Tasks

### Step 1: Launch Claude Code
Open a terminal in this exercise directory and run `claude` to start a Claude Code session.

### Step 2: Understand the Target Layout
Ask Claude Code to read `reference-layout.txt` and explain the tmux session structure you need to build: how many windows, how many panes, and what runs in each.

### Step 3: Create the Tmux Session Manually
Ask Claude Code to create a tmux session named "agent-ops" with 3 windows. Work through this step by step so you understand each tmux command.

### Step 4: Set Up the Logs Window
In Window 0 ("logs"): set up split panes tailing each agent's log file. The top half should be split vertically with `weather-bot.log` on the left and `support-agent.log` on the right. The bottom half should show `data-processor.log` across the full width.

### Step 5: Set Up the Metrics Window
In Window 1 ("metrics"): run the system monitoring commands from `metrics-commands.txt`. This window should show a live-updating view of CPU, memory, and disk usage.

### Step 6: Set Up the Deploy Window
In Window 2 ("deploy"): a clean shell ready for deployment commands. No commands running, just a prompt.

### Step 7: Test Session Persistence
Detach from the session and reattach to verify it persists. This simulates what happens when your SSH connection drops.

### Step 8: Write the Automation Script
Write `setup-monitoring.sh` that recreates this entire layout automatically. The script should be idempotent -- if the session already exists, kill it and recreate from scratch.

### Step 9: Test the Script
Kill the existing tmux session, run your script, and verify the result matches `reference-layout.txt`. The script should work on a fresh system where no tmux session exists yet.

## Expected Results

- `setup-monitoring.sh` -- Executable script that creates the complete tmux session
- Running the script produces a tmux session matching `reference-layout.txt`
- Script is idempotent (kills existing session before recreating)

## Reflection

1. What happens to your monitoring when your SSH connection drops? How does tmux solve this?
2. Could you extend this script to also set up environment variables per window?
3. How would you modify this for a server with 10 agents instead of 3?
