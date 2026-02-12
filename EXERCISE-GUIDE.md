# Linux Mastery for Digital FTEs: Exercise Guide

## A Hands-On Guide to Linux System Administration for AI Agent Deployment

**By Panaversity -- Learn by Doing, Not by Reading**

---

## How This Guide Works

Every module in this guide follows a consistent pattern: **X.1 is a Build exercise** where you apply skills to create something from requirements, and **X.2 is a Debug or Audit exercise** where you diagnose problems in a broken system. Build exercises develop your ability to execute Linux operations correctly. Debug exercises develop your ability to think systematically about production failures -- a skill that matters even more, because in professional operations work, you spend more time diagnosing broken systems than building new ones.

Three core skills run through every exercise. First, **server investigation**: understanding a system's state before changing it. You will learn to check processes, ports, disk space, permissions, and logs before touching a single config file. Second, **systematic operations**: following procedures that prevent mistakes. You will internalize the discipline of backup-first, one-change-at-a-time, verify-after-every-step. Third, **production thinking**: treating security, reliability, and automation as defaults rather than afterthoughts. You will build the habits that keep servers running at 3 AM without human intervention.

**Tool guidance**: Use **Claude Code** for all exercises. These exercises involve real Linux system operations -- navigating filesystems, editing configs, managing processes, reading logs, writing scripts, and configuring services in a terminal environment. Claude Code is purpose-built for this kind of work. You can optionally use **Cowork** for planning-heavy exercises (like designing a deployment pipeline), but Claude Code is strongly preferred since even planning exercises benefit from testing plans against real system state immediately.

Every exercise includes starter files that simulate realistic server scenarios. You will work with agent deployment directories, broken config files, corrupted deploy scripts, messy log files, misconfigured services, and production failure scenarios. The files are designed to contain the same kinds of edge cases and messiness you encounter on real production servers -- because that is where the learning happens.

---

## Linux Operations Framework

Every Linux operation in this course follows a 7-step framework. Memorize this. It becomes second nature.

### Step 1: Investigate
**What is the current state? Check before assuming.**

Before you change anything, understand what you are working with. Use `ps aux`, `ss -tlnp`, `systemctl status`, `df -h`, `free -m`, `ls -la`, and `journalctl` to build a complete picture of the system. Check what processes are running. Check what ports are open. Check disk and memory usage. This step takes 2-5 minutes and prevents hours of wrong-direction debugging.

### Step 2: Plan
**Design your approach before executing.**

Write down what you intend to change, what the expected outcome is, and how you will verify success. For destructive operations, plan your rollback path. A plan written in 30 seconds saves 30 minutes of undo work. State your plan to Claude Code before executing -- it will catch obvious gaps.

### Step 3: Backup
**Safety net before destructive changes.**

Copy config files before editing: `cp nginx.conf nginx.conf.bak.$(date +%Y%m%d)`. Snapshot before upgrading packages. Export databases before migrations. A backup you have not verified is not a backup -- it is a hope. Check that the backup file exists, is not empty, and contains what you expect.

### Step 4: Execute
**One change at a time.**

Never combine multiple changes into a single operation. If you change the nginx config AND the firewall rules AND the service user simultaneously, and the service breaks, you have no idea which change caused it. Make one change. Verify. Make the next change. Verify. This feels slower but is faster overall because you never have to untangle compound failures.

### Step 5: Verify
**Did it work? Check with specific commands.**

After every change, verify with a command that proves correctness. `systemctl status` shows if a service is running. `curl localhost:8080` shows if an endpoint responds. `journalctl -u service --since "1 min ago"` shows if new errors appeared. Do not assume success -- verify it.

### Step 6: Document
**Record what you did and why.**

Write a brief note: what you changed, why you changed it, and what the state was before. Save this in a runbook, a commit message, or a comment in the config file. Future-you debugging this server at 2 AM will be grateful. The most common phrase in incident response is "who changed this and why?"

### Step 7: Automate
**If you did it twice, script it.**

Manual repetition is where human error lives. If you deployed an agent by running 15 commands, write a `deploy-agent.sh` that runs those commands. If you check server health by running 5 checks, write a `health-check.sh`. Scripts are documentation that also executes.

---

## Assessment Rubric

Use this rubric to self-assess your work on each exercise. Be honest -- the point is growth, not grades.

