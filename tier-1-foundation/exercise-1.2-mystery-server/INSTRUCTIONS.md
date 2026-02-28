# Exercise 1.2 — The Mystery Server (Debug)

## Scenario

Ali's colleague Priya asks for help. She deployed an agent to a server last month but cannot remember the details. She knows it is "somewhere in /opt" and it "used to work." She gives Ali SSH access and asks him to figure out what is there, where it lives, and whether it is still running.

## Your Task

Investigate the `simulated-server/` directory. Find the project directory under `/opt`. Read the directory structure to understand what the agent does. Check the file timestamps (recorded in `file-timestamps.txt`) to see when things were last modified. Look at the log files for any error messages or the last successful run. Check if there is a systemd service for it.

Produce a summary for Priya:
> "Your agent is at [path], it does [purpose], it last ran on [date], and it stopped because [reason]."

## Success Criteria

- [ ] Found the agent directory under /opt
- [ ] Identified what the agent does from source code and README
- [ ] Determined when it last ran from logs and timestamps
- [ ] Found the reason it stopped
- [ ] Checked for a systemd service file
- [ ] Wrote a clear summary for Priya

## Reflection

What clues did the file timestamps and log contents give you? If the logs were empty, what would you check next?
