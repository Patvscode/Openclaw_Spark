# Evaluation Metrics for Recursive Self‑Improvement (RSI) Systems

**Date:** 2026‑02‑13

## Overview
Recursive self‑improvement (RSI) systems iteratively modify their own algorithms, architectures, or data pipelines to become more capable.  Measuring progress reliably is critical for research, safety, and alignment.  Below is a synthesis of metrics identified from recent literature (Wikipedia, emergentmind.com, ICLR‑2026 workshop, firstscattering.com, and related articles).

## Core Metric Categories
| Category | Example Metrics | Description |
|---|---|---|
| **Performance Improvement** | • *Improvement Rate* – % gain in benchmark score per iteration (e.g., accuracy ↑ 2 % per cycle).<br>• *Absolute Score* – Raw score on a standardized test suite (e.g., MATH, BIG‑BENCH).<br>• *Mean Utility Increase* – Average increase in a utility function defined for the target task. | Directly quantifies capability growth.
| **Safety & Alignment** | • *Safety Compliance* – Pass/fail on a curated safety test suite (e.g., OpenAI Safety Gym, alignment checklists).<br>• *Deceptive Alignment Ratio* – Frequency of passing safety tests without true alignment (measured via hidden probes).<br>• *Robustness to Distribution Shift* – Performance drop when evaluated on out‑of‑distribution data. | Ensures gains are not merely “gaming” metrics.
| **Efficiency** | • *Compute‑per‑Improvement* – FLOPs or GPU‑hours required for each % gain.
• *Energy Consumption* – kWh per iteration.
• *Latency Reduction* – Time‑to‑inference improvement after each cycle. | Tracks resource cost of self‑improvement.
| **General Capability Acceleration** | • *Broad Capability Acceleration* – Aggregate improvement across a suite of heterogeneous tasks (e.g., language, vision, robotics). Measured as slope of total score vs. time.
• *Cross‑Domain Transfer* – Gains on tasks not directly optimized (zero‑shot performance). | Captures the “general intelligence” aspect.
| **Stability & Convergence** | • *Improvement Variance* – Standard deviation of scores across iterations; low variance indicates stable progress.
• *Convergence Rate* – Number of iterations until marginal gains fall below a threshold.
• *Catastrophic Failure Rate* – Frequency of regressions (score drop > X%). | Monitors reliability of the self‑improvement loop.
| **Human‑Interpretability** | • *Explainability Score* – Degree to which changes can be understood (e.g., proportion of generated code that passes static analysis). | Helpful for auditability.

## Recommended Composite Index
Many papers (e.g., ICLR 2026 workshop) suggest a **Composite RSI Index (CRSI)** that aggregates the above categories with configurable weights:
```
CRSI = w₁·ImprovementRate + w₂·SafetyScore + w₃·EfficiencyScore 
       + w₄·GeneralAccel + w₅·StabilityScore + w₆·Explainability
```
Weights can be tuned per project (e.g., safety‑heavy robotics may set w₂ = 0.4, w₁ = 0.2).

## Practical Steps for Pat’s Projects
1. **Select a Benchmark Suite** – BIG‑BENCH, MATH, and a robotics‑specific control benchmark (e.g., OpenAI Gym‑Robotics). 
2. **Define Safety Tests** – Use the OpenAI Safety Gym scenarios plus custom “misalignment probes” relevant to robot control. 
3. **Automate Metric Collection** – Script a CI pipeline that runs after each self‑improvement iteration and logs the metrics to a CSV/JSON file.
4. **Compute CRSI** – Apply a simple Python script to combine the metrics and track trends over time.

## References
- Wikipedia – Recursive self‑improvement
- emergentmind.com – Empirical measures of RSI (accuracy jumps, utility increase)
- ICLR 2026 Workshop – “Defining reproducible baselines for improvement cycles”
- firstscattering.com – “Red Lines for Recursive Self‑Improvement” (general capability acceleration, safety compliance)
- Alpha Evolve description – challenges around automated evaluation functions.