| Criteria | Beginner (1) | Developing (2) | Proficient (3) | Advanced (4) |
|----------|:---:|:---:|:---:|:---:|
| **Investigation** | Skipped investigation, changed files blindly | Some checks before acting, missed key system state | Systematic state verification before every change | Built reusable investigation scripts and checklists |
| **Operations Safety** | No backups, large multi-step changes at once | Some safety measures, few verification checkpoints | Backup-first, atomic operations, verified each step | Scripted operations with automatic rollback on failure |
| **Security Awareness** | Ran everything as root, no firewall, open permissions | Basic permission awareness, some access controls | Least privilege, SSH keys, firewall rules, proper ownership | Security as architectural default with audit trails |
| **Debugging** | Random changes hoping to fix the problem | Some log reading, trial and error | Systematic layer-by-layer diagnosis using logs and state | Automated health checks, monitoring, and alerting |
| **Automation** | All manual, repeated operations by hand | Some scripts, partial automation | Complete deployment scripts with error handling | Idempotent, tested automation pipelines with rollback |
| **Documentation** | Nothing documented | Some notes about what was done | Full server maps, audit reports, runbooks | Operational playbooks with troubleshooting decision trees |

**Scoring guide:**
- 6-10 points: Revisit the chapter material and retry the exercise
- 11-15 points: Solid foundation -- move to the next module
- 16-20 points: Strong execution -- try the capstones
- 21-24 points: Ready to manage production Linux servers

---

## Module 1: Filesystem Recon

> **Core Principle**: "Your agents live on Linux servers. Before you can manage them, you must navigate their home."
>
> **Covers**: Filesystem hierarchy, navigation, directory structure, file types and permissions

Before you can deploy agents, configure services, or debug failures, you need to know your way around a Linux server. Module 1 builds the navigation habit -- the discipline of understanding a server's filesystem layout before making changes. This is the difference between an operator who can fix problems and an operator who creates new ones. Operators who skip investigation end up editing the wrong config file, overwriting production data, or deploying to the wrong directory.

---

### Exercise 1.1 -- Agent Server Recon (Build)

**Time**: 30-45 minutes

**The Problem**: You have SSH access to a server running 3 AI agents (a chatbot, a code reviewer, and a document processor). Nobody gave you a server map. The previous admin left no documentation. You need to find where everything lives -- configs, logs, binaries, data directories, virtual environments, and any running processes -- before you can maintain these agents.

The server follows no standard layout. Some agents are installed in `/opt`, one is in `/home/agent-user`, config files are scattered between `/etc` and each agent's own directory, and logs may be going to `/var/log`, `journalctl`, or a local `logs/` directory. You need to map all of it.

**Your Task**: Use Claude Code to systematically explore the server and produce a `SERVER-MAP.md` that documents:

- All agent installation directories (binaries, scripts, source code)
- Configuration file locations (with notes on what each config controls)
- Log file locations (where each agent writes logs)
- Data directories (databases, caches, uploaded files)
- Running processes (PIDs, ports, resource usage)
- User accounts and permissions (which user runs each agent)
- Service management (systemd units, cron jobs, or manual startup scripts)
- Network state (listening ports, connected services)

**Starter Prompt** (vague -- see what happens):
> "Show me what's running on this server."

**Better Prompt** (specific -- compare the difference):
> "I just got access to a server running 3 AI agents with zero documentation. Before I touch anything, I need a complete server map. Check running processes with ps and ports with ss, find agent installations under /opt, /home, and /usr/local, locate all config files, find where logs are going, identify which user runs each agent, check for systemd services and cron jobs, and document everything in SERVER-MAP.md organized by agent."

**The Principle at Work**: Investigation before action. You are building a complete picture of the server before changing anything. Every item in SERVER-MAP.md is something you could have accidentally broken if you had skipped this step.

**What You Will Learn**:
1. Linux servers have a standard filesystem hierarchy (`/etc` for configs, `/var/log` for logs, `/opt` for third-party software) but real servers deviate -- you must explore, not assume
2. `ps aux`, `ss -tlnp`, `systemctl list-units`, and `find` are your primary investigation tools -- they reveal the server's actual state, not its intended state
3. A server map is a living document -- you will update it every time you discover something new, and it pays for itself the first time you need to find a config file at 3 AM

**Reflection Questions**:
1. What surprised you about the server layout? Were any agents installed in unexpected locations?
2. How long did the investigation take? How much time would it have saved if the previous admin had left a SERVER-MAP.md?
3. If a new team member joined tomorrow, could they maintain these agents using only your SERVER-MAP.md?

---

### Exercise 1.2 -- The Misplaced Deployment (Debug)

**Time**: 20-30 minutes

**The Problem**: A junior admin deployed a new agent but put files in the wrong locations. The agent binary is in `/tmp` instead of `/opt/agent-name`. Log configuration points to the admin's home directory instead of `/var/log/agent-name`. The config file has hardcoded paths to the wrong directories. The systemd service file references paths that do not exist. The agent will not start, and the error messages are cryptic because every path is wrong.

