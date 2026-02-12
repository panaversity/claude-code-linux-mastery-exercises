# Exercise 4.1 -- Agent Log Forensics

**Build** -- Extract operational metrics from raw agent logs using text processing pipelines

## Goal

Your support agent has been running for 24 hours. Management wants a report: How many requests? What is the error rate? What are the top 5 errors? What is the average response time? What are the busiest hours? You must extract all of this from raw log files using grep, sed, awk, and pipes. Manual counting is not an option -- the log has 500+ lines.

## What You Have

- `agent.log` -- 500+ lines of structured agent logs spanning a full 24-hour period (2026-02-10 00:00 through 23:59), containing request/response pairs, errors, health checks, and system warnings.

## Your Tasks

### Step 1: Launch Claude Code
Open a terminal in this exercise directory and run `claude` to start a Claude Code session.

### Step 2: Count Total Requests
Count every line containing `Request:` in agent.log. This is your total request count for the 24-hour period.

### Step 3: Count Errors
Count every line containing `[ERROR]`. This gives you total errors.

### Step 4: Calculate Error Rate
Divide errors by total requests and multiply by 100. Express this as a percentage. You can use `awk` or `bc` for the arithmetic.

### Step 5: Find Top 5 Error Messages
Extract the error descriptions from `[ERROR]` lines, then use a `grep | sort | uniq -c | sort -rn | head -5` pipeline to rank them by frequency.

### Step 6: Calculate Average Response Time
Extract the `latency=` values from response lines, strip the `ms` suffix, and compute the average using `awk`. Note which lines have latency values and which do not.

### Step 7: Find the Busiest Hours
Extract the hour portion (HH) from timestamps on request lines, count occurrences per hour, and sort to find the peak traffic hours.

### Step 8: Find the Slowest 10 Requests
Sort all request/response pairs by latency (descending) and extract the 10 slowest. Include the timestamp, user, endpoint, and latency for each.

### Step 9: Identify Timeouts
Find all requests with a response time exceeding 5000ms. These are operational timeouts that need investigation.

### Step 10: Compile METRICS-REPORT.md
Create a METRICS-REPORT.md file in this exercise directory that contains all findings in a structured format with markdown tables and the exact command pipeline used to produce each metric.

## Expected Results

A `METRICS-REPORT.md` file containing:
- Total request count with the grep command used
- Total error count and error rate (as a percentage)
- Top 5 error messages ranked by frequency (as a table)
- Average response time in milliseconds
- Busiest hours ranked by request volume (as a table)
- The 10 slowest requests with timestamps and details
- All timeout incidents (latency > 5000ms)
- Every metric backed by the exact command pipeline that produced it

## Reflection

1. Which metric was hardest to extract? Why?
2. How would you automate this report to run daily via cron?
3. What would you add to the log format to make future analysis easier?
