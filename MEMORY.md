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

## TownHall Group Chat (Temporary)
- Chat ID: -5195425739
- Append to every message I send there: @Alphamini1bot @Betamini2bot @Deltamini4bot @Gammamini3bot @Opclpmbot
- Temporary until Pat configures @-free visibility for all bots

## Environment
- DGX Spark: 20-core ARM64, 128GB RAM, GB10 GPU, 3.7TB NVMe
- Telegram paired (Pat's user ID: 7827979987)
- OpenClaw multi-agent: main (Spark/Opus) + bob (GPT-OSS-120B/Ollama)
- Workspace backed up to GitHub: Patvscode/Openclaw_Spark (daily auto-backup at noon via cron → Bob)

## Agent Delegation — Ultimate Team (2026-02-15)
- **FLASH** (qwen3:30b-a3b, 19GB): sessions_spawn(agentId="flash") — **MVP**, fastest, perfect tool use, MoE, 256K ctx
- **CODER** (qwen3-coder, 18GB): sessions_spawn(agentId="coder") — web_fetch expert, needs format fix
- **PRIME** (qwen3:32b, 20GB): sessions_spawn(agentId="prime") — deep analysis, exec works, slow multi-step
- **RUNNER** (qwen3:14b, 9.3GB): sessions_spawn(agentId="runner") — fast worker, tools work
- **REASON** (qwen3:14b, 9.3GB): sessions_spawn(agentId="reason") — reasoning specialist
- **VISION** (qwen3-vl:8b, 6.1GB): sessions_spawn(agentId="vision") — visual intelligence
- **Bob** (gpt-oss:120b, 65GB): sessions_spawn(agentId="bob") — reserve, not loaded by default
- Total ~82GB, 46GB headroom. OLLAMA_NUM_PARALLEL=3.
- GitHub backup: Patvscode/Openclaw_Spark

## Tool-Use Breakthrough (2026-02-15)
- Qwen3 CAN use tools — fix: tool name hints in SOUL.md (exec/write/read not run/write_file/read_file)
- DeepSeek R1 CANNOT use tools at all
- FLASH is most reliable; gateway restarts kill running tasks
