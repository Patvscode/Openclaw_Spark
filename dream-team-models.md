# 🏆 Dream Team: Best Open-Source Models for DGX Spark
*Compiled 2026-02-14 | 128GB unified VRAM | ARM64 + GB10 GPU*

## The Landscape (as of Feb 2026)
The open-source model ecosystem has exploded. Key families:
- **Qwen3** (Alibaba) — dominant across text, code, vision, reasoning
- **DeepSeek** — V3.2 for general, R1 for reasoning, Coder V3 for code
- **Llama 4** (Meta) — strong general purpose
- **FLUX.2** (Black Forest Labs) — leading image generation
- **Sesame CSM / F5-TTS / CosyVoice 3** — TTS leaders

---

## Category Winners

### 💬 General Chat/Text
| Model | Params | VRAM (Q4) | Why |
|-------|--------|-----------|-----|
| **Qwen3-32B** | 32B dense | ~20GB | Sweet spot — beats many 70B models, thinking+non-thinking modes |
| **Qwen3-30B-A3B** (MoE) | 30B total/3B active | ~18GB | MoE efficiency — fast inference, only 3B active params |
| **Qwen3-8B** | 8B dense | ~5GB | Best small model, thinking mode, tool use |
| **Qwen3-14B** | 14B dense | ~10GB | Mid-tier workhorse |

### 💻 Coding
| Model | Params | VRAM (Q4) | Why |
|-------|--------|-----------|-----|
| **Qwen3-Coder-30B-A3B** (MoE) | 30B/3B active | ~18-20GB | Top open coding model, 256K+ context, 100+ languages, agentic |
| **DeepSeek-Coder-V3** | varies | varies | Less hallucination than Qwen on TypeScript per community |
| **Qwen2.5-Coder-32B** | 32B | ~20GB | Still excellent, proven track record |

### 👁️ Vision/Multimodal
| Model | Params | VRAM (Q4) | Why |
|-------|--------|-----------|-----|
| **Qwen3-VL-8B** | 8B | ~6GB | Best small vision model, available on Ollama |
| **Qwen3-VL-32B** | 32B | ~22GB | SOTA open-source vision (when VRAM available) |
| **MiniCPM-V 2.6** | 8.1B | ~5.5GB | Tiny but capable, 32K context |
| **InternVL3-78B** | 78B | ~48GB | SOTA benchmarks (full GPU mode only) |

### 🧠 Reasoning/Math
| Model | Params | VRAM (Q4) | Why |
|-------|--------|-----------|-----|
| **DeepSeek-R1-Distill-Qwen-32B** | 32B | ~20GB | Best distilled reasoning model, beats QwQ |
| **DeepSeek-R1-Distill-Qwen-14B** | 14B | ~10GB | Outperforms QwQ-32B at half the size |
| **QwQ-32B** | 32B | ~20GB | Strong at coding reasoning |
| **Qwen3-32B** (thinking mode) | 32B | ~20GB | Built-in reasoning toggle |

### 🎤 Audio/Speech
| Model | Type | Size | Why |
|-------|------|------|-----|
| **Sesame CSM** | TTS | 1B (~2GB) | Most natural conversational voice, Llama-based |
| **F5-TTS** | TTS | ~1GB | MIT license, fast, good quality |
| **CosyVoice 3.0** | TTS | varies | Alibaba's latest, multilingual, voice cloning |
| **Whisper Large-v3** | STT | ~3GB | Still the king of transcription |
| **SenseVoice** | STT | varies | Alibaba's alternative, very fast |

### 📎 Embeddings/RAG
| Model | Dims | VRAM | Why |
|-------|------|------|-----|
| **Nomic Embed v2** | varies | ~1-5GB | Top open-source recall, available on Ollama |
| **BGE-M3** | varies | ~2GB | Best multilingual, 63.0 MTEB |
| **MiniLM-L6-v2** | 384 | ~1.2GB | Edge-friendly, blazing fast |

### 🎨 Image Generation
| Model | Params | VRAM | Why |
|-------|--------|------|-----|
| **FLUX.1 Dev** | 12B | ~12-16GB | Best open-weight quality, rect flow transformer |
| **FLUX.2 Dev** | varies | ~16GB+ | Latest generation (if available) |
| **Stable Diffusion 3.5 Large** | varies | ~8-12GB | Good alternative, well-supported |
| **Qwen-Image-2512** | varies | ~16GB | Surprisingly good, GGUF Q4 fits 16GB |

