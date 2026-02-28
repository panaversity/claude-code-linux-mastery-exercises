# Exercise 1.4 — Permission Puzzle (Debug)

## Scenario

Ali tries to read a log file and gets "Permission denied." He tries to write to a configuration directory and gets "Permission denied" again. He can see the files exist but he cannot access them. Something about the file permissions is blocking him.

## Your Task

Examine the `simulated-server/` directory. The file `permission-listing.txt` shows the output of `ls -la` for several problematic files. For each file:

1. Decode the permission string (e.g., `-rw-------` means only the owner can read and write)
2. Explain who owns the file and what group it belongs to
3. Explain why Ali (user `ali`, group `ali`) cannot access it
4. State what the correct permissions should be and why

Create a `PERMISSION-FIXES.md` documenting each problem and its fix.

**Important:** One file has the OPPOSITE problem — it is too OPEN, not too restrictive. Find it.

## Success Criteria

- [ ] Correctly decoded all 4 permission strings
- [ ] Identified the owner and group for each file
- [ ] Explained why Ali cannot access each restricted file
- [ ] Found the file that is too open (world-readable .env)
- [ ] Proposed correct permissions for each file with justification

## Reflection

Why is a world-readable `.env` file a bigger security risk than a log file Ali cannot read? Which problem would you fix first in production?
