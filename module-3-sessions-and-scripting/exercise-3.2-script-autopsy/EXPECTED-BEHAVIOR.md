# Expected Behavior of deploy.sh

## Usage

```
./deploy.sh <environment>
```

Where `environment` is either `"production"` or `"staging"`.

## Step-by-Step Expected Behavior

### Step 1: Validate Environment

- If no argument provided: print a clear usage message and exit with code 1
- If argument is not "production" or "staging": print error with the invalid value and exit 1
- If valid: print the target environment and continue
- The script should never produce a bash syntax error for missing arguments

### Step 2: Create Deploy User

- If user "supportagent" already exists: print a message and skip
- If user does not exist: create a system user with no login shell (`/bin/false`)
- This step should work on any Linux system with `useradd`

### Step 3: Copy Application Files

- **Create directories first if they do not exist:**
  - `/opt/customer-support-agent/` (application files)
  - `/etc/customer-support-agent/` (configuration)
  - `/var/log/customer-support-agent/` (logs)
- Copy `main.py`, `requirements.txt`, and `templates/` to `/opt/customer-support-agent/`
- Copy `config.yaml` to `/etc/customer-support-agent/`
- If any copy fails, the script should stop immediately (not continue to later steps)

### Step 4: Set Permissions

- `main.py` should be executable: `chmod 755 /opt/customer-support-agent/main.py`
- `config.yaml` should be read-only (not executable): `chmod 644 /etc/customer-support-agent/config.yaml`
- All application files owned by the `supportagent` user and group
- Log directory also owned by `supportagent`

### Step 5: Check Port Availability

- Count how many instances of the app are currently running (numeric comparison)
- If zero: report port is available and continue
- If non-zero: stop the existing service first, then continue
- The comparison should use numeric operators (`-eq`) not string operators (`=`)

### Step 6: Install and Start Service

- Copy the `.service` file to `/etc/systemd/system/`
- Reload the systemd daemon to pick up the new service file
- Enable the service (so it starts on boot)
- Start the service

### Step 7: Verify Deployment

- Wait 2 seconds for the service to initialize
- Check if the service is active
- If active: report success
- If not active: report failure with the exact command to check logs
- Exit with code 1 on failure, code 0 on success