Your job is forensic: find every misplaced file, move it to the correct location, fix all path references, and get the agent running.

**Your Task**:
1. Read the intended deployment layout from `DEPLOYMENT-SPEC.md`
2. Investigate the current state -- where are files actually located?
3. For each misplaced file, document: where it is, where it should be, and what references need updating
4. Move files to correct locations using `mv`, `cp`, and `ln -s` as appropriate
5. Update all path references in config files and service definitions
6. Verify the agent starts correctly
7. Create a `FIX-LOG.md` documenting every correction

**The Principle at Work**: Investigation before action, again. You could have started moving files immediately, but without understanding the full picture first, you would have missed cross-references and broken things further.

**What You Will Learn**:
1. File paths in Linux are interconnected -- moving a binary without updating the systemd service file, the config file, AND the log path creates a cascade of failures
2. `mv` vs `cp` vs `ln -s` each have appropriate use cases -- symlinks can bridge the gap between where a file is expected and where it lives
3. Systematic fix-and-verify (fix one path, test, fix the next) prevents compound errors

**Reflection Questions**:
1. How many path references did you need to update? Was it more than you expected?
2. Did you find any paths that were technically wrong but still worked? (For example, a relative path that happened to resolve correctly from the current directory)
3. What deployment checklist would prevent this kind of misplacement in the future?

---

## Module 2: Text & Pipes

> **Core Principle**: "The pipe operator is the most powerful composition tool in computing. Master it and you can transform any data."
>
> **Covers**: Text processing, pipes, redirection, grep, sed, awk, config file management

Linux administration is text processing. Config files are text. Logs are text. Command output is text. The pipe operator lets you chain simple tools into powerful data transformations -- `cat | grep | sort | uniq -c | sort -rn` takes a log file and produces a ranked frequency table in one line. Module 2 builds fluency with pipes and text processing, the skill that makes everything else in Linux faster.

---

### Exercise 2.1 -- Config Pipeline (Build)

**Time**: 30-45 minutes

**The Problem**: You are deploying an agent that requires 3 configuration files: a main application config, a database connection config, and a logging config. But the configs are not ready -- they exist as fragments scattered across a `config-fragments/` directory. Some fragments overlap. Some contain environment-specific values that need to be substituted. Some are templates with placeholder tokens like `{{DB_HOST}}` and `{{LOG_LEVEL}}`.

You need to assemble 3 complete, valid config files from these fragments using pipes, `cat`, `grep`, `sed`, and output redirection.

**Your Task**:
1. Survey the `config-fragments/` directory -- what fragments exist and what do they contain?
2. Determine which fragments belong to which config file
3. Assemble each config file using pipes and redirection (`cat`, `grep`, `sed` for substitution)
4. Substitute all placeholder tokens with actual values from `environment.env`
5. Validate the assembled configs (check for syntax, missing values, duplicate keys)
6. Document your pipeline commands in `CONFIG-PIPELINE.md` so someone else can reproduce the assembly

**Starter Prompt** (vague):
> "Put together the config files from the fragments."

**Better Prompt** (specific):
> "I need to assemble 3 config files from fragments in config-fragments/. First survey all fragments, then determine which belong to each config. Use cat and pipes to combine them, sed to substitute placeholders from environment.env, and redirect output to final config files. Validate each assembled config for completeness and save the pipeline commands in CONFIG-PIPELINE.md."

**The Principle at Work**: Plan before execute. Understanding which fragments belong to which config before running any commands prevents you from assembling corrupt config files.

**What You Will Learn**:
1. Pipes compose simple tools into powerful transformations -- `cat fragment1.conf fragment2.conf | sed 's/{{DB_HOST}}/localhost/' > app.conf` is a complete config assembly pipeline
2. Config assembly from fragments is a real production pattern -- Docker secrets, Kubernetes configmaps, and CI/CD systems all assemble configs from pieces
3. Documented pipelines are reproducible -- your CONFIG-PIPELINE.md means anyone can regenerate these configs for a new environment

**Reflection Questions**:
1. How many pipe stages did your longest pipeline have? Could you break it into simpler steps without losing correctness?
2. What happened when you forgot to substitute a placeholder? How did you catch it?
3. How would you adapt this pipeline for a different environment (staging vs production)?

---

### Exercise 2.2 -- Broken Pipeline Diagnosis (Debug)

**Time**: 25-35 minutes

**The Problem**: A colleague wrote a 4-stage pipeline to process agent log data:

```bash
cat raw-logs.txt | grep "ERROR" | sed 's/timestamp: //' | awk '{print $3}' > error-summary.txt
```

