# Claude Code: Linux Mastery Exercises

**Master Linux System Administration Through Agent Deployment Scenarios**

Practice exercises for Chapter 10: Linux Mastery for Digital FTEs. These exercises take you from navigating server filesystems through scripting deployments, securing servers, managing systemd services, and debugging production failures -- building the operational skills that separate "it works on my laptop" from "it runs in production."

## Package Structure

```
claude-code-linux-mastery-exercises/
├── EXERCISE-GUIDE.md                              # Full guide with rubrics and framework
├── README.md                                      # This file
├── scoring-rubric.md                              # Per-module scoring criteria
├── module-1-filesystem-recon/
│   ├── exercise-1.1-agent-server-recon/           (Build: Map a running agent server)
│   └── exercise-1.2-misplaced-deployment/         (Debug: Fix files in wrong directories)
├── module-2-text-and-pipes/
│   ├── exercise-2.1-config-pipeline/              (Build: Assemble configs from fragments)
│   └── exercise-2.2-broken-pipeline/              (Debug: Find the corrupted pipe stage)
├── module-3-sessions-and-scripting/
│   ├── exercise-3.1-tmux-control-center/          (Build: Create monitoring session)
│   └── exercise-3.2-script-autopsy/               (Debug: Fix 5 bugs in deploy script)
├── module-4-logs-and-security/
│   ├── exercise-4.1-agent-log-forensics/          (Build: Extract metrics from logs)
│   └── exercise-4.2-security-audit/               (Apply: Audit server for violations)
├── module-5-networking-and-services/
│   ├── exercise-5.1-systemd-from-scratch/         (Build: Write complete service file)
│   └── exercise-5.2-why-wont-it-start/            (Debug: Diagnose 3 startup failures)
├── module-6-debugging-and-workflows/
│   ├── exercise-6.1-cascade-failure/              (Build: Trace HTTP 502 to root cause)
│   └── exercise-6.2-deploy-pipeline/              (Build: Chain all skills into deploy script)
└── module-7-capstones/
    ├── capstone-A-full-production-deployment/      (End-to-end spec-first deployment)
    ├── capstone-B-server-rescue/                   (Fix 7 simultaneous server problems)
    └── capstone-C-your-own-agent/                  (Deploy your own project)
```

## Getting Started

### Prerequisites

- **Claude Code** (required): All exercises involve real Linux system operations in the terminal. Install Claude Code following the instructions at https://docs.anthropic.com/en/docs/claude-code.
- **Linux/WSL2 environment** (required): Exercises require a Linux system or Windows Subsystem for Linux 2. macOS works for most exercises but some systemd and networking exercises require a full Linux environment.
- **Root or sudo access** (recommended): Several exercises involve service management, user creation, and firewall configuration that require elevated privileges.

### Setup

1. Download or clone this repository
2. Open a terminal in the repository root
3. Launch Claude Code: `claude`
4. Start with Module 1 and work sequentially

### Recommended Order

Work through modules in order. Each module builds on skills from the previous one.

| Module | Focus | Time |
|--------|-------|------|
| Module 1: Filesystem Recon | Navigate and fix agent server layouts | 30-60 min |
| Module 2: Text & Pipes | Config assembly and pipeline debugging | 30-60 min |
| Module 3: Sessions & Scripting | tmux monitoring and bash script debugging | 45-90 min |
| Module 4: Logs & Security | Log analysis and security auditing | 45-90 min |
| Module 5: Networking & Services | systemd service files and startup debugging | 45-90 min |
| Module 6: Debugging & Workflows | Production troubleshooting and deployment pipelines | 45-90 min |
| Module 7: Capstones | Integration projects (pick one+) | 2-4 hrs each |

## Linux Operations Framework

Every Linux operation in this course follows a 7-step framework. Memorize this. It becomes second nature.

1. **Investigate** -- What is the current state? Check before assuming. Run `ps`, `ss`, `systemctl`, `df`, `ls` before changing anything.
2. **Plan** -- Design your approach before executing. Write down what you intend to change and what the expected outcome is.
3. **Backup** -- Safety net before destructive changes. Copy configs before editing. Snapshot before upgrading. No exceptions.
4. **Execute** -- One change at a time. Never combine multiple changes into a single operation. If something breaks, you need to know which change caused it.
5. **Verify** -- Did it work? Check with specific commands. `systemctl status`, `curl localhost`, `journalctl -u service`. Trust output, not assumptions.
6. **Document** -- Record what you did and why. Future-you will not remember why you changed that firewall rule at 2 AM.
7. **Automate** -- If you did it twice, script it. Manual repetition is where human error lives.

You will practice each step individually in Modules 1-6, then chain them together in the capstones.

## Assessment

See EXERCISE-GUIDE.md for the full assessment rubric covering:
- Investigation Quality
- Operations Safety
- Security Awareness
- Debugging Methodology
- Automation Quality
- Documentation

See scoring-rubric.md for per-module scoring criteria and self-assessment questions.

## Tips

- **Read INSTRUCTIONS.md first** in each exercise before opening Claude Code
- **Never skip the investigation step** -- even when you think you know what is wrong
- **Treat every exercise like a production server** -- build the habit of safety-first operations even when nothing is at stake
- **Reflect honestly** -- the reflection questions are where real learning happens
- **Keep your deliverables** -- SERVER-MAP.md, SECURITY-REPORT.md, deploy scripts, and similar outputs are your portfolio of operational skills
