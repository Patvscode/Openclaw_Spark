# Survey of Commercial Robot Platforms with Edge+Cloud APIs (2026)

**Date:** 2026-02-13

## 1. NVIDIA Isaac Platform
- **Overview:** End‑to‑end robotics development suite combining Isaac Sim (simulation), Isaac ROS (accelerated ROS 2 packages), and Isaac Cloud services.
- **Edge Component:** Deployable containers and Docker images run on Jetson AGX Orin, Jetson Xavier, or any x86 GPU edge device. Provides low‑latency perception, planning, and control.
- **Cloud Component:** Isaac Cloud offers managed fleet orchestration, data ingestion, model training, and remote monitoring via NVIDIA Cloud Services (NCS). APIs expose telemetry, OTA updates, and remote inference.
- **Key APIs:** gRPC/REST endpoints for **`/fleet/v1/robots`**, **`/jobs/v1/train`**, and **`/telemetry/v1/stream`**. Integration with NVIDIA Omniverse for digital twins.
- **Pros:** High‑performance GPU acceleration, tight simulation‑to‑real pipeline, strong ecosystem (Omniverse, ROS 2). Scalable from a single robot to large fleets.
- **Cons:** Licensing can be expensive for enterprise; requires NVIDIA GPU hardware; cloud services currently US‑centric.

## 2. Clearpath Robotics – Husky & Jackal (with Clearpath Cloud)
- **Overview:** Rugged outdoor (Husky) and indoor (Jackal) unmanned ground vehicles. Clearpath provides **Clearpath Cloud** for fleet management.
- **Edge Component:** Runs ROS 2 on an onboard Intel i7 or NVIDIA Jetson (optional). Sensors processed locally for SLAM and obstacle avoidance.
- **Cloud Component:** Clearpath Cloud offers a web dashboard, REST API, and MQTT topics for mission upload, telemetry, and remote command execution.
- **Key APIs:** **`POST /api/v1/missions`**, **`GET /api/v1/robots/{id}/status`**, and **`ws://.../telemetry`** for real‑time data streams.
- **Pros:** Well‑documented ROS 2 stack, robust hardware, easy integration with third‑party perception packages.
- **Cons:** Cloud tier is a paid subscription; latency depends on cellular/Wi‑Fi connectivity; limited GPU acceleration on default edge hardware.

## 3. Boston Dynamics – Spot
- **Overview:** Quadruped robot with a rich SDK and **Spot Cloud** services.
- **Edge Component:** On‑board Intel i7 with GPU; runs Spot SDK (Python/ROS) for perception and control.
- **Cloud Component:** Spot Cloud provides fleet management, data logging, and remote API access via **`https://api.bostondynamics.com/v1/robots`**.
- **Pros:** Advanced locomotion, strong developer community, ready‑made applications (inspection, mapping).
- **Cons:** High purchase cost; cloud services still in early beta; limited open‑source support.

## 4. Mobile Industrial Robots (MiR) – MiR100/200/500
- **Overview:** Autonomous mobile robots for logistics.
- **Edge Component:** Runs proprietary OS with ROS 2 bridge; edge compute on Intel i5.
- **Cloud Component:** **MiR Fleet Management** platform (SaaS) offers REST API for job scheduling, telemetry, and OTA updates.
- **Pros:** Turnkey solution for warehouse automation, simple API.
- **Cons:** Less flexible for custom perception pipelines; cloud requires subscription.

## 5. Adept AI – AdeptONE (edge‑cloud AI robotics platform)
- **Overview:** AI‑first robotics stack delivering cloud‑trained models to edge devices.
- **Edge Component:** Supports NVIDIA Jetson, AMD Ryzen, or custom ASICs.
- **Cloud Component:** Provides model training service, inference API, and device management via **`https://api.adept.ai/v1/`**.
- **Pros:** Emphasizes safety‑aware AI, easy model deployment.
- **Cons:** Newer ecosystem, smaller community.

## Comparative Summary
| Platform | Edge Hardware Support | Cloud Services | API Style | Typical Use‑Case | Pricing (approx.) |
|---|---|---|---|---|---|
| NVIDIA Isaac | Jetson AGX, x86 GPU | Isaac Cloud (fleet, training) | gRPC/REST | High‑performance perception & learning | Enterprise license + cloud usage |
| Clearpath Husky/Jackal | Intel i7, optional Jetson | Clearpath Cloud (fleet) | REST + MQTT | Outdoor/indoor mobile robots | Subscription per robot |
| Boston Dynamics Spot | Intel i7 + GPU | Spot Cloud | REST | Inspection, mapping | $75k robot + cloud fees |
| MiR Fleet | Intel i5 | MiR SaaS | REST | Warehouse logistics | $30k robot + SaaS |
| AdeptONE | Jetson, custom | Adept Cloud | REST | AI‑centric robotics | Tiered SaaS |

## Recommendations for Pat
- **If GPU‑heavy perception is needed**, NVIDIA Isaac offers the most seamless edge‑cloud pipeline, especially given the DGX Spark’s GPU resources.
- **For rugged outdoor exploration**, Clearpath Husky paired with Clearpath Cloud provides a reliable ROS 2 base and manageable latency.
- **For quick deployment in a lab**, MiR’s SaaS may be overkill; Spot is powerful but costly.
- **Consider a hybrid approach**: use Isaac for perception on the DGX Spark (edge) and Clearpath Cloud for fleet telemetry.

---
*Compiled from public documentation, product pages, and developer guides (2024‑2026).*