The pipeline is supposed to extract a clean list of error codes from the raw logs. But the output in `error-summary.txt` is wrong -- some entries are garbled, some are missing, and some contain fields that should have been stripped. The pipeline has a bug in one of the 4 stages, and your job is to find which stage corrupts the data.

**Your Task**:
1. Read the expected output format from `EXPECTED-OUTPUT.md`
2. Run the pipeline one stage at a time, examining the output after each stage
3. Identify which stage produces unexpected output
4. Diagnose the root cause (wrong regex? wrong field number? wrong grep pattern?)
5. Fix the broken stage
6. Verify the corrected pipeline produces the expected output
7. Document your diagnosis in `PIPELINE-DIAGNOSIS.md`

**The Principle at Work**: Systematic debugging. You could have stared at the full pipeline trying to spot the bug. Instead, you isolate each stage and test it independently -- the same technique used to debug any multi-step process.

**What You Will Learn**:
1. Debugging pipelines means testing each stage in isolation -- pipe to `head` or redirect to a temp file after each stage to inspect intermediate output
2. Common pipe bugs: `grep` pattern too broad or too narrow, `sed` regex that matches unintended text, `awk` field number off-by-one, missing quotes around patterns with spaces
3. Stage-by-stage diagnosis is the same skill used for debugging microservice chains, CI/CD pipelines, and data processing workflows

**Reflection Questions**:
1. Which stage was broken? How long did it take you to find it by testing each stage independently vs. how long would it have taken by staring at the full pipeline?
2. What would have made this pipeline easier to debug? (Hint: intermediate output files, comments, variable names for patterns)
3. How would you add error checking to each stage so the pipeline fails loudly instead of producing silent corruption?

---

## Module 3: Sessions & Scripting

> **Core Principle**: "Your terminal session is ephemeral. Your agents are not. Bridge the gap with persistent sessions and automation scripts."
>
> **Covers**: tmux, bash scripting, environment management, process persistence

A terminal session ends when you close your laptop. A production agent must keep running. Module 3 bridges this gap with two skills: persistent terminal sessions (tmux) for real-time monitoring, and bash scripts for automation. Together they give you the ability to manage long-running agents without being physically present at the terminal.

---

### Exercise 3.1 -- Tmux Control Center (Build)

**Time**: 30-45 minutes

**The Problem**: You manage 3 agents on a server. You need to monitor their logs simultaneously, check metrics periodically, and have a shell ready for deployments. Currently you open 5 separate SSH sessions, lose track of which is which, and when your connection drops, everything disappears. You need a persistent monitoring setup that survives disconnections.

**Your Task**:
1. Design a tmux session layout with 3 windows:
   - **Window 1 (Logs)**: Split into 3 panes, each tailing a different agent's log file
   - **Window 2 (Metrics)**: Runs a monitoring command showing CPU, memory, and disk usage, refreshing every 10 seconds
   - **Window 3 (Deploy)**: A clean shell in the deployment directory, with environment variables loaded
2. Create the session manually first, verifying each window and pane works
3. Script the entire setup in `setup-monitoring.sh` so it can be recreated with a single command
4. Test the script by killing the session and re-running the script
5. Document the key bindings and workflow in `TMUX-GUIDE.md`

**The Principle at Work**: Automate. You built the monitoring setup once manually, then scripted it. Now you can recreate it in seconds after any disconnection.

**What You Will Learn**:
1. tmux sessions persist independently of your SSH connection -- you can detach, disconnect, reconnect, and reattach without losing any running processes or log output
2. Scripting tmux setup converts a 5-minute manual process into a 1-second command -- and eliminates the risk of forgetting a window or misconfiguring a pane
3. A monitoring control center is standard operational practice -- every production team has some version of this

**Reflection Questions**:
1. What happened when you detached from tmux and reattached? Was all output preserved?
2. How would you extend this setup for a server with 10 agents instead of 3?
3. What monitoring information is missing from this setup that you would want during an incident?

---

### Exercise 3.2 -- Script Autopsy (Debug)

**Time**: 30-45 minutes

**The Problem**: A deploy script `deploy-agent.sh` was written hastily during an incident. It mostly works, but it has 5 bugs that cause intermittent failures. Sometimes it deploys successfully. Sometimes it deploys to the wrong directory. Sometimes it leaves the old version running alongside the new one. Sometimes it silently fails and reports success.

The script is 60-80 lines of bash. Your job: find and fix all 5 bugs.

**Your Task**:
1. Read the script completely before changing anything
2. Read `DEPLOY-SPEC.md` to understand what the script is supposed to do
3. Identify all 5 bugs -- for each one, document:
   - Line number and the buggy code
   - What the bug causes (wrong behavior)
   - Why it is a bug (what should happen instead)
   - Your fix
