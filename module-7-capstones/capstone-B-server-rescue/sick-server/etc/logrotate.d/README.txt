# Log Rotation Configuration Directory
#
# This directory should contain logrotate configs for all services.
# Currently installed configs:
#   (none)
#
# MISSING CONFIGS:
#   - No config for support-agent logs (/var/log/support-agent/)
#   - No config for weather-bot logs (/var/log/weather-bot/)
#
# Without logrotate configs, log files grow indefinitely.
# The support-agent access.log is currently 800MB and growing.
#
# A typical logrotate config would look like:
#
#   /var/log/support-agent/*.log {
#       daily
#       rotate 14
#       compress
#       delaycompress
#       missingok
#       notifempty
#       postrotate
#           systemctl reload support-agent 2>/dev/null || true
#       endscript
#   }
#
# This config was never created during the initial deployment.
# TODO: INFRA-201 -- Add logrotate configs for all agent services
