# Admin bash history -- prod-server-01
# Most recent commands at bottom

# Feb 9 -- regular maintenance
sudo apt update
sudo apt list --upgradable
df -h
free -m
systemctl status support-agent
systemctl status weather-bot
uptime

# Feb 9 15:10 -- "speed up recovery time"
sudo systemctl edit support-agent
# changed RestartSec from 5 to 0
sudo systemctl daemon-reload
sudo systemctl restart support-agent
# "that should make it recover faster"

# Feb 9 15:30 -- checking disk
df -h
# showed 78% -- "still have room"
du -sh /var/log/*
# /var/log/support-agent was 650MB but "it'll be fine"

# Feb 9 18:00 -- end of day
exit

# Feb 10 08:30 -- morning check after alerts
sudo systemctl status support-agent
# showing constant restarts
journalctl -u support-agent --since "1 hour ago" | tail -20
# tons of restart entries
df -h
# 95%!!
du -sh /var/log/support-agent/*
# 800MB access.log
du -sh /var/lib/support-agent/cache/*
# 2.1GB response-cache.json
# "how did it grow that fast?"
