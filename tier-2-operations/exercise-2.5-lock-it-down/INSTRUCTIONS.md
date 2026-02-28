# Exercise 2.5 — Lock It Down (Build)

## Scenario

Ali's social-media-monitor is running as a systemd service — but it is running as root because the intern never created a dedicated user. Dev says: "A root agent with internet access is a security nightmare. Lock it down."

## Your Task

Using the `insecure-deployment/` as the starting state, write a `HARDENING-PLAN.md` that documents every step to secure this deployment:

1. Create a dedicated `social-monitor` system user with no login shell and no home directory
2. Change ownership of the project directory to the new user
3. Set file permissions so only the service user can read the `.env` file
4. Update the systemd unit file to run as the new user
5. Set up SSH key authentication for Ali's personal login (describe the commands)

For each step, include: the exact command, what it does, and how to verify it worked.

## Success Criteria

- [ ] useradd command creates system user with --system --no-create-home --shell /usr/sbin/nologin
- [ ] chown -R changes ownership of entire project directory
- [ ] chmod 600 on .env file
- [ ] Unit file updated with User= and Group=
- [ ] SSH key setup steps are complete and correct
- [ ] Each step has a verification command

## Reflection

Why does Ali create a system user with no login shell instead of a regular user? What attack vector does this close?
