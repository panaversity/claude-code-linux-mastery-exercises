# Exercise 2.1 — Agent Home Setup (Build)

## Scenario

Ali is deploying a new agent — a social-media-monitor that tracks brand mentions. He needs to set up the complete directory structure on the server before any code runs.

## Your Task

Create the full project structure for a social-media-monitor agent. The structure should follow Linux best practices for agent deployment:

```
social-monitor/
├── src/           # Python source code
├── config/        # Configuration files
│   └── .env       # API keys (must be permission 600)
├── logs/          # Log output (must be writable by agent user)
├── data/          # Output files
└── README.md      # What this agent does and how to run it
```

Create each directory and file. The `.env` file should contain placeholder API keys. Write a realistic README.md.

## Success Criteria

- [ ] All 4 subdirectories created (src/, config/, logs/, data/)
- [ ] `.env` file exists with placeholder keys
- [ ] README.md explains the agent's purpose and how to run it
- [ ] `.env` file would have 600 permissions (note this in your work)
- [ ] logs/ directory would be writable by the agent user

## Reflection

Why does Ali create the directory structure before writing any code? What would happen if he just dumped all files in one flat directory?
