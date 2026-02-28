# Exercise 2.2 — The Missing Pieces (Debug)

## Scenario

Ali comes back to a server where an intern set up a project directory, but several things are wrong. The agent keeps failing on startup and nobody can figure out why.

## Your Task

Examine the `broken-project/` directory. It represents `/opt/agents/data-collector/` set up by an intern. Find and document ALL problems:

1. Check the `.env` file permissions (listed in `audit-output.txt`)
2. Check if the `logs/` directory exists
3. Check if source code is properly organized
4. Check for documentation
5. Check for unnecessary files wasting disk space

Create a `FIX-REPORT.md` listing every problem, its severity (security/functionality/organization), and the fix — in order of severity (security first).

## Success Criteria

- [ ] Found the world-readable .env file (security issue)
- [ ] Found the missing logs/ directory (functionality issue)
- [ ] Found the unorganized source code (organization issue)
- [ ] Found the missing README (documentation issue)
- [ ] Found the bloated node_modules (disk waste issue)
- [ ] Prioritized fixes correctly: security → functionality → organization

## Reflection

The intern's setup "almost worked." Why is "almost works" dangerous in production? What is the difference between "runs" and "runs correctly"?
