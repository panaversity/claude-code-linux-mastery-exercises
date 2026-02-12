# .bashrc for dataproc service account
# Created: 2025-12-15

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# Data processor shortcuts
alias dplogs='tail -f /var/log/data-processor/pipeline.log'
alias dpstatus='systemctl status data-processor'
alias dprun='sudo systemctl start data-processor'
alias dpinput='ls -la /var/lib/data-processor/input/'
alias dpoutput='ls -la /var/lib/data-processor/output/'

# Quick check of last batch run
alias dplast='journalctl -u data-processor --since "today" --no-pager'

# Count pending files
alias dppending='ls /var/lib/data-processor/input/*.csv 2>/dev/null | wc -l'

export PATH="/opt/data-processor:$PATH"
export PIPELINE_CONFIG="/etc/data-processor/pipeline.yaml"
