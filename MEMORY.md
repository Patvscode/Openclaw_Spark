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

## AI-Scientist (Sakana)
- Repo: ~/.openclaw/workspace-bob/AI-Scientist/
- Python 3.12 venv with PyTorch 2.10.0+cu130 (CUDA working on GB10)
- Patched llm.py for Ollama: `ollama/qwen3:8b`, `ollama/qwen3:32b`, etc.
- NanoGPT template prepped (shakespeare_char dataset)
- First successful experiment run with qwen3-coder (no thinking mode!)
- Qwen3 thinking mode breaks OpenAI-compatible API (content empty, thinking eats tokens)
- qwen3-coder is the only Qwen3 model WITHOUT thinking mode — use for AI-Scientist
- DGX Spark needs cu130 wheels (not cu128/cu124) — use `--index-url https://download.pytorch.org/whl/cu130`
- sm_121 warning safe to ignore
- datasets pip package fails (pyarrow build issue) — skip it, not needed for NanoGPT

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

## Current Focus: Daily Utility (2026-02-15)
- Pat: stop tinkering with research infra, make agents useful for daily tasks
- **ARA6D postponed 2 more weeks** (Pat's call)
- Morning briefing cron: 7:30 AM EST daily (weather, AI-Scientist, GitHub, system health)
- **gh authenticated** (GitHub: Patvscode) — notifications + activity in briefing ✅
- Blocked on email/calendar: gog needs OAuth (patcodesml@gmail.com) — manual flow tried, needs browser
- FLASH promoted to coordinator — Pat talks to FLASH (@Alphamini1bot) for free local work
- FLASH can spawn CODER, RUNNER, REASON, VISION

## Lessons Learned
- AI-Scientist pipeline works end-to-end autonomously — let it run in background, don't babysit
- qwen3-coder best for AI-Scientist (no thinking mode, fast, reliable tool calls)
- Research infra has diminishing returns — pivot to practical daily value quickly
- **Don't run Opus crons frequently** — ai-scientist-monitor at 30min intervals burned all credits in hours
- Route all monitoring/routine crons to local models (FLASH) — reserve Opus for conversations only
- **FLASH is Pat's primary contact now** — I (Spark) handle complex/expensive tasks only

## Recent Major Updates (2026-02-17)
- **Switched to Sonnet 4** — saving significant money vs Opus, morning briefing also moved to FLASH
- **Qwen 3.5 released** (Feb 16) — 397B/17B active, built for agentic AI, not on Ollama yet
- **AI-Scientist scaled to 2 pipelines** — nanoGPT (2+ days, 5 experiments) + grokking (launched today)
- **Research server live** — Tailscale HTTP serving all results at 100.109.173.109:8080

## Remaining TODO
1. Complete gog OAuth (email/calendar integration) — blocked on process timeouts
2. Scale AI-Scientist to 3 pipelines tomorrow, max Thursday (original plan)
3. Build research-on-demand flow (FLASH handles)
4. Build code generation pipeline
5. Sesame CSM installation
6. Spark Hub Electron packaging
7. ARA6D planning (after 2 weeks)
