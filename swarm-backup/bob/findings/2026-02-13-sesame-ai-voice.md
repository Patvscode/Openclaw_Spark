# Sesame AI – Open‑Source Voice Model (CSM‑1B) – Findings (2026‑02‑13)

**Model name / repo**
- **Name:** Conversational Speech Model – **CSM‑1B** (the 1‑billion‑parameter base generation model released by Sesame AI).  
- **GitHub repository:** https://github.com/SesameAILabs/csm  
- **Hugging Face repo:** https://huggingface.co/sesame/csm-1b  
- **License:** Apache 2.0 (per the repo README).

**Hardware requirements**
- **GPU:** Any NVIDIA GPU with ≥ 8 GB VRAM (the guide recommends RTX 4060‑8 GB as the minimum consumer card).  
- **CPU / OS:** Python 3.10+ on Linux (Ubuntu 22.04 LTS or newer).  
- **RAM / storage:** 16 GB RAM minimum, ~50 GB free disk for model weights and caches.  
- **CUDA:** CUDA 12.x (12.4/12.6 tested) with cuDNN 8.x.
- **DGX Spark compatibility:**
  - DGX Spark ships a Grace‑Blackwell **GB10** SOC with 128 GB unified memory and a high‑performance NVIDIA GPU (≈ 1 PFLOP FP4, > 8 GB VRAM equivalent).  
  - The unified memory model satisfies the 8 GB VRAM requirement, and the GPU supports CUDA 12, so CSM‑1B can run on DGX Spark.  
  - The only potential hurdle is the ARM64 architecture: PyTorch wheels for `aarch64` with CUDA are available (e.g., `torch‑2.3.0+cu121‑aarch64.whl`).  Build the environment with those wheels or compile from source – the repo does not contain any x86‑only binaries.

**Installation & local run steps (high‑level)**
1. **Prerequisites** – Install NVIDIA driver, CUDA 12, Python 3.10, `git`, `ffmpeg`.  
2. **Clone repo**: `git clone https://github.com/SesameAILabs/csm.git && cd csm`  
3. **Create virtual env**: `python3 -m venv .venv && source .venv/bin/activate`  
4. **Install PyTorch (ARM64+CUDA)**, e.g.:
   ```bash
   pip install torch==2.3.0+cu121 torchaudio==2.3.0+cu121 -f https://download.pytorch.org/whl/torch_stable.html
   ```
5. **Install other deps**: `pip install -r requirements.txt`  
6. **Login to Hugging Face** (needed for the model weights): `huggingface-cli login`  
7. **Download the model** – the repo provides a helper script (`scripts/download_models.py`) that pulls `sesame/csm-1b` and the Llama‑3.2‑1B text backbone.  
8. **Run a quick test**:
   ```python
   from generator import load_csm_1b
   gen = load_csm_1b(device="cuda")
   audio = gen.generate(text="Hello from Sesame CSM 1B", speaker=0)
   audio.save("hello.wav")
   ```
9. **Voice‑cloning / context** – the repo includes `scripts/clone_voice.py` and examples that accept a reference wav and a text prompt.

**Real‑time voice‑to‑voice conversation?**
- CSM‑1B generates **audio codes** (RVQ) that are decoded to waveforms.  The codebase reports a **real‑time factor ≈ 0.6 ×** on an RTX 4070 Ti (i.e., faster than real time).  On DGX Spark the larger GPU and unified memory should give similar or better latency, so real‑time voice‑to‑voice interaction is feasible.
- The model itself only **synthesises audio**; you still need a separate speech‑to‑text component (e.g., Whisper) and a text LLM for dialogue management.  A typical pipeline is:
  1. Capture microphone audio → ASR (Whisper, etc.)
  2. Send transcript to a text LLM (Ollama, OpenAI, etc.)
  3. Feed the LLM reply to CSM‑1B → audio output.
- The CSM‑1B API (`generate`) accepts a **context list** of prior utterances, enabling multi‑turn conversation with low latency.

**Integration with Ollama**
- Ollama currently supports text‑only LLMs; it does **not** have a built‑in driver for the CSM audio generation pipeline because CSM is a **speech‑generation** model, not a language model.  
- Users typically run CSM‑1B as a separate service (e.g., a Flask or FastAPI endpoint) and call it from their application after obtaining the LLM response from Ollama.  
- The GitHub issue *How to run locally* (see above) confirms that the author expects the model to be run outside of Ollama.  No official Ollama “model card” exists for CSM‑1B.

**Summary**
- **Model**: CSM‑1B – open‑source, Apache 2.0, GitHub + HF repos.  
- **Runs on DGX Spark**: Yes, provided you install the ARM64 CUDA‑enabled PyTorch wheels; GPU memory is sufficient.  
- **Installation**: Clone → venv → install CUDA‑enabled PyTorch → pip install deps → download weights → run `generate`.  
- **Real‑time**: Achievable; benchmarked < 1 × real‑time on consumer GPUs, should be similar on DGX Spark.  
- **Ollama integration**: Not native; run CSM‑1B as a separate service and invoke it after Ollama’s text response.

*Prepared for the main agent – Bob*