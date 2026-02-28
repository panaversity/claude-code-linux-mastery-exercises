# Claude Code: Linux Operations Exercises

**Practice exercises for Chapter 11: Linux Mastery for Digital FTEs**

14 hands-on exercises across 3 tiers that take you from navigating server filesystems to diagnosing cascading production failures. Every exercise puts you in Ali's shoes — you direct Claude Code, read the output, and make decisions.

## Package Structure

```
claude-code-linux-mastery-exercises/
├── EXERCISE-GUIDE.md                                # Full guide with rubrics and framework
├── README.md                                        # This file
├── tier-1-foundation/                               # Lessons 1-2: Navigation and reading
│   ├── exercise-1.1-server-orientation/             (Build: Explore a new server)
│   ├── exercise-1.2-mystery-server/                 (Debug: Find and diagnose an abandoned agent)
│   ├── exercise-1.3-reading-the-room/               (Build: Interpret server health output)
│   └── exercise-1.4-permission-puzzle/              (Debug: Diagnose permission errors)
├── tier-2-operations/                               # Lessons 3-5: Building infrastructure
│   ├── exercise-2.1-agent-home-setup/               (Build: Create project directory structure)
│   ├── exercise-2.2-missing-pieces/                 (Debug: Fix an intern's broken setup)
│   ├── exercise-2.3-service-from-scratch/           (Build: Write a systemd service)
│   ├── exercise-2.4-service-wont-start/             (Debug: Find 3 root causes in a failed service)
│   ├── exercise-2.5-lock-it-down/                   (Build: Harden a deployment's security)
│   └── exercise-2.6-overprivileged-agent/           (Debug: Security audit with 5 findings)
└── tier-3-diagnosis/                                # Lessons 6-7: Systematic debugging
    ├── exercise-3.1-silent-agent/                   (Debug: Agent running but not working)
    ├── exercise-3.2-cascading-failure/              (Debug: 3 agents down, 1 root cause)
    ├── exercise-3.3-deployment-spec/                (Build: Write a complete deployment spec)
    └── exercise-3.4-spec-vs-reality/               (Debug: Find gaps between spec and server)
```

## Getting Started

### Prerequisites

- **Claude Code** (required): All exercises involve directing Claude Code to investigate and fix Linux scenarios. Install following the instructions at https://docs.anthropic.com/en/docs/claude-code.
- **No live server required**: Exercises use simulated server output files. You practice reading and interpreting output, then directing Claude Code — no SSH or root access needed.

### Setup

1. Download or clone this repository
2. Open a terminal in the repository root
3. Launch Claude Code: `claude`
4. Start with Tier 1 and work sequentially

### Recommended Order

Work through tiers in order. Each tier builds on skills from the previous one.

| Tier | Focus | Exercises | Time |
|------|-------|-----------|------|
| Tier 1: Foundation | Server navigation, reading output, permissions | 1.1 – 1.4 | 60-90 min |
| Tier 2: Operations | Directory setup, systemd, security hardening | 2.1 – 2.6 | 90-120 min |
| Tier 3: Diagnosis | LNPS method, cascading failures, deployment specs | 3.1 – 3.4 | 60-90 min |

## The LNPS Debugging Method

Tier 3 exercises use the LNPS triage method. Follow this order for every diagnosis:

1. **Logs** — What do the logs say? Read before guessing.
2. **Network** — Can the service reach what it needs? Check ports and connectivity.
3. **Process** — Is the process alive? What state is it in?
4. **System** — Are disk, memory, and CPU okay?

## Exercise Workflow

For every exercise:

1. **Read INSTRUCTIONS.md** in the exercise folder
2. **Examine the starter files** — simulated server output, configs, logs
3. **Direct Claude Code** to investigate and diagnose
4. **Create the deliverable** (report, fix plan, audit, or spec)
5. **Reflect** using the questions in INSTRUCTIONS.md

## Tips

- **Read INSTRUCTIONS.md first** in each exercise before opening Claude Code
- **Never skip the investigation step** — even when you think you know what is wrong
- **For Debug exercises**: read the broken state carefully before attempting any fix
- **Reflect honestly** — the reflection questions are where real learning happens