4. Fix each bug
5. Test the fixed script
6. Create `AUTOPSY-REPORT.md` documenting all 5 bugs and fixes

**The Principle at Work**: Investigation before action. Reading the entire script and the spec first gives you context that makes each bug obvious. Fixing bugs in isolation without understanding the full script creates new bugs.

**What You Will Learn**:
1. Common bash script bugs: unquoted variables (`$DIR` vs `"$DIR"`), missing error checking (`set -e`), wrong comparison operators (`-eq` vs `==`), race conditions between stop and start, hardcoded paths that assume a specific working directory
2. A deploy script that silently fails is worse than one that crashes -- at least a crash tells you something went wrong
3. Reading the full script before fixing anything prevents "whack-a-mole" debugging where fixing one bug creates another

**Reflection Questions**:
1. Which bug was the most dangerous? Which one could cause data loss or downtime?
2. What patterns would you add to ANY deploy script to prevent these classes of bugs? (Hint: `set -euo pipefail`, quoting, explicit error messages)
3. Could any of these bugs have been caught by a linter or static analysis tool?

---

## Module 4: Logs & Security

> **Core Principle**: "Production means reading logs, not writing code. And production means security is architectural, not an afterthought."
>
> **Covers**: Log analysis, grep/sed/awk for metrics, security hardening, auditing, permissions

Two skills define a production operator: reading logs fluently and thinking about security by default. Module 4 builds both. Log analysis teaches you to extract meaning from thousands of lines of text -- turning raw logs into error rates, response times, and root causes. Security auditing teaches you to see a server through an attacker's eyes -- finding the open doors that should be closed.

---

### Exercise 4.1 -- Agent Log Forensics (Build)

**Time**: 35-50 minutes

**The Problem**: Your agent has been running for 24 hours and has generated 500+ lines of log output. Management wants a health report: What is the error rate? What are the most common errors? What is the average response time? Are there any patterns (errors clustering at specific times)?

You cannot read 500 lines manually. You need to extract metrics programmatically using `grep`, `sed`, `awk`, `sort`, and `uniq`.

**Your Task**:
1. Survey the log file -- how many lines, what format, what fields are available?
2. Extract error rate: count ERROR lines vs total lines, calculate percentage
3. Find top 5 most common error messages (deduplicate and rank)
4. Calculate response time statistics: min, max, average, 95th percentile
5. Identify time-based patterns: do errors cluster in any time window?
6. Produce a `HEALTH-REPORT.md` with all findings, generated entirely from command-line tools

**Starter Prompt** (vague):
> "Analyze the agent logs."

**Better Prompt** (specific):
> "Process agent.log (500+ lines) to produce a health report. Calculate: error rate as percentage of total lines, top 5 error messages ranked by frequency, response time min/max/avg, and any time-based error clustering. Use grep, awk, sort, uniq to extract metrics. Output everything to HEALTH-REPORT.md with the actual numbers."

**The Principle at Work**: Investigate with precision. You are extracting specific metrics from raw data, not just skimming logs. Every number in your report is backed by a command you can re-run.

**What You Will Learn**:
1. `grep -c "ERROR"` counts errors, `awk '{sum+=$NF} END {print sum/NR}'` computes averages, `sort | uniq -c | sort -rn | head -5` finds the top 5 -- these are the building blocks of log analysis
2. Log analysis is a daily production skill -- you will do this during every incident, every performance review, and every capacity planning session
3. Command-line log analysis is faster than any dashboard for ad-hoc queries -- dashboards show predefined views, but command-line tools answer any question

**Reflection Questions**:
1. What was the error rate? Would you consider this healthy, concerning, or critical?
2. Did you find any time-based patterns? What might explain clustering of errors at specific times?
3. Which log format made analysis easier or harder? What format would you request for future agents?

---

### Exercise 4.2 -- Security Audit (Apply)

**Time**: 40-60 minutes

**The Problem**: You have been asked to audit a server for security violations before it goes into production. The server was set up quickly during a prototype phase, and "we'll harden it later" was the plan. Later is now.

The server has common security problems: root SSH access may be enabled, files may have world-writable permissions, services may be running as root, firewall may be unconfigured, and sensitive files may have overly permissive ownership.

**Your Task**:
1. Check SSH configuration for security violations
2. Find all world-writable files and directories
3. Check which services run as root that should not
4. Audit file permissions on sensitive files (configs, keys, data)
5. Check firewall status and rules
6. Review user accounts for unnecessary access
7. Check for common security misconfigurations (open ports, default credentials, unpatched services)
8. Produce a `SECURITY-REPORT.md` with findings ranked by severity (Critical, High, Medium, Low)
9. For each finding, include a remediation command

