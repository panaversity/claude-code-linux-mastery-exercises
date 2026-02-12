# Service Requirements

## Basic Requirements
- Service name: `support-agent`
- Run as dedicated user: `supportagent` (system user, no login shell)
- Working directory: `/opt/support-agent/`
- Start command: `/opt/support-agent/venv/bin/python main.py`
- Environment file: `/etc/support-agent/agent.env`
- Start after: network.target

## Reliability Requirements
- Restart on failure (NOT on clean exit)
- Wait 5 seconds between restart attempts
- Maximum 5 restarts per 60-second window (prevent restart storms)
- Log to journald (StandardOutput=journal, StandardError=journal)
- SyslogIdentifier: support-agent

## Resource Limits
- Maximum memory: 512MB (MemoryMax=512M)
- Maximum CPU: 200% of one core (CPUQuota=200%)
- These prevent a runaway agent from killing the server

## Security
- NoNewPrivileges=true (prevent privilege escalation)
- ProtectSystem=strict (read-only filesystem except working dirs)
- ReadWritePaths=/var/log/support-agent /opt/support-agent/data

## Startup
- Enable for boot: WantedBy=multi-user.target
- Type=simple (uvicorn runs in foreground)
