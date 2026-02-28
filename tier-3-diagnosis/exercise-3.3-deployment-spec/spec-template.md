# Deployment Specification: [Agent Name]

## 1. Server Requirements

| Requirement | Value |
|-------------|-------|
| OS | |
| Minimum Memory | |
| Minimum Disk | |
| Required Ports | |
| Network Access | |

## 2. Project Structure

```
/opt/agents/[agent-name]/
├── 
├── 
├── 
├── 
└── 
```

## 3. Dependencies

### System Packages
- 

### Python Packages
- 

## 4. Secret Management

### .env File Contents
```
# /opt/agents/[agent-name]/config/.env
```

### Permissions
- .env file: 
- config/ directory: 

## 5. systemd Service

```ini
[Unit]

[Service]

[Install]
```

## 6. Verification Checklist

| Check | Command | Expected Output |
|-------|---------|----------------|
| Service running | | |
| Service enabled | | |
| User exists | | |
| .env permissions | | |
| Logs writable | | |
