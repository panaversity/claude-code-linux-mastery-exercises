#!/bin/bash
# Deploy script for customer-support-agent
# Usage: ./deploy.sh <environment>
#
# Deploys the customer support agent to the specified environment.
# Supports "production" and "staging" environments.

ENVIRONMENT=$1
APP_NAME="customer-support-agent"
DEPLOY_DIR="/opt/$APP_NAME"
CONFIG_DIR="/etc/$APP_NAME"
LOG_DIR="/var/log/$APP_NAME"
DEPLOY_USER="supportagent"

echo "======================================"
echo "  Deploying $APP_NAME"
echo "  Environment: $ENVIRONMENT"
echo "  Date: $(date)"
echo "======================================"
echo ""

# Step 1: Validate environment argument
echo "[Step 1] Validating environment..."
if [ $ENVIRONMENT = "production" ] || [ $ENVIRONMENT = "staging" ]; then
    echo "  Target environment: $ENVIRONMENT"
else
    echo "  ERROR: Invalid environment '$ENVIRONMENT'"
    echo "  Usage: ./deploy.sh <production|staging>"
    exit 1
fi
echo ""

# Step 2: Create deploy user if not exists
echo "[Step 2] Checking deploy user..."
if id $DEPLOY_USER &>/dev/null; then
    echo "  User '$DEPLOY_USER' already exists"
else
    echo "  Creating user '$DEPLOY_USER'..."
    useradd -r -s /bin/false $DEPLOY_USER
    echo "  User created"
fi
echo ""

# Step 3: Copy application files
echo "[Step 3] Copying application files..."
echo "  Copying app files to $DEPLOY_DIR/"
cp -r agent-files/main.py $DEPLOY_DIR/
cp -r agent-files/requirements.txt $DEPLOY_DIR/
cp -r agent-files/templates/ $DEPLOY_DIR/templates/
echo "  Copying config to $CONFIG_DIR/"
cp agent-files/config.yaml $CONFIG_DIR/
echo "  Files copied successfully"
echo ""

# Step 4: Set permissions
echo "[Step 4] Setting permissions..."
chmod 755 $CONFIG_DIR/config.yaml
chown -R $DEPLOY_USER:$DEPLOY_USER $DEPLOY_DIR
chown -R $DEPLOY_USER:$DEPLOY_USER $CONFIG_DIR
chown -R $DEPLOY_USER:$DEPLOY_USER $LOG_DIR
echo "  Permissions set"
echo ""

# Step 5: Check if port is available
echo "[Step 5] Checking port availability..."
REQUIRED_PORT=8080
CURRENT_PORT=$(ss -tlnp | grep $APP_NAME | wc -l)
if [ $CURRENT_PORT = 0 ]; then
    echo "  Port $REQUIRED_PORT is available"
else
    echo "  WARNING: $APP_NAME already running ($CURRENT_PORT instances)"
    echo "  Stopping existing service..."
    systemctl stop $APP_NAME
fi
echo ""

# Step 6: Install and start service
echo "[Step 6] Installing systemd service..."
cp agent-files/support-agent.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable $APP_NAME
echo "  Starting $APP_NAME..."
systemctl start $APP_NAME
echo ""

# Step 7: Verify deployment
echo "[Step 7] Verifying deployment..."
sleep 2
STATUS=$(systemctl is-active $APP_NAME)
if [ $STATUS = "active" ]; then
    echo "  Deployment SUCCESSFUL"
    echo "  Service is running and healthy"
else
    echo "  Deployment FAILED"
    echo "  Status: $STATUS"
    echo "  Check logs: journalctl -u $APP_NAME --no-pager -n 50"
    exit 1
fi
echo ""

echo "======================================"
echo "  Deployment complete!"
echo "  App: $APP_NAME"
echo "  Env: $ENVIRONMENT"
echo "  Dir: $DEPLOY_DIR"
echo "======================================"
