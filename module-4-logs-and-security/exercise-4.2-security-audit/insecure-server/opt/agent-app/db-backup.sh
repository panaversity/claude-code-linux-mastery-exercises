#!/bin/bash
# Database backup script for agent application
# Runs nightly via cron: 0 2 * * * /opt/agent-app/db-backup.sh
# Last modified: 2025-09-10

set -e

BACKUP_DIR="/var/backups/agent-db"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/agent_production_${TIMESTAMP}.sql.gz"

# Database credentials
DB_HOST="db-prod-01.internal.company.com"
DB_PORT=5432
DB_NAME="agent_production"
DB_USER="agent_svc"
PGPASSWORD="Pr0d_DB_Pass!2025"
export PGPASSWORD

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

echo "[$(date)] Starting database backup..."

# Perform backup
pg_dump -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" "$DB_NAME" | gzip > "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "[$(date)] Backup completed successfully: $BACKUP_FILE"
    echo "[$(date)] Backup size: $(du -h "$BACKUP_FILE" | cut -f1)"
else
    echo "[$(date)] ERROR: Backup failed!"
    # Send alert to Slack
    curl -s -X POST -H 'Content-type: application/json' \
        --data '{"text":"ALERT: Database backup failed on prod-agent-01"}' \
        "FAKE-slack-webhook-for-exercise"
    exit 1
fi

# Clean up backups older than 30 days
find "$BACKUP_DIR" -name "*.sql.gz" -mtime +30 -delete
echo "[$(date)] Cleaned up old backups"

# Verify backup integrity
gunzip -t "$BACKUP_FILE"
if [ $? -eq 0 ]; then
    echo "[$(date)] Backup integrity verified"
else
    echo "[$(date)] WARNING: Backup integrity check failed!"
    exit 1
fi

echo "[$(date)] Backup process complete"
