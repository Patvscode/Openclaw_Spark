# Open-Source Frameworks Supporting Dual Compute (Edge+Cloud) for Two‑Brain Robots

**Date:** 2026‑02‑13

## Overview
Dual‑compute (or “two‑brain”) robot architectures split workloads between an on‑board edge processor and remote cloud/edge servers.  Open‑source projects that enable this split typically provide:
1. **Distributed communication** (low‑latency, reliable data exchange).
2. **Computation off‑loading** mechanisms (transparent RPC, container orchestration).
3. **Hardware‑agnostic deployment** (runs on embedded CPUs, GPUs, or cloud VMs).

Below is a curated list of frameworks that satisfy these criteria, with brief notes on relevance to Pat’s DGX Spark + 6‑DOF arm research.

---
### 1. ROS 2 + DDS (Fast DDS / Cyclone DDS / Eclipse Zenoh)
- **What it is:** ROS 2 is built on the Data Distribution Service (DDS) standard.  DDS implementations (Fast DDS, Cyclone DDS, Zenoh‑DDS) allow nodes to run on any machine – edge or cloud – and discover each other automatically.
- **Dual‑compute support:** Nodes can be launched on the DGX Spark (real‑time control) while heavy perception or planning nodes run on remote servers.  DDS handles QoS, reliability, and bandwidth settings.
- **Key resources:**
  - Fast DDS (eProsima) – widely used in ROS 2 Humble/Foxy.
  - Zenoh‑plugin‑ros2dds (eclipse‑zenoh) – enables zero‑copy, topic‑level routing across WAN.
- **Why it matters:** Pat already uses ROS 2 for arm control; adding DDS‑based off‑loading is a minimal‑effort path.

---
### 2. Open‑RMF (Robot Middleware Framework)
- **What it is:** Open‑RMF sits on top of ROS 2 and provides fleet‑wide task allocation, traffic management, and state monitoring.
- **Dual‑compute support:** RMF’s architecture is inherently distributed; the “dispatcher” can run in the cloud while robot agents run locally, enabling coordinated edge‑cloud operation.
- **Links:** https://www.open-rmf.org/  (GitHub repos: `open-rmf/rmf`, `open-rmf/rmf_ros2`).
- **Relevance:** Ideal for coordinating multiple arms or mobile bases that share a cloud‑based planner.

---
### 3. FogROS2 / FogROS2‑LS
- **What it is:** An extension to ROS 2 that lets developers annotate nodes for automatic off‑loading to edge or cloud resources.
- **Features:** Dynamic selection of the best compute endpoint, transparent ROS‑2 API compatibility, and latency‑aware scheduling.
- **Open‑source:** Available under Apache‑2.0 on GitHub (part of the ROS 2 ecosystem).  The “LS” (Latency‑Sensitive) variant adds real‑time constraints.
- **Use case:** Off‑load deep‑learning perception (e.g., point‑cloud segmentation) from the DGX Spark to an edge GPU cluster while keeping low‑level control local.

---
### 4. Baetyl (Linux Foundation Edge)
- **What it is:** A lightweight edge‑computing runtime that runs containerized workloads and syncs state with the cloud.
- **Dual‑compute relevance:** You can deploy a ROS 2 node as a Docker container on Baetyl‑managed edge devices and have the cloud orchestrate updates.
- **GitHub:** https://github.com/baetyl/baetyl
- **Pros/Cons:** Very modular and language‑agnostic, but requires extra plumbing to bridge ROS topics.

---
### 5. EdgeX Foundry
- **What it is:** An open‑source IoT edge platform offering device services, data ingestion, and micro‑service pipelines.
- **Dual‑compute relevance:** Can host ROS 2 bridge services, providing a unified API for sensor data that can be processed locally or forwarded to cloud analytics.
- **GitHub:** https://github.com/edgexfoundry/edgex‑go
- **Notes:** More generic IoT; integration effort higher than ROS‑centric solutions.

---
### 6. LF Edge / Open Horizon
- **What it is:** A collection of projects (e.g., Akraino, Open Horizon) that define standards for edge‑cloud interoperability.
- **Relevance:** Provide container orchestration and policy‑based workload placement, useful if you want to manage many robots from a central hub.

---
### 7. Kubernetes + ROS 2
- **What it is:** Running ROS 2 nodes as Pods in a K8s cluster (cloud or edge).  Projects like `ros2_kubernetes` offer Helm charts.
- **Dual‑compute:** Enables scaling perception/planning services while the low‑latency control nodes stay on the DGX Spark.
- **Considerations:** Overhead of K8s may be non‑trivial for sub‑millisecond control loops.

---
## Quick Comparison Table
| Framework | Primary Language | Edge‑Ready? | Cloud‑Ready? | ROS 2 Integration | Typical Use‑Case |
|---|---|---|---|---|---|
| ROS 2 + DDS (Fast DDS, Cyclone DDS) | C++/Python | ✅ | ✅ | ✅ (native) | Real‑time control + off‑load perception |
| Open‑RMF | C++/Python | ✅ | ✅ | ✅ (via rmf_ros2) | Fleet coordination |
| FogROS2‑LS | C++/Python | ✅ | ✅ | ✅ (extension) | Dynamic off‑loading |
| Baetyl | Go | ✅ | ✅ | – (needs bridge) | Lightweight edge runtime |
| EdgeX Foundry | Go | ✅ | ✅ | – (bridge) | Generic IoT/edge pipelines |
| LF Edge / Open Horizon | Go/Rust | ✅ | ✅ | – | Policy‑based workload placement |
| K8s + ROS 2 | YAML/Go | ✅ (k3s) | ✅ | ✅ (via ros2_k8s) | Scalable cloud services |

---
## Recommendations for Pat’s Two‑Brain Arm Project
1. **Start with ROS 2 + Fast DDS** – already in the stack; configure QoS profiles to separate control (reliable, low latency) from perception (best‑effort, higher latency).
2. **Add FogROS2‑LS** for a proof‑of‑concept off‑loading of a heavy vision model to an edge GPU (e.g., an NVIDIA Jetson Orin).  Measure latency using the `fogros2 latency` tools.
3. **Prototype Open‑RMF** if you later need multi‑robot coordination (e.g., a second arm or mobile base).
4. **Explore Baetyl** for a minimal container‑based edge node if you want to run non‑ROS services (e.g., a custom reinforcement‑learning trainer) alongside ROS.

---
## Next Steps (Follow‑up Tasks)
- Evaluate FogROS2‑LS off‑loading of a perception pipeline from the DGX Spark to an edge server and measure latency.
- Benchmark ROS 2 DDS (Fast DDS) performance for distributed control between DGX Spark and an edge compute node.
- Compare Baetyl vs EdgeX Foundry for deploying robot control services.

*Prepared for Pat’s review.*
