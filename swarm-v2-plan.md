# Swarm v2: Self-Improving Multi-Agent System
*Plan created 2026-02-14*

## Architecture

### Hierarchy
```
Spark (Opus API) — Architect, final decisions, complex reasoning
  └── Bob (120B) — Manager, research lead, delegation
        └── Alpha (14B) — Swarm coordinator, synthesis
              ├── Beta (8B) — Documentarian
              ├── Gamma (8B) — QA/Testing  
              ├── Delta (8B) — Health/Monitoring
              ├── Echo (8B) — Git/DevOps
              ├── Foxtrot (8B) — Frontend
              ├── Golf (8B) — Research
              └── Hotel (8B) — Backend

Specialists (loaded on demand):
  - qwen3-coder (18GB) — Deep coding tasks
  - qwen3:32b (20GB) — Heavy analysis
  - deepseek-r1:14b (9GB) — Reasoning/math
  - qwen3-vl:8b (6GB) — Vision tasks
  - nomic-embed-text (274MB) — RAG/embeddings
```

### Self-Improvement Loop
1. **Monitor** — Delta tracks health, performance, error rates per agent
2. **Evaluate** — Alpha reviews task completion quality weekly
3. **Propose** — Any agent can propose improvements via comms/proposals/
4. **Vote** — 5/8 majority approves changes
5. **Implement** — Bob or Spark executes approved changes
6. **Log** — All changes tracked in comms/changelog.md

### Self-Regulation Rules
- Agents check their own output quality before submitting
- If an agent fails 3 tasks in a row, Alpha escalates to Bob
- Bob can reassign roles or request model swaps
- GPU memory monitored — auto-unload idle models after 10min
- Task queue prevents overloading (max 3 concurrent local inference)

### Scalability
- New agents added by: create workspace + config entry + SOUL.md
- Model library grows independently of agent count
- Specialists load/unload dynamically based on task type
- File-based coordination (comms/) scales without network overhead
