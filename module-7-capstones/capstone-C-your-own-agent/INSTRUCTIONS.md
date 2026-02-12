# Capstone C -- Your Own Agent

**Integration** -- Deploy your own project to a Linux environment

## Goal

Take a real project you are working on (or use the provided sample) and deploy it using everything you have learned in this chapter. This is YOUR deployment -- you make the decisions, write the spec, create the artifacts, and validate the result.

This capstone is deliberately open-ended. There is no single correct answer. The quality of your work is measured by how thoroughly you apply the skills from every module: filesystem layout, permissions, service management, security hardening, log management, and automation.

## Choose Your Project

### Option 1: Your Own Project

If you have a real application (any language, any framework), deploy it. This is the most valuable path because you will immediately apply what you learn to something you care about.

Your application should have at minimum:
- An HTTP endpoint (API, web app, webhook, anything)
- A health check route
- Some form of logging

### Option 2: Sample Agent

If you do not have a project ready, use `sample-agent/` -- a simple webhook receiver that accepts POST requests, logs them to a JSONL file, and returns 200 OK. It is intentionally simple so the focus is on deployment, not application complexity.

## Your Tasks

### Task 1: Write DEPLOYMENT-SPEC.md

Before creating any deployment artifacts, write a complete specification. This document should answer every question a new team member would have about how this service runs in production.

Cover at minimum:
- **Service identity**: Name, purpose, port, protocol
- **User isolation**: Dedicated user, group, shell, home directory
- **Directory layout**: Where application code, config, logs, and data live
- **systemd service**: Restart behavior, resource limits, dependencies, security directives
- **Network security**: Firewall rules, allowed ports, denied ports
- **SSH hardening**: Authentication method, root access, idle timeout
- **Log management**: Rotation schedule, retention period, max file size
- **Health monitoring**: Health check URL, expected response, check frequency
- **Permissions matrix**: Every file and directory with owner, group, and mode

### Task 2: Create Deployment Artifacts

Create every file needed for the deployment:

- systemd service file (`.service`)
- Environment configuration (`.env` with placeholders, no real secrets)
- Firewall rules script
- SSH hardening configuration
- Log rotation configuration
- Any application-specific configuration

### Task 3: Write deploy.sh

Create an automated deployment script that:

- Is idempotent (safe to run multiple times)
- Creates the system user if it does not exist
- Sets up the directory structure
- Deploys application files with correct permissions
- Installs the systemd service
- Configures the firewall
- Hardens SSH
- Sets up log rotation
- Starts and enables the service
- Prints a summary of what it did

Include error handling (`set -euo pipefail`) and progress messages.

### Task 4: Write verify.sh

Create a verification script that checks every aspect of the deployment:

```bash
#!/usr/bin/env bash
# Verify deployment of [your-service]
# Exit 0 if all checks pass, exit 1 if any fail

PASS=0
FAIL=0

check() {
    local description="$1"
    local command="$2"
    if eval "$command" > /dev/null 2>&1; then
        echo "  PASS: $description"
        ((PASS++))
    else
        echo "  FAIL: $description"
        ((FAIL++))
    fi
}

echo "Running deployment verification..."
check "Service is active"        "systemctl is-active your-service"
check "Port is listening"        "ss -tlnp | grep :PORT"
check "Health check responds"    "curl -sf localhost:PORT/health"
# ... more checks ...

echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
```

### Task 5: Write DEPLOYMENT-GUIDE.md

Document how someone else would use your deployment:

- Prerequisites (OS, packages, access)
- Step-by-step deployment instructions
- How to verify the deployment
- How to troubleshoot common issues
- How to update the application
- How to roll back a bad deployment

## Self-Assessment Checklist

Rate yourself on each item. Be honest -- the goal is learning, not a perfect score.

| Check | Status | Notes |
|-------|--------|-------|
| Dedicated non-root user created | | |
| Proper directory structure (/opt, /etc, /var/log) | | |
| systemd service with restart protection (RestartSec >= 5) | | |
| Resource limits configured (MemoryMax, CPUQuota) | | |
| Environment-specific configuration (no hardcoded values) | | |
| Firewall rules (SSH + app port only, deny all else) | | |
| SSH hardened (no root login, no password auth) | | |
| Log rotation configured (daily, compressed, retained 14 days) | | |
| Health check endpoint working | | |
| Deployment is repeatable (deploy.sh works on fresh server) | | |
| All files have correct permissions (no world-writable) | | |
| No secrets in config files (environment variables only) | | |
| Verification script checks all components | | |
| Deployment guide is complete enough for a new team member | | |

## Estimated Time

2-4 hours (depends on whether you use your own project or the sample)

## Deliverables

- `DEPLOYMENT-SPEC.md` -- Complete deployment specification
- `deployment/` directory with all deployment artifacts (service file, configs, scripts)
- `deploy.sh` -- Automated deployment script
- `verify.sh` -- Automated verification script
- `DEPLOYMENT-GUIDE.md` -- Documentation for other team members
- Completed self-assessment checklist (update the table above)

## Reflection

1. What was the hardest part of specifying the deployment before implementing it? Where did you have to make judgment calls?
2. How does your deployment handle the application crashing? Walk through the exact sequence of events from crash to recovery.
3. If a new person joined your team tomorrow, could they deploy and verify this service using only your documentation? What would they struggle with?
4. What is the single most important thing this chapter taught you about running services on Linux?
