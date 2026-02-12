# .bashrc for weatherbot service account
# Created: 2025-11-20

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# Weather bot shortcuts
alias wblogs='tail -f /var/log/weather-bot/access.log'
alias wberr='tail -f /var/log/weather-bot/error.log'
alias wbstatus='systemctl status weather-bot'
alias wbrestart='sudo systemctl restart weather-bot'

# Quick health check
alias wbhealth='curl -s http://localhost:8001/health | python3 -m json.tool'

export PATH="/opt/weather-bot:$PATH"
