# Linux Operations Exercise Guide

## Three Core Skills

Every exercise practices one or more of these skills:

1. **Server Navigation** — Finding your way around a Linux filesystem and reading what the system tells you
2. **Infrastructure Setup** — Building production-ready deployments from directory structures through systemd services
3. **Systematic Diagnosis** — Finding root causes using the LNPS method instead of blindly restarting

## Exercise Types

- **Build exercises** — You create something from scratch (directory structure, service file, deployment spec)
- **Debug exercises** — You diagnose and fix something broken (permission errors, failed services, cascading failures)

Debug exercises develop different skills than Build exercises. Building teaches creation; debugging teaches reading system output critically and tracing errors to root causes.

## Tier Progression

### Tier 1: Foundation (Exercises 1.1 – 1.4)

**Covers:** Lessons 1-2 (SSH, filesystem navigation, command output, permissions)

Starter prompts are provided for each exercise. Focus on reading output carefully before acting.

| Exercise | Type | Focus |
|----------|------|-------|
| 1.1 Server Orientation | Build | Explore an unfamiliar server systematically |
| 1.2 Mystery Server | Debug | Find and diagnose an abandoned agent |
| 1.3 Reading the Room | Build | Interpret health metrics and make go/no-go decision |
| 1.4 Permission Puzzle | Debug | Decode permission strings and fix access errors |

### Tier 2: Operations (Exercises 2.1 – 2.6)

**Covers:** Lessons 3-5 (directory setup, .env files, systemd, security hardening)

Less scaffolding than Tier 1. You decide the approach.

| Exercise | Type | Focus |
|----------|------|-------|
| 2.1 Agent Home Setup | Build | Create complete project directory structure |
| 2.2 Missing Pieces | Debug | Fix 5 problems in an intern's broken setup |
| 2.3 Service From Scratch | Build | Write a complete systemd unit file |
| 2.4 Service Won't Start | Debug | Find 3 simultaneous root causes |
| 2.5 Lock It Down | Build | Security hardening: user, permissions, SSH |
| 2.6 Overprivileged Agent | Debug | Full security audit with 5 findings |

### Tier 3: Diagnosis (Exercises 3.1 – 3.4)

**Covers:** Lessons 6-7 (LNPS method, deployment specs)

No scaffolding. You design the entire investigation.

| Exercise | Type | Focus |
|----------|------|-------|
| 3.1 Silent Agent | Debug | Agent appears healthy but produces no output |
| 3.2 Cascading Failure | Debug | 3 agents down — find the single root cause |
| 3.3 Deployment Spec | Build | Write a complete spec for a new agent |
| 3.4 Spec vs Reality | Debug | Find gaps between deployment spec and server state |

## Assessment Rubric

For each exercise, evaluate yourself on:

| Criteria | Beginner (1) | Developing (2) | Proficient (3) | Advanced (4) |
|----------|:---:|:---:|:---:|:---:|
| **Investigation Quality** | Runs one command | Checks multiple areas | Systematic investigation covering all areas | Discovers hidden issues beyond the obvious |
| **Operational Safety** | Makes changes without checking state | Checks some state first | Full investigation before any change | Documents state, backs up, then changes |
| **Security Awareness** | Ignores permission/access issues | Fixes obvious security problems | Identifies and prioritizes all security issues | Prevents recurrence with automation |
| **Debugging Methodology** | Guesses and restarts | Reads some logs | Follows LNPS systematically | Traces root cause AND identifies prevention |
| **Documentation** | No deliverable | Basic notes | Complete report with evidence | Reusable template with verification steps |

## Self-Assessment Questions

After completing each tier, ask yourself:

**After Tier 1:**
- Can I decode a Linux permission string (e.g., `drwxr-x---`) without looking it up?
- Can I interpret `df -h`, `free -h`, and `ps aux` output and explain what the numbers mean?

**After Tier 2:**
- Can I set up a complete agent deployment (directories, .env, systemd, permissions) from memory?
- Do I instinctively check security (permissions, user, SSH) during every setup?

**After Tier 3:**
- When a service fails, do I follow LNPS or do I restart first and hope?
- Can I write a deployment spec detailed enough for someone else to follow without questions?
