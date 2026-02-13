# Prototype STOP‑style Self‑Improvement Loop on DGX Spark

**Date:** 2026‑02‑13

## Goal
Create a design plan for a **STOP‑style** (Self‑Training‑Optimisation‑Policy) self‑improvement loop that runs on the DGX Spark workstation. The loop should be able to:
1. **Collect** performance data from the robot control stack.
2. **Evaluate** improvements against safety and performance metrics.
3. **Train / fine‑tune** a policy model using the new data.
4. **Validate** the updated policy with formal safety checks before deployment.
5. **Deploy** the new policy back to the robot controller.

## High‑Level Architecture
```
+-------------------+   +-------------------+   +-------------------+
|  Data Collector   |→ |  Evaluation &    |→ |  Model Trainer    |
| (ROS2 logs,      |   |  Metric Service   |   | (RLHF / PPO)      |
|  sensor streams) |   | (latency, torque,|   |                   |
+-------------------+   |  safety scores)   |   +-------------------+
          |               +-------------------+            |
          v                        |                     v
+-------------------+   +-------------------+   +-------------------+
|  Safety Validator |← | Orchestrator      |← |  Policy Deployer   |
| (Reluplex,       |   | (Airflow / custom|   | (Docker/K8s)       |
|  Marabou)        |   |  DAG)             |   +-------------------+
+-------------------+   +-------------------+   
```

### 1. Data Collector
* **ROS2 nodes** capture sensor streams, joint states, and controller commands.
* Store raw logs in a time‑series DB (e.g., InfluxDB) and archive raw bag files on NVMe.
* Use a lightweight edge agent (Python) to push summaries to a central **MongoDB** used by the evaluation service.

### 2. Evaluation & Metric Service
* Define **core metrics**:
  - End‑effector position error (mm)
  - Trajectory smoothness (jerk)
  - Energy consumption (J)
  - Safety incidents (collision alerts)
  - Improvement rate (Δ metric per iteration)
* Implement as a **FastAPI** service exposing `/evaluate` that consumes the latest data batch and returns a JSON score.

### 3. Model Trainer
* Base policy: **Open‑source PPO‑based controller** (e.g., `stable‑baselines3` with a transformer backbone).
* Training pipeline using **Ray Tune** for distributed GPU utilization on the DGX Spark.
* Incorporate **RLHF** style human feedback: Pat can label successful vs. unsafe trajectories via a simple web UI.

### 4. Safety Validator
* Export the trained policy to ONNX.
* Run **formal verification** tools (Reluplex, Marabou) on the network to prove:
  - No joint exceeds torque limits.
  - No state leads to a collision within a 200 ms horizon.
* If verification fails, the loop aborts and rolls back.

### 5. Orchestrator
* Use **Apache Airflow** (lightweight Docker image) to schedule the DAG:
  1. Trigger data collection (hourly).
  2. Run evaluation.
  3. If improvement > threshold **AND** safety passes, start training.
  4. Post‑training verification.
  5. Deploy new policy.
* Airflow UI provides visibility for Pat.

### 6. Policy Deployer
* Containerised ROS2 node (`policy_server`) reads the latest ONNX model from a **private Docker registry**.
* Uses **zero‑downtime rollout**: keep the previous node running while the new node starts, then switch topics.

## Required Components & Resources
| Component | Tool / Library | Reason |
|-----------|----------------|--------|
| Data logging | ROS2 bag, InfluxDB | Native ROS2 integration, fast time‑series queries |
| Metric evaluation | FastAPI, Pandas, NumPy | Simple REST API, easy to extend |
| Training | Ray Tune, stable‑baselines3, PyTorch | Scales across DGX GPUs |
| Human feedback UI | Flask + React | Minimal UI for Pat to label runs |
| Safety verification | Reluplex, Marabou (ONNX backend) | Formal guarantees on neural nets |
| Orchestration | Apache Airflow (Docker) | DAG scheduling, monitoring |
| Deployment | Docker, ROS2 launch | Container isolation, easy rollback |
| Storage | MongoDB (metadata), NVMe (raw bags) | Fast reads/writes, persistence |

## Rough Timeline (first prototype)
1. **Week 1** – Set up data collector & storage.
2. **Week 2** – Implement metric service & baseline evaluation.
3. **Week 3** – Build training pipeline on a small dataset.
4. **Week 4** – Integrate safety validator (run on sample nets).
5. **Week 5** – Wire Airflow DAG and test end‑to‑end loop.
6. **Week 6** – Conduct first full‑cycle run and iterate.

## Risks & Mitigations
* **Verification scalability** – start with small networks, gradually increase complexity.
* **Catastrophic policy regression** – enforce strict rollback and keep previous policy versioned.
* **Compute budget** – limit training epochs; use early‑stop based on metric improvement.
* **Human‑in‑the‑loop bottleneck** – batch feedback sessions weekly, not per‑iteration.

---
*Prepared for Pat and Spark to review. Next steps: flesh out concrete metric formulas and prototype the data collector.*