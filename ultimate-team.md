# The Ultimate Team — DGX Spark Agent Architecture

## The Hard Truth About Bob

Bob (gpt-oss:120b) costs **65GB** — over half our GPU. For that same 65GB we can run:
- qwen3:32b (20GB) — smarter generalist, better tool use
- qwen3:30b-a3b (19GB) — MoE miracle: 30B brain, 3B active = blazing fast, 256K context
- deepseek-r1:14b (9GB) — dedicated reasoning engine
- qwen3:14b (9.3GB) — strong secondary brain
- **Total: 57.3GB** — 4 capable specialists vs 1 generalist

Bob is a good model. But he's not 4-models-good.

---

## The Team: 7 Agents, 6 Roles, ~105GB

### 🧠 PRIME — qwen3:32b (20GB)
**Role:** Primary Intelligence / Final Decision Maker
- Best dense Qwen3 model we can run
- Excellent structured output + tool calling
- Handles: complex reasoning, code review, architecture, final-pass quality
- Context: 40K

### ⚡ FLASH — qwen3:30b-a3b (19GB) ← THE SECRET WEAPON
**Role:** Coordinator / Router / Fast Thinker
- MoE architecture: 30B total params, only 3B active
- **Faster than 8B models** with **32B-level intelligence**
- 256K context window (biggest on the team)
- Handles: task routing, coordination, memory management, quick analysis
- This model outperforms QwQ-32B per Qwen's own benchmarks

### 🔬 REASON — deepseek-r1:14b (9GB)
**Role:** Deep Reasoning / Math / Logic Specialist
- DeepSeek R1 family = purpose-built for chain-of-thought
- Handles: math problems, logical analysis, proof verification, complex debugging
- The "think harder" model when Prime needs a second opinion

### 💻 CODER — qwen3-coder (18GB)
**Role:** Code Generation / Refactoring / Analysis
- 32B parameter coding specialist
- Handles: writing code, debugging, refactoring, code review, test generation
- Best open coding model at this size

### 👁️ VISION — qwen3-vl:8b (6.1GB)
**Role:** Visual Intelligence
- Handles: image analysis, screenshot reading, diagram understanding, OCR
- Can read camera feeds, analyze UI, process documents

### 🏃 RUNNER — qwen3:14b (9.3GB)
**Role:** Versatile Worker / Execution Agent
- Strong enough to handle complex tasks independently
- Handles: research, file operations, data processing, summaries
- The reliable workhorse

### 🔍 EMBED — nomic-embed-text (0.3GB)
**Role:** Semantic Search / RAG
- Embeddings for memory search, document retrieval, similarity matching

---

## Memory Budget

| Agent | Model | VRAM |
|-------|-------|------|
| PRIME | qwen3:32b | 20 GB |
| FLASH | qwen3:30b-a3b | 19 GB |
| CODER | qwen3-coder | 18 GB |
| REASON | deepseek-r1:14b | 9 GB |
| RUNNER | qwen3:14b | 9.3 GB |
| VISION | qwen3-vl:8b | 6.1 GB |
| EMBED | nomic-embed-text | 0.3 GB |
| **TOTAL** | | **~82 GB** |

**Headroom: ~46GB free** for context growth, KV cache, and burst loading

---

## Architecture

```
         ┌─────────────┐
         │   SPARK ⚡   │  (Claude Opus, cloud API)
         │  Overseer    │  Complex strategy, creativity
         └──────┬───────┘
                │
         ┌──────▼───────┐
         │   FLASH ⚡    │  (qwen3:30b-a3b, LOCAL)
         │  Coordinator  │  Routes tasks, fast decisions
         │  256K context │  Memory manager
         └──────┬───────┘
                │
    ┌───────────┼───────────┬──────────┐
    ▼           ▼           ▼          ▼
┌───────┐ ┌─────────┐ ┌────────┐ ┌────────┐
│ PRIME │ │  CODER  │ │ REASON │ │ RUNNER │
│qwen3  │ │qwen3-  │ │deepsk  │ │qwen3   │
│ :32b  │ │ coder  │ │r1:14b  │ │ :14b   │
│       │ │        │ │        │ │        │
│Complex│ │Code    │ │Math &  │ │General │
│reasoning│ │generation│ │logic   │ │tasks   │
└───────┘ └─────────┘ └────────┘ └────────┘
                                      │
                               ┌──────▼──────┐
                               │   VISION    │
                               │ qwen3-vl:8b │
                               │ Image tasks │
                               └─────────────┘
```

## vs Old Architecture

| | Old (Bob-centric) | New (Ultimate Team) |
|---|---|---|
| GPU used | ~109GB | ~82GB |
| Free headroom | ~19GB | ~46GB |
| Agents that can think | 1 (Bob) | 6 |
| Parallel tasks | 1-2 | 4-6 |
| Fastest response | ~2min (Bob) | ~5sec (Flash) |
| Best reasoning | Bob (decent) | Prime + Reason (excellent) |
| Coding | Bob (decent) | Coder (specialist) |
| Vision | Weak (llava) | Strong (qwen3-vl) |
| 256K context | Bob only | Flash has it |
| Tool use potential | Broken | Same blocker, but more models to test |

## What Gets Removed

- `gpt-oss:120b` and `gpt-oss:120b-ctx131k` (65GB each, same weights)
- `gpt-oss:20b` (13GB, replaced by qwen3:14b)
- `qwen2.5:7b` (4.7GB, superseded by qwen3:8b)
- `qwen2.5vl:7b` (6GB, superseded by qwen3-vl:8b)
- `llava` (4.7GB, superseded by qwen3-vl:8b)
- `phi3` (2.2GB, no role)

**Disk recovered: ~160GB**

## What Gets Added

- `qwen3:30b-a3b` (19GB) — the only new download needed

## Deployment Modes

### Mode A: Full Team (~82GB)
All 6 models + embeddings loaded. Maximum capability.

### Mode B: Power Mode (~58GB)
Prime + Flash + Coder + Embed. Drop Reason/Runner/Vision. 70GB free for huge contexts.

### Mode C: Blitz (~30GB)
Flash + Runner + Embed only. 98GB free. Maximum parallel throughput.

---

## Next Steps to Deploy

1. Pull `qwen3:30b-a3b` (~19GB download)
2. Register in OpenClaw config
3. Create agent configs (SOUL.md, workspace for each)
4. Remove old models to free disk
5. Test tool calling with each model
6. Wire up Flash as coordinator
7. **Still need to fix the tool-use pipeline** — this team is more capable but faces the same blocker