### 🛠️ Agent/Tool Use
| Model | Params | VRAM (Q4) | Why |
|-------|--------|-----------|-----|
| **Qwen3-8B** (thinking mode) | 8B | ~5GB | Native tool use, agentic, small footprint |
| **Qwen3-30B-A3B** | 30B MoE | ~18GB | Best agent model among open-source per benchmarks |
| **Qwen3-Coder-30B-A3B** | 30B MoE | ~18-20GB | Agentic coding specifically |

---

## 🎯 Recommended Team Configs

### Config A: "Everyday" (Bob loaded, ~63GB free)
| Role | Model | VRAM | Notes |
|------|-------|------|-------|
| 🧠 Manager | Bob (GPT-OSS 120B) | 65GB | Already loaded, research + delegation |
| 🛠️ Worker | Qwen3-8B | ~5GB | Fast general tasks, tool use, agent mode |
| 👁️ Eyes | Qwen3-VL-8B | ~6GB | Vision tasks, screenshots, diagrams |
| 💻 Coder | (share Qwen3-8B or Qwen3-Coder-30B-A3B) | 0-20GB | 8B for quick, 30B for serious coding |
| 📎 Embeddings | Nomic Embed v2 | ~1GB | RAG support |
| 🎤 TTS | Sesame CSM | ~2GB | Voice output |
| **Total** | | **~79-99GB** | Fits with room to spare |

### Config B: "Full Power" (Bob unloaded, 128GB free)
| Role | Model | VRAM | Notes |
|------|-------|------|-------|
| 💬 General | Qwen3-32B | ~20GB | Best all-rounder with thinking mode |
| 💻 Coder | Qwen3-Coder-30B-A3B | ~20GB | Top coding with 256K context |
| 👁️ Eyes | Qwen3-VL-32B | ~22GB | SOTA vision |
| 🧠 Reasoning | DeepSeek-R1-Distill-Qwen-32B | ~20GB | Heavy reasoning tasks |
| 🎨 Image | FLUX.1 Dev | ~16GB | Image generation |
| 📎 Embeddings | Nomic Embed v2 | ~1GB | RAG |
| 🎤 TTS | Sesame CSM | ~2GB | Voice |
| **Total** | | **~101GB** | Fits! Swap models as needed |

### Config C: "Swarm Blitz" (Bob unloaded, max parallel agents)
| Role | Model | VRAM | Instances |
|------|-------|------|-----------|
| Workers | Qwen3-8B | ~5GB each | x8 = 40GB |
| Coder | Qwen3-Coder-30B-A3B | ~20GB | x1 |
| Vision | Qwen3-VL-8B | ~6GB | x1 |
| Coordinator | Qwen3-14B | ~10GB | x1 |
| Embeddings | Nomic Embed v2 | ~1GB | x1 |
| **Total** | | **~77GB** | 10 parallel agents! |

---

## 🔥 Priority Downloads (via Ollama)
```bash
# Immediate — replace current 20B minis
ollama pull qwen3:8b              # ~5GB — best small all-rounder
ollama pull qwen3-coder:30b-a3b   # ~18GB — coding beast (MoE, only 3B active)
ollama pull qwen3-vl:8b           # ~6GB — vision upgrade from qwen2.5vl:7b

# Next wave
ollama pull qwen3:32b             # ~20GB — full power mode
ollama pull deepseek-r1:14b       # ~10GB — reasoning specialist
ollama pull nomic-embed-text      # ~300MB — embeddings for RAG

# When ready for voice
# Sesame CSM (manual install from HuggingFace, not on Ollama)
# F5-TTS (pip install, lightweight alternative)

# When ready for images
# FLUX.1 Dev via ComfyUI or diffusers (not on Ollama)
```

## Key Insight
**Qwen3 dominates every category.** The MoE variants (30B-A3B) are genius — 30B total params but only 3B active at inference, so they're fast AND smart. This is the architecture that makes our swarm actually viable.

The biggest upgrade: replacing gpt-oss:20b minis with qwen3:8b workers. Smaller, faster, smarter, no reasoning leakage, native tool use.
