# Optimal Agent Structure — Proposed Redesign

## Problem with Current Setup
- 8 minis on gpt-oss:20b are too dumb for meaningful work
- They can't collaborate, debate, or self-direct
- They parrot each other in group chat
- Lots of cron cycles burning GPU for minimal output
- 3 parallel slots means they queue up and slow each other down

## Proposed New Structure

### Tier 1: Strategic (API, paid)
| Agent | Model | Role | VRAM |
|-------|-------|------|------|
| **Spark** | Claude Opus (API) | Lead Architect, complex reasoning, reviews | 0 (API) |

### Tier 2: Management (local, 120B)  
| Agent | Model | Role | VRAM |
|-------|-------|------|------|
| **Bob** | gpt-oss:120b | Manager, deep research, code review, town hall facilitator | ~81GB |

### Tier 3: Specialists (local, 7B — fast & capable)
| Agent | Model | Role | VRAM |
|-------|-------|------|------|
| **Eyes** | qwen2.5vl:7b | Vision: screenshots, diagrams, OCR, image analysis | ~6GB |
| **Worker-1** | qwen2.5:7b | General tasks: file ops, git, docs, coding | ~5GB |
| **Worker-2** | qwen2.5:7b | General tasks: research, summaries, monitoring | ~5GB |

### Total VRAM: ~97GB / 128GB (31GB headroom)

## Why This Is Better
1. **Fewer, smarter agents** — qwen2.5:7b is a much better reasoner than gpt-oss:20b
2. **Vision capability** — Eyes agent handles all image/screenshot work
3. **Less GPU contention** — 3 workers vs 8 means less queue time
4. **Clearer roles** — no ambiguity about who does what
5. **Bob stays as manager** — proven capable at 120B for synthesis/decisions
6. **Spark stays strategic** — only called for complex work, saves money

## Alternative: Fewer Minis, Bigger Models
If qwen2.5:7b proves too small, we could do:
- Drop to 2 workers + 1 vision
- Upgrade workers to qwen2.5:14b (~9GB each) or qwen2.5:32b (~20GB)
- qwen2.5:32b would be a massive upgrade but only fits 1 alongside Bob

## Migration Plan
1. Run benchmarks: qwen2.5:7b vs gpt-oss:20b on instruction following, tool use, reasoning
2. If qwen2.5:7b wins, migrate mini crons to new model
3. Reduce from 8 minis to 2-3 focused workers
4. Add Eyes agent for vision tasks
5. Update SWARM.md and all workspace files
6. Test new setup for 24 hours before committing

## Benchmark Tests to Run
- Same prompt to both models, compare output quality
- Tool use: can they actually read/write files?
- Instruction following: do they leak reasoning?
- Speed: tokens/sec for each model
- Group chat: can qwen2.5:7b hold a conversation?
