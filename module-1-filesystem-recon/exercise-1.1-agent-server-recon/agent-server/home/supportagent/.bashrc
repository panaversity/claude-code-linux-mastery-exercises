# .bashrc for supportagent service account
# Created: 2025-12-03

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# Support agent shortcuts
alias salogs='tail -f /var/log/support-agent/combined.log | jq .'
alias sastatus='systemctl status support-agent'
alias sarestart='sudo systemctl restart support-agent'

# Check active sessions
alias sasessions='curl -s http://localhost:8002/admin/sessions | jq .'

# Node version management
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

export PATH="/opt/support-agent/node_modules/.bin:$PATH"
