ls -la /opt/agent-app/
systemctl status agent-app
journalctl -u agent-app -f
cd /opt/agent-app
cat .env
vim config.yaml
sudo systemctl restart agent-app
tail -f /var/log/agent-app/access.log
curl -H "Authorization: Bearer FAKE-deepseek-api-key-for-exercise" http://localhost:8080/api/health
mysql -u root -p'Pr0d_DB_Pass!2025' -h db-prod-01.internal.company.com
psql -U agent_svc -h db-prod-01.internal.company.com -d agent_production
export PGPASSWORD='Pr0d_DB_Pass!2025' && psql -U agent_svc -h db-prod-01.internal.company.com
ssh root@10.0.1.50
ssh root@10.0.1.51
scp /opt/agent-app/.env admin@10.0.1.52:/tmp/
curl -X POST https://api.deepseek.com/v1/chat/completions -H "Authorization: Bearer FAKE-deepseek-api-key-for-exercise" -d '{"model":"deepseek-chat","messages":[{"role":"user","content":"test"}]}'
sudo iptables -L
sudo iptables -F
docker ps
docker logs agent-app-redis-1
pip install requests
sudo apt update && sudo apt upgrade -y
df -h
free -m
top
htop
vim /etc/ssh/sshd_config
sudo systemctl restart sshd
git pull origin main
chmod 666 /etc/agent-app/config.yaml
chmod 644 /opt/agent-app/.env
sudo chown root:root /etc/agent-app/config.yaml
ls -la /var/log/agent-app/
cat /var/log/agent-app/access.log | grep ERROR | tail -20
history
