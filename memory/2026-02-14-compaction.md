# 2026-02-14 — Pre-Compaction Snapshot

## Agent Benchmarking In Progress
- qwen2.5:7b downloading (session "oceanic-shore", ~4.7GB text-only)
- Plan: benchmark qwen2.5:7b vs gpt-oss:20b, then restructure agents
- Proposed new tier: Spark (Opus) → Bob (120B) → Eyes (qwen2.5vl:7b) + Worker-1/2 (qwen2.5:7b), ~97GB/128GB
- Benchmark plan file: ~/.openclaw/workspace/agent-benchmark.md
- Optimal structure file: ~/.openclaw/workspace/optimal-agent-structure.md

## Key Finding: 20B Minis Are Too Dumb
- 8 minis on gpt-oss:20b can't collaborate, parrot each other, leak reasoning, burn GPU
- Decision: replace with fewer smarter agents once benchmarks confirm

## Cron Audit Done
- Fixed all 15 cron jobs — routed to correct agents (bob/mini-N instead of main)
- Town Hall: 10am + 4pm, Bob facilitates
- Emergency health check: every 15min via Delta
- All minis have role-specific prompts

## Ollama Models Available
- gpt-oss:120b (65GB), gpt-oss:20b (13GB), qwen2.5vl:7b (6GB), llava (4.7GB), phi3 (2.2GB)
- qwen2.5:7b downloading (~4.7GB)

## Still TODO
- Finish benchmarks → implement agent restructure
- Sesame CSM voice (needs PyTorch ARM64+CUDA, HF login)
- Electron app packaging
- Wire token pacer into API flow
- OpenAI fallback config (failed once, retry needed)
- ARA6D system architecture planning
