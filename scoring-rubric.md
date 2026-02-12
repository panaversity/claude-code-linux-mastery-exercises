# Linux Mastery: Scoring Rubric

## Per-Module Proficiency Criteria

What "Proficient" (score 3) looks like for each module. Use this as your target.

---

### Module 1: Filesystem Recon

**Proficient means**:
- Produced a complete SERVER-MAP.md covering all agent directories, configs, logs, processes, and network state
- Used `ps`, `ss`, `find`, `ls -la`, `systemctl` systematically -- not just `ls` once
- Identified which user runs each process and what ports are in use
- Fixed all misplaced files AND updated cross-references (config paths, service files)

**Below Proficient**: Missed hidden files, skipped process/port check, or left broken path references after moving files.

**Above Proficient**: Created a reusable server reconnaissance script (`server-recon.sh`) that auto-generates SERVER-MAP.md format.

---

### Module 2: Text & Pipes

**Proficient means**:
- Assembled all 3 config files correctly with no unresolved placeholders
- Pipeline commands documented and reproducible from CONFIG-PIPELINE.md
- Diagnosed the broken pipeline stage by testing each stage independently (not guessing)
- Fix was targeted to the exact broken stage, not a rewrite of the whole pipeline

**Below Proficient**: Left unresolved `{{PLACEHOLDER}}` tokens, or could not articulate which pipeline stage was broken and why.

**Above Proficient**: Added validation to each pipeline stage (e.g., checking output line count between stages) and error handling for missing input files.

---

### Module 3: Sessions & Scripting

**Proficient means**:
- tmux session has all 3 windows configured correctly (logs, metrics, deploy)
- `setup-monitoring.sh` recreates the session from scratch in one command
- Found and fixed all 5 bugs in the deploy script
- Each bug documented with: what it was, what it caused, and why the fix is correct

**Below Proficient**: tmux script only partially works (missing windows or panes), or fewer than 4 of 5 bugs found.

**Above Proficient**: Deploy script fix includes `set -euo pipefail`, trap-based cleanup, and logging that would make future debugging easier.

---

### Module 4: Logs & Security

**Proficient means**:
- HEALTH-REPORT.md contains actual computed metrics (error rate percentage, top 5 errors with counts, response time statistics)
- All metrics derived from verifiable commands (could re-run and get same numbers)
- SECURITY-REPORT.md covers SSH, permissions, services, firewall, and users
- Each security finding has a severity rating AND a specific remediation command

**Below Proficient**: Metrics are approximations ("lots of errors") instead of precise numbers, or security audit skips a major category (e.g., no firewall check).

**Above Proficient**: Created a `health-check.sh` and `security-audit.sh` that automate the analysis and can be run on any server.

---

### Module 5: Networking & Services

**Proficient means**:
- Service file includes: dedicated user, restart policy, resource limits, environment file, and correct install target
- Service starts, runs, and restarts automatically after `kill -9`
- All 3 startup failures diagnosed with specific root causes from `journalctl` output
- Each fix verified by successful service start AND sustained running (checked after 30 seconds)

**Below Proficient**: Service file missing restart policy or resource limits, or startup failure diagnosis was "I changed things until it worked" without identifying root cause.

**Above Proficient**: Service file includes hardening directives (`ProtectSystem`, `NoNewPrivileges`, `PrivateTmp`) and documentation explains each directive's purpose.

---

### Module 6: Debugging & Workflows

**Proficient means**:
- Cascade failure diagnosed layer-by-layer (nginx -> app -> database -> resources) with evidence from each layer
- INCIDENT-REPORT.md includes timeline, symptoms, investigation, root cause, fix, and prevention
- Deploy script handles the complete lifecycle with error checking at each stage
- Script includes rollback logic that restores previous state on failure

**Below Proficient**: Jumped to root cause without checking intermediate layers, or deploy script has no error handling (fails silently).

**Above Proficient**: Deploy script is idempotent (safe to run twice), includes dry-run mode, and DEPLOY-RUNBOOK.md covers failure scenarios with decision trees.

---

### Module 7: Capstones

**Proficient means**:
- All 7 framework steps followed in sequence with evidence of each
- Complete operational documentation (SERVER-MAP.md, SERVICE-SETUP.md, DEPLOY-RUNBOOK.md)
- Agent survives reboots, restarts on crash, and runs as non-root user
- Security basics in place (firewall, permissions, SSH hardened)

**Below Proficient**: Skipped steps (no backup, no documentation), agent runs as root, or no verification after deployment.

**Above Proficient**: Full automation pipeline, monitoring/alerting configured, security audit clean, and documentation is detailed enough for a new team member to operate independently.

---

## Overall Scoring

Calculate your average across the 6 rubric categories (Investigation, Operations Safety, Security Awareness, Debugging, Automation, Documentation).

| Average Score | Level | What It Means |
|:---:|---|---|
| 1.0 - 1.5 | **Beginner** | You can run commands but lack systematic process. Revisit chapter material before continuing. |
| 1.6 - 2.2 | **Developing** | You have the right instincts but skip steps under time pressure. Focus on building the habit of completing every framework step. |
| 2.3 - 3.0 | **Proficient** | You operate servers systematically and safely. Ready for production responsibilities with supervision. |
| 3.1 - 3.5 | **Advanced** | You build reusable systems, not one-time fixes. Ready for independent production operations. |
| 3.6 - 4.0 | **Expert** | You think in automation, security, and observability by default. Ready to design operational standards for a team. |

---

## Self-Assessment Questions

Answer these after completing each module. Honest self-assessment drives improvement.

### After Every Exercise

1. Did I investigate system state BEFORE making changes? If not, what did I miss?
2. Did I back up before every destructive operation? Was there a moment where I thought "I'll skip the backup, it's fine"?
3. Did I verify after every change with a specific command? Or did I assume success?
4. Could someone reproduce my work from my documentation alone?

### After Module Pairs (1-2, 3-4, 5-6)

5. Am I building the investigation reflex, or do I still jump to action?
6. Am I writing scripts for operations I repeat, or am I still typing commands manually?
7. Am I thinking about security during setup, or only when the exercise mentions it?

### After Capstones

8. If I were handed a new server tomorrow with a new agent to deploy, could I do it end-to-end without referring back to the exercises?
9. What is my weakest skill area? (Investigation, safety, security, debugging, automation, documentation) What specific practice would strengthen it?
10. What would my SERVER-MAP.md look like for a server I manage at work or for a personal project? Would I be confident showing it to a senior engineer?
