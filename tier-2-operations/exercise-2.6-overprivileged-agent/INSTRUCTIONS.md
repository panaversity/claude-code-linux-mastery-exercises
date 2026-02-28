# Exercise 2.6 — The Overprivileged Agent (Debug)

## Scenario

Ali audits a server that another team has been using. He finds an agent running as root with security holes everywhere. Dev asks him to identify and fix every security problem.

## Your Task

Examine the `insecure-server/` directory. Five security problems are planted:

1. **Check the systemd service** (`etc/systemd/system/report-generator.service`) — what user does it run as?
2. **Check the .env permissions** (`opt/agents/report-generator/config/.env`) — who can read it?
3. **Check SSH configuration** (`etc/ssh/sshd_config`) — is password auth enabled?
4. **Check the log files** (`var/log/agent-app/app.log`) — are secrets being logged?
5. **Check the firewall rules** (`etc/iptables/rules.v4`) — is the agent port exposed?

For each problem: state what is wrong, explain the specific risk (what could an attacker do?), and write the fix command. Create a `SECURITY-AUDIT.md` with findings ordered by severity.

## Success Criteria

- [ ] Found: service runs as root
- [ ] Found: .env has 666 permissions (world read+write)
- [ ] Found: SSH password authentication enabled
- [ ] Found: API keys printed in log files
- [ ] Found: port 8080 exposed to all interfaces
- [ ] Ordered fixes by severity (leaked keys most urgent)
- [ ] Each fix includes the specific command

## Reflection

Which of the five problems could be exploited by someone who does NOT have SSH access to the server? Which require an attacker to already be on the machine? How does this change your fix priority?
