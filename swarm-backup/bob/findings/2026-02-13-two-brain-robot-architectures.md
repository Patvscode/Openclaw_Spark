# Findings: Two‑Brain (Edge + Cloud) Robot Architectures

**Date:** 2026‑02‑13

## Overview
Two‑brain (or dual‑compute) robot architectures combine **local edge compute** for low‑latency, safety‑critical control with **cloud compute** for heavy‑weight perception, planning, data sharing, and continual learning. The edge component runs on the robot’s onboard processor (e.g., NVIDIA Jetson, ARM CPU, FPGA), while the cloud component runs in a data‑center or hybrid edge‑cloud platform.

## Real‑World Examples

1. **Google Self‑Driving Cars (Waymo)** – The vehicles host perception and short‑term motion planning on an onboard GPU (edge) for millisecond‑scale decisions, while sending sensor streams to Google’s cloud for map updates, long‑term planning, fleet‑wide learning, and model training. The cloud aggregates experiences from all cars and pushes improved models back to the fleet. [Source: Cloud robotics article]
2. **Cloud Medical Robots** – Surgical assistants and tele‑presence robots connect to a “medical cloud” that stores patient records, disease archives, and expert‑system knowledge. The robot performs real‑time kinematics locally, while consulting the cloud for diagnostic assistance and remote surgeon guidance. [Source: Cloud robotics article]
3. **Assistive Domestic Robots** – Elder‑care robots monitor health metrics locally and upload alerts to cloud‑based health services. They receive fall‑prevention policies and emergency response instructions from the cloud, enabling continuous improvement without on‑device retraining. [Source: Cloud robotics article]
4. **Industrial Robots (Industry 4.0)** – Factories use edge controllers for precise motion control on robotic arms, while a cloud platform coordinates multiple robots, performs scheduling, and runs large‑scale simulations for optimization. [Source: Cloud robotics article]
5. **NVIDIA Isaac Platform** – Provides an edge runtime (Isaac SDK) for on‑robot AI inference, coupled with the Isaac Cloud services for fleet management, model training, and data aggregation. This is a commercial embodiment of the two‑brain pattern.

## Architectural Patterns
- **Edge Compute:** Low‑latency sensor processing, safety loops, actuator control. Often runs ROS 2 nodes, real‑time OS, or dedicated inference accelerators.
- **Cloud Compute:** Heavy perception models, large‑scale SLAM maps, reinforcement‑learning updates, cross‑robot knowledge bases.
- **Communication Layer:** Secure MQTT/ROS 2 DDS, gRPC, or WebSockets with bandwidth‑aware protocols; fallback to offline mode when connectivity is lost.
- **Data Synchronization:** Periodic upload of logs, trajectories, and learned policies; cloud‑to‑edge OTA updates for models.

## Benefits & Trade‑offs
| Benefit | Edge | Cloud |
|---|---|---|
| Latency | Milliseconds – essential for safety | Seconds‑to‑minutes – acceptable for planning, learning |
| Compute Power | Limited by on‑board hardware | Virtually unlimited (GPU clusters) |
| Data Freshness | Real‑time sensor data | Aggregated, historical data across fleet |
| Reliability | Operates offline | Dependent on network connectivity |
| Maintenance | OTA updates required | Centralized model training and distribution |

## Open‑Source Frameworks Supporting Two‑Brain
- **ROS 2** with DDS for distributed communication and QoS settings.
- **Open‑RMF** (Robot Middleware Framework) for fleet‑level coordination across edge and cloud.
- **Ignition Gazebo** for cloud‑based simulation coupled with edge runtime.

## Next Steps (Follow‑up Tasks)
1. Identify open‑source frameworks (ROS 2 DDS, Open‑RMF) that facilitate dual‑compute deployments.
2. Evaluate latency and bandwidth requirements for edge‑cloud split in a 6‑DOF arm control loop.
3. Survey commercial platforms (NVIDIA Isaac, Clearpath Husky) offering edge‑cloud APIs.

---
*Compiled for Bob’s autonomous worker queue.*