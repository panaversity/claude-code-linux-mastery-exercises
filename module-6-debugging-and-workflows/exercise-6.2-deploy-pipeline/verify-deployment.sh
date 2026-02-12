#!/bin/bash
set -euo pipefail

APP_NAME="support-agent"
ENVIRONMENT="${1:-production}"

echo "=== Deployment Verification ==="
echo "App: $APP_NAME | Environment: $ENVIRONMENT"
echo ""

PASS=0
FAIL=0

check() {
    local description="$1"
    local command="$2"
    if eval "$command" &>/dev/null; then
        echo "✓ PASS: $description"
        ((PASS++))
    else
        echo "✗ FAIL: $description"
        ((FAIL++))
    fi
}

# Directory structure
check "App directory exists" "[ -d /opt/$APP_NAME ]"
check "Config directory exists" "[ -d /etc/$APP_NAME ]"
check "Log directory exists" "[ -d /var/log/$APP_NAME ]"

# Files
check "main.py exists and is executable" "[ -x /opt/$APP_NAME/main.py ]"
check "Config file exists" "[ -f /etc/$APP_NAME/config.yaml ]"
check "Env file exists" "[ -f /etc/$APP_NAME/agent.env ]"

# No template variables remaining
check "Config has no unresolved variables" "! grep -q '\${' /etc/$APP_NAME/config.yaml"
check "Env has no unresolved variables" "! grep -q '\${' /etc/$APP_NAME/agent.env"

# Service
check "Service file exists" "[ -f /etc/systemd/system/$APP_NAME.service ]"
check "Service is enabled" "systemctl is-enabled $APP_NAME"
check "Service is active" "systemctl is-active $APP_NAME"

# User
check "Service user exists" "id ${APP_NAME}-user"

# Permissions
check "Config not world-readable" "[ ! -r /etc/$APP_NAME/agent.env ] || [ $(stat -c '%a' /etc/$APP_NAME/agent.env) = '640' ]"

echo ""
echo "=== Results: $PASS passed, $FAIL failed ==="
[ $FAIL -eq 0 ] && echo "Deployment verified successfully!" || echo "Deployment has issues — fix and re-run."
