# Exercise 2.4 — The Service That Won't Start (Debug)

## Scenario

Ali's competitor-tracker service was working yesterday. This morning, `systemctl status competitor-tracker` shows it as "failed." Ali's instinct is to restart it. But he remembers: restarting is not debugging.

## Your Task

Examine the `broken-service/` directory. Three things are broken simultaneously:

1. Check `systemctl-status.txt` for the error message
2. Check `journalctl-output.txt` for detailed logs
3. Check the unit file — does the Python path it references exist?
4. Check the `.env` file — are all required variables present?
5. Check directory permissions in `ls-output.txt`

Find all THREE root causes before proposing any fixes. Document them in `DIAGNOSIS.md` with: what is broken, how you found it, and the fix.

## The Three Root Causes

(Find these yourself — they are all documented in the provided files)

## Success Criteria

- [ ] Found root cause 1: wrong Python path in unit file
- [ ] Found root cause 2: missing DATABASE_URL in .env
- [ ] Found root cause 3: read-only logs directory
- [ ] Diagnosed ALL THREE before proposing fixes
- [ ] Fixes are in correct order (path → env → permissions → restart)

## Reflection

If Ali had just restarted the service, would restarting have fixed any of these three problems? Why is the diagnostic step non-negotiable?
