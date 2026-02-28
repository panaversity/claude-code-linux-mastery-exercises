# Deployment Specification: Price Watcher Agent

## Service Configuration
- User: price-watcher
- Group: price-watcher
- Restart: on-failure
- RestartSec: 10

## Security
- .env permissions: 600 (owner read/write only)
- .env owner: price-watcher:price-watcher

## Boot Configuration
- Service must start on boot (systemctl enable)

## Verification Checklist
| Check | Command | Expected |
|-------|---------|----------|
| Service user | `systemctl show -p User price-watcher` | User=price-watcher |
| .env perms | `stat -c '%a' /opt/agents/price-watcher/config/.env` | 600 |
| Boot enabled | `systemctl is-enabled price-watcher` | enabled |
| Service active | `systemctl is-active price-watcher` | active |
