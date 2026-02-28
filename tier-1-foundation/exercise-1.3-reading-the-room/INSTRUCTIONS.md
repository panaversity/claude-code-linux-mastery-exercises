# Exercise 1.3 — Reading the Room (Build)

## Scenario

Ali wants to check the health of a server before deploying his competitor-tracker agent. He needs to read system output and understand what it means — not just see numbers, but interpret them.

## Your Task

The file `simulated-server/system-health-output.txt` contains the output of four diagnostic commands captured from a real server. Read each section and write a `HEALTH-ASSESSMENT.md` that answers:

1. **Disk usage** (`df -h` output): Which filesystem is most full? Is there enough space for a new agent?
2. **Memory** (`free -h` output): How much free memory is available? Is there enough for a Python agent (~200MB)?
3. **Top processes** (`ps aux` output): What are the top memory consumers? Is anything using too much?
4. **Load average** (`uptime` output): What do the three load numbers mean? Is this server under stress?

For each section, write one sentence explaining what the output tells you about this server's readiness for a new deployment.

## Success Criteria

- [ ] Correctly identified the fullest filesystem and remaining space
- [ ] Assessed whether memory is sufficient for a Python agent
- [ ] Identified the top 3 memory-consuming processes
- [ ] Explained all three load average numbers
- [ ] Wrote a go/no-go recommendation for deploying a new agent

## Reflection

If the disk was 92% full, what would you tell Claude Code to do before deploying? How would you decide what is safe to delete?
