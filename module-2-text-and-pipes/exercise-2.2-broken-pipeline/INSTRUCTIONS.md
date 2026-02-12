# Exercise 2.2 -- Broken Pipeline Diagnosis

**Debug** -- Find the corrupted stage in a multi-step pipeline

## Goal

A colleague wrote a 4-stage pipeline to process agent access logs into a summary report. The pipeline runs without errors but produces wrong output. Your job: test each stage independently to find where the data gets corrupted, then fix it.

## What You Have

- `access.log` -- 200 lines of raw access log data from a support agent API
- `expected-output.txt` -- What the pipeline SHOULD produce (verified by hand count)
- `actual-output.txt` -- What the pipeline ACTUALLY produces (wrong)
- `pipeline.sh` -- The 4-stage pipeline script

## Your Tasks

### Step 1: Launch Claude Code
Open a terminal in this exercise directory and run `claude` to start a Claude Code session.

### Step 2: Read the Pipeline Script
Ask Claude Code to read `pipeline.sh` and explain what each stage does. Understand the intended data flow before running anything.

### Step 3: Compare Expected vs Actual Output
Diff `expected-output.txt` and `actual-output.txt`. Note the specific differences -- which users have wrong counts? Are there entries that should not exist?

### Step 4: Test Stage 1 Alone
Run only Stage 1 (the `grep` filter) on `access.log`. Count the output lines. Does the count match what you would expect from examining the raw log?

### Step 5: Test Stages 1-2
Pipe Stage 1 into Stage 2 (the `sed` extraction). Examine the output. Are all lines clean usernames, or is anything unexpected leaking through?

### Step 6: Test Stages 1-2-3
Add Stage 3 (the `sort | uniq -c`). Check the counts against a manual spot-check of the log.

### Step 7: Run the Full Pipeline
Run all 4 stages. Compare with `expected-output.txt`. Confirm the discrepancies match what you saw in Step 3.

### Step 8: Identify and Fix the Bugs
Determine which stage(s) introduce errors and why. Fix the pipeline so its output matches `expected-output.txt`.

### Step 9: Write DIAGNOSIS.md
Document your findings with this structure:
- Which stage(s) had bugs
- What the bug was in each case
- How you discovered it (which test step revealed it)
- The fix you applied
- Before/after output comparison

## Expected Results

- Identified all bugs in the pipeline
- A fixed version of `pipeline.sh` that produces output matching `expected-output.txt`
- `DIAGNOSIS.md` with a systematic trace of the debugging process

## Reflection

1. If you had only compared final output (skipping the stage-by-stage trace), could you have found all the bugs?
2. What does "testing each stage independently" look like for other tools beyond shell pipes?
3. How would you prevent this class of bug in future pipelines?
