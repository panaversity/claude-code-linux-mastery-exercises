# Capstone A -- Full Production Deployment

**Integration** -- End-to-end spec-first agent deployment

## Goal

Deploy a complete AI agent to a simulated production server using the spec-first methodology from Chapter 10. You will write a deployment specification, implement every step, validate against the spec, and package it all as a repeatable script.

This capstone integrates skills from across the entire chapter: filesystem layout, permissions, systemd service management, firewall configuration, SSH hardening, log management, and scripted automation. The spec-first approach ensures you think through every decision before executing.

## What You Have

- `agent-codebase/` -- A complete FastAPI customer support agent application with health check, chat endpoint, and stats endpoint
- `server-baseline.txt` -- Description of the target server's current state (fresh Ubuntu 22.04, only SSH installed)

## Your Tasks

### Phase 1: Write DEPLOYMENT-SPEC.md (30 min)

Before touching the server, write a complete deployment specification. This document is your blueprint -- every implementation step should trace back to a line in this spec.

Open Claude Code and ask it to help you create `DEPLOYMENT-SPEC.md` covering:

1. **Service definition** -- Service name, port, dedicated user, resource limits (memory, CPU)
2. **Directory layout** -- Where every file goes (`/opt` for application, `/etc` for config, `/var/log` for logs)
3. **Security requirements** -- SSH hardening rules, firewall rules, file permission matrix
4. **Monitoring plan** -- What to log, health check URL, restart behavior, alerting thresholds
5. **Validation criteria** -- How to verify each component works (specific commands for each check)

The spec should be detailed enough that someone else could implement the deployment by reading it alone.

### Phase 2: Implement (60 min)

Execute the specification step by step. Work through these in order, verifying each before moving to the next:

1. **Create dedicated system user** -- Non-login user with appropriate shell and home directory for the agent process
2. **Set up directory structure** -- Application directory in `/opt`, configuration in `/etc`, logs in `/var/log`
3. **Deploy application files** -- Copy agent code with correct ownership and permissions
4. **Create environment-specific configuration** -- Write the `.env` file (no secrets in plain text -- use placeholders)
5. **Write systemd service file** -- Include restart protection (`RestartSec`), resource limits (`MemoryMax`, `CPUQuota`), and proper dependencies
6. **Configure firewall** -- Allow SSH (port 22) and agent port only, deny everything else
7. **Harden SSH** -- Disable root login, disable password authentication
8. **Start and enable the service** -- The agent should start on boot

For each step, write the actual deployment artifacts (service file, config files, firewall rules) as files in this exercise directory.

### Phase 3: Validate (20 min)

Run layered validation -- each layer checks a different aspect of the deployment:

| Layer | Check | Command |
|-------|-------|---------|
| 1 | Service active? | `systemctl is-active support-agent` |
| 2 | Port listening? | `ss -tlnp \| grep 8080` |
| 3 | Health responding? | `curl -s localhost:8080/health` |
| 4 | Correct user? | `ps aux \| grep support-agent` |
| 5 | Logs flowing? | `journalctl -u support-agent --since "1 min ago"` |
| 6 | Resource limits? | `systemctl show support-agent -p MemoryMax,CPUQuota` |
| 7 | Security? | Check SSH config, file permissions, firewall rules |

Write the results of each validation layer in `VALIDATION-REPORT.md`.

### Phase 4: Package (20 min)

Convert everything into a repeatable `deploy.sh` script that another person could run on a fresh server matching `server-baseline.txt`. The script should:

- Be idempotent (safe to run multiple times)
- Include error checking (exit on failure)
- Print progress messages for each step
- Accept configuration via environment variables or arguments
- Include a `--dry-run` flag that shows what it would do without doing it

## Deliverables

Create these files in this exercise directory:

- `DEPLOYMENT-SPEC.md` -- Complete deployment specification (Phase 1)
- `deployment/support-agent.service` -- systemd service file
- `deployment/support-agent.env` -- Environment configuration (no real secrets)
- `deployment/ufw-rules.sh` -- Firewall configuration script
- `deployment/sshd-hardening.conf` -- SSH hardening overrides
- `deployment/logrotate-support-agent` -- Log rotation configuration
- `deploy.sh` -- Repeatable deployment script (Phase 4)
- `VALIDATION-REPORT.md` -- Results of all validation checks (Phase 3)

## Estimated Time

2-3 hours

## Reflection

1. How did writing the spec first change your implementation approach? Did it catch any decisions you would have made ad-hoc?
2. Which validation layer caught something you missed during implementation?
3. What would you add for a real production deployment that this exercise skipped? (Think: TLS certificates, database migrations, blue-green deploys, secrets management)
4. How would your `deploy.sh` need to change to support deploying a second agent on the same server?
