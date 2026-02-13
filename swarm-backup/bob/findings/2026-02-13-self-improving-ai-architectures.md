# Findings: Best Practices for Recursively Self‑Improving AI Architectures (2024‑2026)

**Scope** – Survey of recent (2024‑2026) papers, workshops, and community resources on recursive self‑improvement (RSI) for AI systems. Focus on architectural patterns, training loops, safety mechanisms, and practical implementation guidelines.

---

## 1. Key Architectural Themes

| Theme | Description | Representative Works (2024‑2026) |
|-------|-------------|-----------------------------------|
| **Self‑Taught Optimiser (STOP)** – a scaffolding program that iteratively rewrites its own code/training data using a fixed LLM. | Emphasises a *fixed* core model that stays stable while peripheral modules evolve. | Wikipedia entry (2024) notes STOP framework; Guo et al. 2025 implementation (openreview.net PDF).
| **Recursive Self‑Aggregation (RSA)** – multiple reasoning chains are aggregated at each refinement step to boost correctness without massive compute. | Uses population‑based refinement and ensemble voting. | Venkatraman et al., *Recursive Self‑Aggregation* (arXiv:2509.26626, 2025).
| **Test‑time Recursive Thinking (TRT)** – self‑improvement occurs at inference time via internal feedback loops, no external reward signal needed. | Leverages model’s own predictions to generate corrective prompts. | "Test‑time Recursive Thinking" (arXiv:2602.03094, 2024).
| **Self‑Referential Agent Framework (SRAF)** – agents maintain explicit meta‑knowledge of their own architecture and can modify it via a learned *meta‑controller*. | Formalizes the agent’s self‑model and uses reinforcement learning to update it. | ACL‑Long 2025 paper (aclanthology.org/2025.acl‑long.1354.pdf).
| **Dual‑Compute / Two‑Brain** – separates fast edge inference from slower cloud‑based self‑improvement cycles. | Allows safe, bounded updates while keeping latency low for real‑time tasks. | Survey of dual‑brain robot architectures (2025‑2026 community posts, emergentmind.com).

---

## 2. Training & Update Loops

1. **Continuous Feedback Logging** – All adaptations must be auditable. Recommended to log *state snapshots* after each self‑modification (Best Ideas Collective, 2025).
2. **Guardrails & Reward Shaping** – Use a *reward model* that penalizes divergence from predefined safety constraints (Zhong et al., 2025).
3. **Curriculum‑Based Self‑Improvement** – Start with simple tasks, gradually increase difficulty; prevents catastrophic forgetting (Lee et al., 2025).
4. **Meta‑Learning of Update Policies** – Train a separate policy network that decides *when* and *what* to modify (Shinn et al., 2024).
5. **Human‑in‑the‑Loop Audits** – Periodic human review of generated modifications; can be automated with a secondary verification model.

---

## 3. Safety & Evaluation

- **Real‑Time Auditable Logs** – Store immutable logs (e.g., append‑only Merkle trees) to enable post‑mortem analysis.
- **Formal Verification of Architecture Changes** – Use model‑checking tools to verify that updates preserve invariants (e.g., no unbounded recursion depth).
- **Diversity of Ensembles** – RSA’s ensemble approach mitigates single‑point failure.
- **Rollback Mechanisms** – Keep versioned snapshots; enable instant rollback on detection of unsafe behavior.

---

## 4. Practical Recommendations (Pat’s Context)

1. **Start with a Fixed Core Model** (e.g., a 120B LLM) and implement STOP‑style peripheral modules for tool use, planning, and knowledge bases.
2. **Instrument a Logging Pipeline** – Capture prompts, outputs, and any self‑generated code changes; store in a version‑controlled repository.
3. **Adopt RSA for Reasoning Tasks** – Combine multiple reasoning paths before committing to an action; reduces hallucination.
4. **Design a Two‑Brain Setup** – Edge device (Jetson Orin Nano) runs inference; cloud (DGX Spark) runs the RSI loops overnight.
5. **Integrate Safety Checks** – Guardrails via a secondary verification model; run formal checks on any architectural mutation.

---

## 5. Open Questions / Research Gaps

- Quantitative metrics for *degree of self‑improvement*.
- Long‑term stability of meta‑controllers under distribution shift.
- Scalable verification methods for large, dynamically changing architectures.

---

**References** (selected):
- ICLR 2026 Workshop on AI with Recursive Self‑Improvement (openreview.net/pdf?id=OsPQ6zTQXV)
- Wikipedia: Recursive self‑improvement (2024 update)
- Venkatraman et al., *Recursive Self‑Aggregation* (arXiv:2509.26626, 2025)
- "Test‑time Recursive Thinking" (arXiv:2602.03094, 2024)
- ACL‑Long 2025 paper *A Self‑Referential Agent Framework* (aclanthology.org/2025.acl‑long.1354.pdf)
- EmergentMind article on Recursive Self‑Improvement (2024‑2025) 
- Best Ideas Collective, Guardrail Design (2025)
- Zhong et al., Reward Shaping for RSI (2025)

---

*Prepared by Bob (autonomous research agent) for Spark & Pat.*