# Exercise 1.2 -- Misplaced Deployment

**Debug** -- Fix a botched agent deployment by relocating files to standard Linux locations

## Goal

A junior admin deployed an AI agent but put everything in the wrong places. The agent binary is in `/tmp`, configs are in the home directory, logs are going to stdout with no file target, and the service file references all the wrong paths. You need to fix the layout to match Linux filesystem conventions and document every change you make.

## What You Have

- `broken-server/` -- A server where a `summarizer-agent` has been deployed with every file in the wrong location. The agent technically works, but it violates Linux filesystem conventions in ways that will cause real problems (data loss on reboot, security issues, maintenance nightmares).

## Your Tasks

### Step 1: Launch Claude Code
Open a terminal in this exercise directory and run `claude` to start a Claude Code session.

### Step 2: Survey the Broken Layout
Ask Claude Code to map every file in `broken-server/`. For each file, identify what it is and note where it currently lives.

### Step 3: Identify Correct Locations
For each misplaced file, determine where it SHOULD be according to Linux filesystem conventions:
- Binaries/scripts go in `/opt/<app>/` or `/usr/local/bin/`
- Configuration goes in `/etc/<app>/`
- Service files go in `/etc/systemd/system/`
- Logs go in `/var/log/<app>/`
- Persistent data goes in `/var/lib/<app>/`
- SSL certificates go in `/etc/ssl/` or `/opt/<app>/certs/`
- Environment files stay with the application in `/opt/<app>/`

### Step 4: Create the Correct Directory Structure
Build out the proper directory tree inside `broken-server/` with all the standard locations.

### Step 5: Move Files to Correct Locations
Relocate each file from its wrong location to the correct one.

### Step 6: Fix Path References
Update the service file so all `ExecStart`, `WorkingDirectory`, and `EnvironmentFile` paths point to the new correct locations. Update `config.yaml` so all directory paths reference the correct locations.

### Step 7: Create FIXES-LOG.md
Document every change in a `FIXES-LOG.md` file in this exercise directory. For each fix, include:
- What file was moved
- Where it was (wrong location)
- Where it is now (correct location)
- Why the original location was wrong
- What could go wrong if left in the original location

## Expected Results

- All files relocated to standard Linux filesystem locations
- Service file with all paths pointing to correct locations
- Config file with all directory references updated
- No files remaining in `tmp/`, `home/admin/`, or `root/`
- A `FIXES-LOG.md` with before/after documentation and rationale for every change

## Reflection

1. Which Linux filesystem convention was most severely violated? What real-world consequences would it cause?
2. What would happen if the agent ran from `/tmp`? (Hint: most Linux distributions clean `/tmp` on reboot via `tmpfiles.d` or `systemd-tmpfiles-clean.timer`)
3. Why is running an application's data directory as root a security concern? What principle does this violate?
