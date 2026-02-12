# Deployment Specification

## Script: deploy-agent.sh
## Usage: ./deploy-agent.sh <environment>
## Environments: production, staging

## Configuration by Environment

| Setting | Production | Staging |
|---------|-----------|---------|
| PORT | 8080 | 8081 |
| LOG_LEVEL | WARNING | DEBUG |
| WORKER_COUNT | 4 | 1 |
| MEMORY_LIMIT | 512M | 256M |
| CPU_QUOTA | 200% | 100% |
| POOL_SIZE | 20 | 5 |
| MODEL_NAME | gpt-4 | gpt-3.5-turbo |
| MAX_TOKENS | 2048 | 1024 |

## Deployment Steps (in order)

### 1. Argument Validation
- Require exactly one argument
- Must be "production" or "staging"
- Print usage if wrong

### 2. User Creation
- Create system user: ${APP_NAME}-user (e.g., support-agent-user)
- No login shell (-s /bin/false)
- Skip if user already exists (idempotent)

### 3. Directory Structure
- /opt/${APP_NAME}/ -- Application files (owned by service user)
- /etc/${APP_NAME}/ -- Configuration (owned by root, readable by service user)
- /var/log/${APP_NAME}/ -- Logs (owned by service user)
- All created with mkdir -p (idempotent)

### 4. Application Files
- Copy all files from agent-package/ to /opt/${APP_NAME}/
- Set permissions: main.py 755, others 644
- Set ownership to service user

### 5. Configuration
- Process config.template.yaml -> /etc/${APP_NAME}/config.yaml
  (replace all ${VARIABLE} with environment-specific values using sed or envsubst)
- Process .env.template -> /etc/${APP_NAME}/agent.env
- Set config permissions: 640 (root:service-group)

### 6. Service Installation
- Process agent.service.template -> /etc/systemd/system/${APP_NAME}.service
- systemctl daemon-reload
- systemctl enable ${APP_NAME}

### 7. Service Start
- systemctl start ${APP_NAME}
- Wait 3 seconds for startup

### 8. Health Check
- curl -sf http://localhost:${PORT}/health
- If fails: print error and show journalctl command
- If succeeds: print success with port and PID

### 9. Summary
- Print deployment summary: environment, user, port, service status
