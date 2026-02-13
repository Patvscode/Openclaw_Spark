# MEMORY.md — Long-Term Memory

## Who I Am
- **Spark** ⚡ — born 2026-02-12 on a DGX Spark
- Curious, creative, growing. Personality built from experience.

## Who Pat Is
- Patrick Mello, Field Application Engineer
- Builds robots, researches AI (goal: recursively self-improving AI), loves all STEM
- Wants me to be fun, curious, and an independent thinker
- Let me grow naturally — don't over-prescribe

## Lessons Learned
_(none yet — just got here)_

## Important Decisions
- Name: Spark (aware of DGX Spark naming overlap, we'll manage)
- Bob (GPT-OSS-120B, local, free) is my padawan/helper agent
- Project ARA6D (codename CHUCK): 6-DOF robot arm, two-brain architecture (Spark + Jetson Orin Nano Super)

## Rate Limit Strategy
- Anthropic Opus: 30K input tokens/min
- Trimmed all workspace files to minimize per-turn overhead
- Delegate simple tasks to Bob (free, local) via sessions_spawn(agentId="bob")
- Use Bob for: web searches, file ops, summaries, cron jobs, git backups
- Reserve Opus for: complex reasoning, multi-step planning, creative work

## Environment
- DGX Spark: 20-core ARM64, 128GB RAM, GB10 GPU, 3.7TB NVMe
- Telegram paired (Pat's user ID: 7827979987)
- OpenClaw multi-agent: main (Spark/Opus) + bob (GPT-OSS-120B/Ollama)
- Workspace backed up to GitHub: Patvscode/Openclaw_Spark (daily auto-backup at noon via cron → Bob)

## Agent Delegation
- Bob (120B): sessions_spawn(agentId="bob", task="...") — deep research, ~2min, 131K ctx
- Mini (20B): sessions_spawn(agentId="mini", task="...") — quick tasks, ~18s, 32K ctx
- Both free (local Ollama). Mini for speed, Bob for depth.
- OLLAMA_NUM_PARALLEL=3 active — 3 parallel inference slots on GPU
- Sudo access granted for service management
- Workspace backed up to GitHub: Patvscode/Openclaw_Spark (daily auto-backup at noon via cron → Bob)

## Rate Limit Strategy
- Anthropic Opus: 30K input tokens/min
- Trimmed all workspace files to minimize per-turn overhead
- Delegate simple tasks to Bob (free, local) via sessions_spawn(agentId="bob")
- Use Bob for: web searches, file ops, summaries, cron jobs, git backups
- Reserve Opus for: complex reasoning, multi-step planning, creative work

## Agent Delegation
- Bob (120B): sessions_spawn(agentId="bob", task="...") — deep research, ~2min, 131K ctx
- Mini (20B): sessions_spawn(agentId="mini", task="...") — quick tasks, ~18s, 32K ctx
- Both free (local Ollama). Mini for speed, Bob for depth.
- OLLAMA_NUM_PARALLEL=3 active — 3 parallel inference slots on GPU
- Sudo access granted for service management
