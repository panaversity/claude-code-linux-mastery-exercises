# Exercise 6.1 -- The Cascade Failure

**Build** -- Systematically trace an HTTP 502 error to its root cause

## Goal

Users report that the support agent is returning HTTP 502 errors. Your job: use systematic layer-by-layer diagnosis to find the root cause. Don't guess -- trace through each layer methodically.

## What You Have

- `broken-stack/` -- A simulated multi-component setup with logs and configs for: nginx (reverse proxy), the support agent (FastAPI), Redis (cache), and PostgreSQL (database)

## Your Tasks

Follow the systematic debugging methodology -- check each layer in order:

### Layer 1: Is the service running?

1. Read `systemctl-status.txt` for the agent service. Is it active? If not, what does the status say?

### Layer 2: Is the port listening?

2. Read `ss-output.txt` -- is anything listening on port 8080? If not, that explains why nginx gets a 502.

### Layer 3: Can the app start?

3. Read `journalctl-agent.txt` -- what happens when the service tries to start? Look for Python errors, import failures, or connection issues.

### Layer 4: Are dependencies healthy?

4. Read `redis-status.txt` -- is Redis running?
5. Read `pg-status.txt` -- is PostgreSQL running and accepting connections?

### Layer 5: What does nginx see?

6. Read `nginx-error.log` -- what error does nginx report when proxying?

### Layer 6: Write the diagnosis

7. Trace the full failure chain from user to nginx to agent to dependency.
8. Write `ROOT-CAUSE-ANALYSIS.md` in this exercise directory with:
   - **Symptom**: what the user sees
   - **Layer-by-layer trace**: what you checked at each layer and what you found
   - **Root cause**: the actual problem
   - **Fix**: specific commands to resolve the issue
   - **Prevention**: how to prevent recurrence

## Expected Results

- A `ROOT-CAUSE-ANALYSIS.md` with systematic diagnosis following the layer-by-layer methodology
- The root cause correctly identified with a specific fix command

## Reflection

1. At which layer did you identify the problem? Could you have jumped straight there?
2. Why is systematic layer-by-layer diagnosis better than jumping to conclusions?
3. How would automated health checks have caught this before users reported it?
