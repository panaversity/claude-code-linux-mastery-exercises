#!/bin/bash
# ============================================================
# Pipeline: Process access.log into a per-user request summary
#
# Data flow:
#   access.log
#     → Stage 1: Filter only /api/chat requests
#     → Stage 2: Extract username from each line
#     → Stage 3: Count requests per user
#     → Stage 4: Sort by count (descending) and format as report
#
# Expected behavior:
#   - Count only /api/chat endpoint requests (not chat-history,
#     feedback, health, models, etc.)
#   - Group by username
#   - Sort most active users first
#   - Output a clean formatted report
# ============================================================

cat access.log \
  | grep "/api/chat" \
  | sed 's/.*user=//g' \
  | sort \
  | uniq -c \
  | sort -rn \
  | awk '{printf "%-15s %d requests\n", $2, $1}'
