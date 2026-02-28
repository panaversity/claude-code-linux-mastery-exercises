# Exercise 3.3 — Write the Deployment Spec (Build)

## Scenario

Ali has deployed three agents manually over the past week. Each time, he had to remember the steps, look back at old terminal output, and re-discover things he already figured out. Dev says: "Write it down once. Next time, hand the spec to Claude Code and it does the whole deployment in thirty minutes."

## Your Task

Write a `DEPLOYMENT-SPEC.md` for deploying a new agent called `inventory-checker` that monitors product stock levels. Use the `spec-template.md` as your starting point.

The spec must cover all six sections:

1. **Server Requirements** — OS, memory, disk, ports needed
2. **Project Structure** — exact directory layout at `/opt/agents/inventory-checker/`
3. **Dependencies** — Python version, pip packages, system packages
4. **Secret Management** — what goes in `.env`, permissions
5. **systemd Service** — complete unit file with user, restart policy, and resource limits
6. **Verification Checklist** — how to confirm the deployment is production-ready

## Success Criteria

- [ ] All six sections are complete
- [ ] Every path is absolute
- [ ] Every permission is specified (numeric, e.g., 600)
- [ ] The unit file is complete and valid
- [ ] The verification checklist has specific expected outputs
- [ ] Someone unfamiliar with this agent could deploy it without questions

## Reflection

If Ali hands this spec to Claude Code with the instruction "Deploy this agent following the spec exactly," what could still go wrong? What assumptions does the spec make that might not hold on a different server?
