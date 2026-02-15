# AI-Scientist Autonomous Research Pipeline
## DGX Spark — Built 2026-02-15

## Overview
Fully autonomous research pipeline running Sakana AI's AI-Scientist framework locally on a DGX Spark (GB10 GPU, 128GB unified RAM, CUDA 13.0). Uses local Ollama models (zero API cost) to generate research ideas, write experiment code, run GPU training, debug errors, and produce LaTeX papers.

## Architecture

```
┌─────────────────────────────────────────────────┐
│              AI-Scientist Pipeline               │
│                                                  │
│  1. IDEA GENERATION                              │
│     qwen3-coder → generates research ideas       │
│     3 iterations per idea (refine until converge) │
│                                                  │
│  2. EXPERIMENT CODING                            │
│     aider + qwen3-coder → modifies experiment.py │
│     Up to 5 run variants per idea                │
│                                                  │
│  3. GPU TRAINING                                 │
│     PyTorch cu130 on GB10 → trains NanoGPT       │
│     ~15 min per run (5000 iters, 10.65M params)  │
│                                                  │
│  4. ERROR HANDLING                               │
│     If training crashes → error fed back to LLM  │
│     LLM debugs and rewrites code → retry         │
│                                                  │
│  5. PAPER WRITING (when all runs complete)        │
│     LLM writes LaTeX paper comparing results     │
│     Against baseline (val_loss=1.47, 893s)       │
└─────────────────────────────────────────────────┘
```

## Key Components

### Models
- **qwen3-coder** (18GB): Primary research brain. Chosen because it has NO thinking mode — Qwen3 models with thinking mode return empty content via OpenAI-compatible API (thinking tokens eat the budget).
- **Baseline**: NanoGPT 10.65M params on Shakespeare character-level dataset.

### Files & Directories
- **AI-Scientist repo**: `~/.openclaw/workspace-bob/AI-Scientist/`
- **Patched LLM module**: `ai_scientist/llm.py` (Ollama integration via `_OLLAMA_ACTIVE` flag)
- **Templates**: `templates/nanoGPT/` (experiment.py, data/shakespeare_char/)
- **Baseline results**: `templates/nanoGPT/run_0/final_info_shakespeare_char_0.json`
- **Experiment results**: `results/nanoGPT/<timestamp>_<idea_name>/`
- **Runner script**: `~/.openclaw/workspace/ai-scientist-runner.sh`
- **Logs**: `~/.openclaw/workspace/ai-scientist-logs/`
- **Status file**: `ai-scientist-logs/status.json`

### Systemd Service
```bash
# Check status
systemctl --user status ai-scientist

# Stop
systemctl --user stop ai-scientist

# Restart
systemctl --user restart ai-scientist

# View logs
journalctl --user -u ai-scientist -f

# View run log
tail -f $(ls -t ~/.openclaw/workspace/ai-scientist-logs/run_*.log | head -1)
```

Service config: `~/.config/systemd/user/ai-scientist.service`
- Auto-restarts on failure (60s delay)
- Max 3 restarts per 10 minutes
- Environment variables for model/ideas/experiment

### Monitoring
- Cron job `ai-scientist-monitor` runs every 30 minutes
- Reports to Telegram via OpenClaw announce
- Checks: service status, status.json, result files, latest log tail

## Bugs Fixed
1. **KeyError 'novel'**: `--skip-novelty-check` skips adding `novel` key but code filtered on it. Fix: `.get("novel", True)`
2. **final_info filename mismatch**: Experiment writes `final_info_shakespeare_char_0.json`, launcher expects `final_info.json`. Fix: glob fallback.
3. **baseline_results parsing**: Some results are flat dicts, code expected nested `{"means": ...}`. Fix: check structure before extracting.
4. **Qwen3 thinking mode**: All Qwen3 models (8b, 14b, 30b-a3b, 32b) have thinking ON by default. Via OpenAI-compatible API, thinking goes to `reasoning` field and `content` is empty. Fix: use qwen3-coder (no thinking mode).
5. **PyTorch CPU-only**: Default pip install gets CPU torch. Fix: `--index-url https://download.pytorch.org/whl/cu130` for aarch64 CUDA wheels.
6. **Python.h missing**: Triton/inductor compilation needs python3-dev. Fix: `apt install python3-dev`.
7. **Process death on exec cleanup**: nohup child killed when OpenClaw exec session ends. Fix: systemd service.

## DGX Spark Specifics
- CUDA 13.0 — needs cu130 wheels (not cu128/cu124)
- sm_121 warning is safe to ignore (binary compatible with sm_120)
- PyTorch 2.10.0+cu130 from `https://download.pytorch.org/whl/cu130`
- Unified memory: GPU OOM = system OOM. Be careful with batch sizes.
- Reference guide: github.com/natolambert/dgx-spark-setup

## Environment Variables
```bash
AI_SCIENTIST_MODEL=ollama/qwen3-coder   # Which Ollama model
AI_SCIENTIST_IDEAS=3                     # Ideas per run
AI_SCIENTIST_EXPERIMENT=nanoGPT          # Template to use
TORCH_CUDA_ARCH_LIST=12.1a              # Blackwell arch
PYTHONUNBUFFERED=1                       # Real-time logging
```

## Available Templates
- nanoGPT (active — Shakespeare character-level LM)
- 2d_diffusion, grokking, MACE, mobilenetV3, nanoGPT_lite, probes, seir, sketch_rnn, tensorf, earthquake-prediction

## Future Improvements
1. Auto-loop: restart with new ideas after completing a batch
2. Quality gate: auto-evaluate results, discard bad ones
3. FLASH coordinator: decide which templates/ideas to prioritize
4. Parallel runs: multiple templates running simultaneously
5. Morning digest: summarize overnight results for human review
6. Paper review: use a second model to peer-review generated papers
