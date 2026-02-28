# Exercise 1.1 — Server Orientation (Build)

## Scenario

Ali just got SSH access to a new cloud server from a different hosting provider. He has never logged into this machine before. Before he deploys anything, he needs to understand what he is working with.

## Your Task

Use Claude Code to explore the `simulated-server/` directory as if it were a real Linux server. Investigate:

1. What Linux distribution and version is running (check `etc/os-release`)
2. How much disk space and memory are available (check `etc/server-info.txt`)
3. What is in `/home` — are there other users?
4. What is in `/opt` and `/var` — has anyone deployed anything here before?
5. What the current user's permissions are (check `etc/passwd-excerpt.txt`)

Create a `SERVER-REPORT.md` summarizing: What OS is this? How much space do I have? Am I alone on this server? Has anything been deployed here before? What can I do without sudo?

## Success Criteria

- [ ] Identified the OS and version
- [ ] Reported disk and memory stats
- [ ] Listed all users with home directories
- [ ] Discovered the old webapp in `/opt`
- [ ] Summarized server readiness in 2-3 sentences

## Reflection

Why does Ali check what is already on the server before deploying anything? What could go wrong if he skipped this step?