**The Principle at Work**: Security is investigation. You are systematically checking every attack surface, not just the obvious ones. The checklist approach ensures you do not miss the one open door that an attacker will find.

**What You Will Learn**:
1. Security auditing follows a checklist -- SSH, permissions, services, firewall, users, ports -- and skipping any item leaves a gap
2. `find / -perm -o+w`, `ss -tlnp`, `cat /etc/ssh/sshd_config`, `iptables -L` are your core audit tools
3. Every finding needs a remediation -- discovering a problem without fixing it (or documenting the fix) is incomplete work

**Reflection Questions**:
1. How many findings did you discover? Which severity had the most items?
2. Which finding would you fix first and why? What is the risk of leaving each one open?
3. How would you automate this audit so it runs weekly and alerts on new violations?

---

## Module 5: Networking & Services

> **Core Principle**: "systemd is the difference between 'my agent runs on my laptop' and 'my agent runs in production.'"
>
> **Covers**: systemd service files, networking, ports, process management, service lifecycle

An agent that runs when you start it manually is a demo. An agent that starts on boot, restarts on crash, logs to journalctl, and runs as a dedicated user is production infrastructure. Module 5 teaches you to bridge that gap with systemd -- the service manager that turns scripts into reliable services.

---

### Exercise 5.1 -- Systemd from Scratch (Build)

**Time**: 35-50 minutes

**The Problem**: You have a Python agent that runs with `python3 /opt/myagent/main.py`. It works great when you run it manually. But it does not survive server reboots, it does not restart when it crashes, it runs as root (security risk), it has no resource limits (could consume all memory), and its logs are scattered to stdout.

You need to write a complete systemd service file that makes this agent production-ready.

**Your Task**:
1. Write a `.service` file with all required sections: `[Unit]`, `[Service]`, `[Install]`
2. Configure a dedicated service user with minimal permissions
3. Set restart policy: automatic restart on failure with backoff
4. Add resource limits: memory ceiling, CPU quota
5. Configure environment variables from an environment file
6. Set up proper logging integration with journalctl
7. Install, enable, start, and verify the service
8. Document the complete service setup in `SERVICE-SETUP.md`

**The Principle at Work**: Plan and execute systematically. Each section of the service file serves a specific purpose. You are not guessing at directives -- you are designing a service specification.

**What You Will Learn**:
1. A systemd service file is a specification, not a script -- it declares WHAT should happen (restart on failure) and lets systemd handle HOW
2. Production services need: dedicated user (security), restart policy (reliability), resource limits (stability), and log integration (observability)
3. `systemctl enable` vs `systemctl start`: enable makes it survive reboots, start makes it run now -- you almost always want both

**Reflection Questions**:
1. What happens when you `kill -9` your agent process? Does systemd restart it? How quickly?
2. What happens when the agent exceeds the memory limit you set? Is that the behavior you want?
3. How would you modify this service file for an agent that needs to run 3 worker processes?

---

### Exercise 5.2 -- Why Won't It Start? (Debug)

**Time**: 30-45 minutes

**The Problem**: Three different agents have service files that fail to start. Each has a different problem. The error messages from `systemctl status` and `journalctl` are your only clues. You must diagnose and fix all 3 startup failures.

The failures are realistic: one has a permission problem, one has a dependency ordering problem, and one has a configuration error that only manifests at runtime.

**Your Task**:
For each of the 3 failing services:
1. Check `systemctl status service-name` for the failure state
2. Read `journalctl -u service-name` for error details
3. Diagnose the root cause
4. Fix the problem
5. Verify the service starts and stays running
6. Document the diagnosis in `STARTUP-FIXES.md`

**The Principle at Work**: Systematic diagnosis. `systemctl status` tells you WHAT failed. `journalctl` tells you WHY. You follow the evidence, not your intuition.

**What You Will Learn**:
1. `systemctl status` shows the symptom (exit code, state), `journalctl -u service` shows the cause (error message, stack trace) -- always check both
2. Common startup failures: wrong file permissions (service user cannot read config), missing dependencies (database not ready when agent starts), wrong ExecStart path (typo or missing interpreter)
3. Service debugging follows the same investigate-diagnose-fix-verify cycle as every other Linux operation

**Reflection Questions**:
1. Which failure was hardest to diagnose? What made the error message misleading?
2. How would you prevent each failure from occurring in the first place? (Validation before deployment? Integration tests? Dependency checks?)
3. What monitoring would you add to detect these failures automatically rather than discovering them manually?

---

## Module 6: Debugging & Workflows

> **Core Principle**: "When production breaks, panic is your enemy. Systematic diagnosis is your friend."
>
> **Covers**: Production debugging, multi-layer diagnosis, deployment automation, end-to-end workflows

