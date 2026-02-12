# Exercise 6.2 -- Deploy Pipeline

**Build** -- Chain all chapter skills into a complete deployment script

## Goal

Write a `deploy-agent.sh` script that performs a complete agent deployment from scratch. This is the culmination of everything in the chapter -- file operations, text processing, scripting, security, service management, and verification -- all in one automated pipeline.

## What You Have

- `agent-package/` -- The agent application files ready to deploy
- `DEPLOY-SPEC.md` -- Exact specification of what the script must do
- `verify-deployment.sh` -- A verification script that tests if deployment succeeded (provided, read-only)

## Your Tasks

### Step 1: Understand the Specification
Read `DEPLOY-SPEC.md` to understand all deployment steps and the configuration differences between production and staging environments.

### Step 2: Understand the Verification
Read `verify-deployment.sh` to understand what will be checked. Your script must pass all these checks.

### Step 3: Write the Deployment Script
Write `deploy-agent.sh` that performs ALL steps in order:
1. Validate arguments (environment name required, must be "production" or "staging")
2. Create a dedicated system user for the service
3. Create directory structure (`/opt`, `/etc`, `/var/log`)
4. Copy application files with correct permissions
5. Generate environment-specific config from templates (replace all `${VARIABLE}` placeholders)
6. Install the systemd service file
7. Enable and start the service
8. Run a basic health check (`curl localhost:PORT/health`)
9. Print a deployment summary

### Step 4: Make It Production-Grade
- Make the script idempotent (safe to run twice without breaking anything)
- Add proper error handling (`set -euo pipefail`, trap for cleanup)

### Step 5: Test and Verify
Run `deploy-agent.sh` and then `verify-deployment.sh` to confirm all checks pass.

### Step 6: Document
Write `DEPLOY-LOG.md` documenting what the script does at each step and why.

## Expected Results

- `deploy-agent.sh` -- Complete, idempotent deployment script (~80-120 lines)
- `DEPLOY-LOG.md` -- Documentation of each deployment step
- `verify-deployment.sh` passes all checks

## Reflection

1. How many skills from this chapter did your script use? List them.
2. What makes a deployment script "idempotent"? Why does it matter?
3. What would you add for a production deployment that this exercise skips?
