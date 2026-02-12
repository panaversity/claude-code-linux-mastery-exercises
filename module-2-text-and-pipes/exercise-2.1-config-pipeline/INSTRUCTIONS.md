# Exercise 2.1 -- Config Pipeline

**Build** -- Assemble agent configurations from scattered fragments

## Goal

An agent deployment requires 3 config files (`nginx.conf`, `app-config.yaml`, `.env.production`) but the values are scattered across multiple source files -- a defaults template, an environment override file, team notes, and a secrets reference. Use text tools (`cat`, `grep`, `sed`, pipes, redirection) to assemble the final configs.

## What You Have

- `config-fragments/` -- A directory containing:
  - `defaults.template` -- Base config with placeholder values (`PLACEHOLDER_*`) for all three output files
  - `env-overrides.txt` -- Production-specific values in `KEY=VALUE` format
  - `team-notes.md` -- Sprint meeting notes with config decisions buried inside (look for `DECISION:` prefix)
  - `secrets-reference.txt` -- Secret names and which config they belong to (vault references, NOT actual values)
  - `port-assignments.csv` -- CSV mapping of service name, port, protocol, and notes

## Your Tasks

### Step 1: Launch Claude Code
Open a terminal in this exercise directory and run `claude` to start a Claude Code session.

### Step 2: Read All Source Files
Ask Claude Code to read every file in `config-fragments/` so you understand what values exist where. Note which placeholders appear in the template and which source file provides each value.

### Step 3: Extract the Production Port
Use `grep` and `cut` on `port-assignments.csv` to extract the external nginx port (443) and the internal app port (8080).

### Step 4: Extract KEY=VALUE Pairs
Use `grep` on `env-overrides.txt` to extract all non-comment lines containing `=`. These are your production values.

### Step 5: Extract Buried Config Decisions
Use `grep` on `team-notes.md` to find lines with the `DECISION:` prefix. These confirm values that should appear in the final configs.

### Step 6: Assemble nginx.conf
Starting from the nginx section of `defaults.template`, use `sed` to replace each `PLACEHOLDER_*` token with the correct production value. Pipe multiple `sed` commands together or use `-e` flags. Redirect the result to `nginx.conf`.

### Step 7: Assemble app-config.yaml
Extract the app config section from `defaults.template` and replace all placeholders with values from `env-overrides.txt`. Redirect the result to `app-config.yaml`.

### Step 8: Assemble .env.production
Combine the environment variable values from `env-overrides.txt` with the vault references from `secrets-reference.txt` to produce a complete `.env.production` file.

### Step 9: Verify No Placeholders Remain
Run this check against each assembled file:
```bash
grep -c 'PLACEHOLDER\|TODO\|XXX' <file>
```
Every file should return `0`. If any placeholders remain, go back and fix your pipeline.

### Step 10: Document Your Work
Create a `PIPELINE-LOG.md` that records each command pipeline you used and what it produced.

## Expected Results

- `nginx.conf` -- A valid nginx server block with all placeholders replaced by production values
- `app-config.yaml` -- A valid YAML config with all production values filled in
- `.env.production` -- Environment variables with real values plus vault references for secrets
- `PIPELINE-LOG.md` -- A log showing each pipeline command and its purpose
- Zero remaining placeholders in any assembled file

## Reflection

1. Which config was hardest to assemble? Why?
2. How many pipe stages did your longest pipeline have?
3. Could you turn your pipeline commands into a reusable script? What would make that script more robust than manual piping?