Everything breaks in production. The question is not whether but when -- and whether you have the skills to diagnose the failure systematically or resort to randomly restarting services. Module 6 builds production debugging skills through realistic failure scenarios, then caps it with a deployment pipeline that chains every skill from the course.

---

### Exercise 6.1 -- Cascade Failure (Build)

**Time**: 40-60 minutes

**The Problem**: Your agent's API endpoint returns HTTP 502 Bad Gateway. Users are reporting errors. The agent was working fine yesterday. You need to find the root cause.

The system has multiple layers: nginx (reverse proxy) -> agent application (Python) -> database (PostgreSQL). The 502 could be caused by ANY layer: nginx misconfiguration, agent crash, database connection failure, disk full, port conflict, or something else entirely.

**Your Task**:
1. Start from the outside in: check nginx status and logs
2. Check the agent application: is the process running? Is it listening on the expected port?
3. Check the database: is it running? Can the agent connect?
4. Check system resources: disk space, memory, open file limits
5. Identify the root cause and fix it
6. Verify the full stack is working end-to-end
7. Write an `INCIDENT-REPORT.md` with: timeline, symptoms, investigation steps, root cause, fix, and prevention measures

**The Principle at Work**: Layer-by-layer diagnosis. You do not guess which layer is broken. You check each layer systematically, starting from the user-facing edge and working inward until you find the failure point.

**What You Will Learn**:
1. HTTP 502 means "the reverse proxy could not reach the backend" -- it narrows the problem to the backend application or its dependencies, not to nginx itself
2. Layer-by-layer diagnosis (network -> proxy -> application -> database -> resources) is the standard approach to production debugging
3. An incident report is not bureaucracy -- it is how you prevent the same failure from happening again and how you transfer debugging knowledge to your team

**Reflection Questions**:
1. How many layers did you check before finding the root cause? Did any layer show misleading symptoms?
2. What monitoring would have alerted you to this problem BEFORE users reported errors?
3. How would you add health checks that detect this specific failure automatically?

---

### Exercise 6.2 -- Deploy Pipeline (Build)

**Time**: 45-60 minutes

**The Problem**: You deploy agents manually by running 12-15 commands in sequence: stop the old version, back up configs, pull new code, install dependencies, run migrations, update configs, start the new version, verify health, update nginx, reload nginx, check logs for errors. Every time you deploy, you forget a step or run them in the wrong order.

You need a `deploy-agent.sh` script that chains all these steps together, with error handling, rollback, and logging.

**Your Task**:
1. Document the complete deployment sequence in order
2. Write `deploy-agent.sh` implementing every step with:
   - `set -euo pipefail` for strict error handling
   - Logging of each step to a deploy log file
   - Verification after critical steps (health check after start)
   - Rollback on failure (restore backup configs, restart old version)
   - Command-line arguments for agent name and version
3. Test the script with a simulated deployment
4. Create `DEPLOY-RUNBOOK.md` documenting how to use the script, what it does at each step, and how to handle failures

**The Principle at Work**: Automate. You are converting 15 manual steps into a single reliable command. The script is not just automation -- it is codified operational knowledge.

**What You Will Learn**:
1. A deploy script is the highest-value automation you can write -- it is the operation you repeat most often and where mistakes are most costly
2. Error handling in bash (`set -euo pipefail`, trap for cleanup, explicit exit codes) is the difference between a script that fails safely and one that fails silently
3. Rollback logic is the hardest part of deployment scripts -- you must think about what to undo at each step if the next step fails

**Reflection Questions**:
1. What was the hardest part of the deploy script to implement? Was it the happy path or the error handling?
2. Is your script idempotent -- can you run it twice safely? What happens if you run it again after a successful deployment?
3. What would you add to make this script suitable for a team of 5 operators who all deploy independently?

---

## Module 7: Capstone Projects

> Choose one (or more). This is where everything comes together.
>
> Capstones are not graded exercises -- they are integration challenges that combine every skill from Modules 1-6.

---

### Capstone A -- Full Production Deployment

**Time**: 2-4 hours

**The Challenge**: Take an agent from "code in a repository" to "running in production" using the complete Linux operations workflow:

1. **Investigate**: Survey the target server -- resources, existing services, available ports
2. **Plan**: Write a deployment specification (user, directory layout, service file, firewall rules, log rotation)
3. **Backup**: Snapshot any existing state on the server
4. **Execute**: Deploy step by step -- create user, set up directories, install agent, write service file, configure nginx, set up firewall
5. **Verify**: Health check every layer, check logs, confirm external access
6. **Document**: Write complete server documentation (SERVER-MAP.md, SERVICE-SETUP.md, DEPLOY-RUNBOOK.md)
7. **Automate**: Convert your deployment into a reusable script

