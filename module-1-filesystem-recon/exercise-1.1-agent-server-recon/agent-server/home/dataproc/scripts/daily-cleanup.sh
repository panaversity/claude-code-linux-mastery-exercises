#!/bin/bash
# daily-cleanup.sh - Clean up old data processor files
# Runs via cron: 0 4 * * * /home/dataproc/scripts/daily-cleanup.sh
# Author: jake@ops
# Last modified: 2026-01-22

set -euo pipefail

LOG_FILE="/var/log/data-processor/cleanup.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

log() {
    echo "${TIMESTAMP} [cleanup] $1" >> "${LOG_FILE}"
}

log "Starting daily cleanup"

# Remove processed output files older than 7 days
REMOVED_OUTPUT=$(find /var/lib/data-processor/output -name "processed-*.json" -mtime +7 -delete -print | wc -l)
log "Removed ${REMOVED_OUTPUT} old output files"

# Remove staging temp files older than 1 day
REMOVED_STAGING=$(find /home/dataproc/data/staging -name "temp-*.csv" -mtime +1 -delete -print | wc -l)
log "Removed ${REMOVED_STAGING} staging temp files"

# Archive input files that have been processed (older than 3 days)
ARCHIVE_DIR="/var/lib/data-processor/archive"
mkdir -p "${ARCHIVE_DIR}"
ARCHIVED=$(find /var/lib/data-processor/input -name "*.csv" -mtime +3 -exec mv {} "${ARCHIVE_DIR}/" \; -print | wc -l)
log "Archived ${ARCHIVED} processed input files"

# Report disk usage
DISK_USAGE=$(du -sh /var/lib/data-processor/ | cut -f1)
log "Data processor disk usage: ${DISK_USAGE}"

log "Daily cleanup complete"
