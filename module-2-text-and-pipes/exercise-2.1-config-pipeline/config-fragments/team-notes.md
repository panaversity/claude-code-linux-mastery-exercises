# Sprint 47 Team Notes

## Monday Standup (2026-02-03)

- Jake: Working on database migration scripts for v2.4.1
- Sarah: Reviewed infrastructure costs -- our Redis instance is oversized for current load
- Mike: Customer complaint ticket #4821 about slow chat responses during peak hours
- DECISION: Use port 443 for external nginx (was debating 8443 but standard HTTPS is simpler)
- DECISION: Rate limit API at 10 requests/second per IP (burst of 20 allowed)
- Reminder: Sprint demo on Friday

## Wednesday Architecture Review (2026-02-05)

- Discussed caching strategy for agent responses
- Sarah presented cost analysis: current cache hit rate is 67%, target is 85%
- DECISION: Redis TTL should be 3600 seconds for production (1800 for staging)
- DECISION: Worker count set to 4 for our 2-core production server (2 workers per core)
- Jake raised concern about connection pool exhaustion during traffic spikes
- DECISION: Connection pool size 20 (was 10, caused timeouts under load during last incident)
- Review of monitoring approach postponed to next sprint
- Prometheus metrics endpoint on port 9090 confirmed working

## Thursday Bug Triage (2026-02-06)

- Bug #4830: Timeout errors traced to pool_size=10 being too small (see Wednesday decision)
- Bug #4831: Health check returning 503 intermittently -- Jake investigating
- Bug #4832: Log rotation not working -- turns out log path was wrong in staging config
- No config changes needed from bug triage -- all fixes are code-level

## Friday Deployment Planning (2026-02-07)

- Target: Deploy v2.4.1 Monday morning (2026-02-10) during low traffic window
- DECISION: Log level WARNING in production (not INFO -- too noisy, generates 2GB/day)
- Sarah to handle DNS cutover for support.example.com
- Jake: Cert files already provisioned at /etc/ssl/certs/ and /etc/ssl/private/
- DECISION: Debug mode must be false in production (was accidentally true in last deploy)
- DECISION: App name standardized to customer-support-agent across all configs
- Post-deploy: monitor error rate for 2 hours before declaring success
- Rollback plan: revert to v2.3.9 container image if error rate exceeds 1%