Do this in a single continuous Claude Code session. Document each step as you go.

**What You Will Learn**:
1. How all 7 steps chain together naturally -- each step's output becomes the next step's input
2. A production deployment requires ALL the skills from this course simultaneously -- filesystem layout, config management, scripting, security, services, and debugging
3. The documentation you produce is as valuable as the deployment itself -- it is what enables someone else to maintain, update, and troubleshoot the agent

**Deliverable**: A running agent plus complete operational documentation.

---

### Capstone B -- Server Rescue

**Time**: 2-4 hours

**The Challenge**: A server has 7 simultaneous problems. Services are down. Configs are corrupt. Permissions are wrong. Disk is filling up. A cron job is running wild. Firewall rules were flushed. An unauthorized SSH key was added.

You must systematically triage, diagnose, and fix all 7 problems. Order matters -- some fixes depend on others. You cannot just restart everything and hope for the best.

Read `SERVER-STATE.md` for the initial symptoms, then investigate from there.

**What You Will Learn**:
1. Triage is the first skill in incident response -- fixing the disk space problem before the permissions problem, because you cannot edit files on a full disk
2. Simultaneous failures often share a root cause -- finding the connection between problems is the advanced skill
3. Under pressure, systematic process beats clever intuition -- the 7-step framework is your lifeline when everything is broken

**Deliverable**: A working server plus an `INCIDENT-REPORT.md` documenting all 7 problems, your triage order, and the fixes.

---

### Capstone C -- Your Own Agent

**Time**: 2-4 hours

**The Challenge**: Deploy YOUR OWN project (a Python API, a Node.js app, a Go binary, or any long-running process) to a Linux server using everything you learned.

**Rules**:
1. START WITH INVESTIGATION. Survey your server before changing anything.
2. Follow all 7 framework steps. No shortcuts.
3. Your agent must survive reboots (systemd), have proper permissions (dedicated user), have resource limits, log to journalctl, and be accessible through a reverse proxy.
4. Document everything in operational runbooks.
5. The goal is not just "it runs." The goal is "anyone on my team could maintain this."

**What You Will Learn**:
1. Real projects have edge cases that exercises cannot simulate -- your actual application has dependencies, environment variables, and startup quirks that are unique to your codebase
2. The deployment process reveals which operational skills matter most for YOUR specific project -- maybe networking is the hard part, or maybe it is log management
3. The operational documentation you produce is genuinely useful beyond this course -- you just created the runbook for your real infrastructure

**Deliverable**: A production-deployed agent plus complete operational documentation (SERVER-MAP.md, SERVICE-SETUP.md, DEPLOY-RUNBOOK.md, SECURITY-REPORT.md).

---

## Quick Reference: Every Linux Operation Session

Before EVERY exercise, check these boxes:

- [ ] **Investigate first**: What is the current system state? (`ps`, `ss`, `df`, `systemctl status`)
- [ ] **Back up before changing**: Config files copied? State documented?
- [ ] **One change at a time**: Am I combining changes that should be separate?
- [ ] **Verify after every step**: Did I check with a specific command, or did I assume it worked?
- [ ] **Document as you go**: Could someone else understand what I did from my notes?
- [ ] **Security by default**: Am I running as root when I should not be? Are permissions minimal?
- [ ] **Automate repetition**: Am I typing the same command sequence for the third time?

---

## Assessment Summary

After completing exercises, score yourself on the rubric:

| Criteria | Beginner (1) | Developing (2) | Proficient (3) | Advanced (4) |
|----------|:---:|:---:|:---:|:---:|
| **Investigation** | Skipped investigation, changed files blindly | Some checks, missed key state | Systematic state verification before every change | Built reusable investigation scripts |
| **Operations Safety** | No backups, large multi-step changes | Some safety, few checkpoints | Backup-first, atomic operations, verified each | Scripted operations with rollback |
| **Security Awareness** | Ran everything as root | Basic permission awareness | Least privilege, SSH keys, firewall | Security as architectural default |
| **Debugging** | Random changes hoping to fix | Some log reading, guesswork | Systematic layer-by-layer diagnosis | Automated health checks and monitoring |
| **Automation** | All manual, repeat operations | Some scripts, partial automation | Complete deployment scripts | Idempotent, tested automation pipelines |
| **Documentation** | Nothing documented | Some notes | Full server maps, audit reports | Runbooks and operational playbooks |

**Your journey**: Linux system administration is the foundation of every production deployment. The professional who can take a bare server and produce a secure, documented, automated agent deployment has a skill that is in perpetual demand. Every agent you build, every service you deploy, every incident you respond to -- the 7-step framework applies. Master it here, use it everywhere.
