# Exercise 2.3 — Service From Scratch (Build)

## Scenario

Ali's social-media-monitor agent is ready to run. Right now he starts it manually with `python3 src/main.py`. Every time his SSH session ends, the agent dies. He needs to turn this into a systemd service that survives reboots and restarts after crashes.

## Your Task

Using the mock agent in `social-monitor/`, write a complete systemd service unit file (`social-monitor.service`) that:

1. Runs as a dedicated `social-monitor` user (not root)
2. Loads environment variables from the `.env` file
3. Uses `Restart=on-failure` with a 10-second delay between restarts
4. Sets a memory limit of 256MB
5. Starts automatically on boot

Write the unit file and a `SETUP-STEPS.md` documenting every command you would run to install and start the service.

## Success Criteria

- [ ] Unit file has correct [Unit], [Service], and [Install] sections
- [ ] User= is set to a non-root user
- [ ] EnvironmentFile= points to the .env file
- [ ] Restart=on-failure with RestartSec=10
- [ ] MemoryMax=256M (or MemoryLimit for older systemd)
- [ ] WantedBy=multi-user.target for boot startup
- [ ] SETUP-STEPS.md lists commands in correct order

## Reflection

Why did Ali choose `Restart=on-failure` instead of `Restart=always`? What is the difference, and when would `always` be the wrong choice?
