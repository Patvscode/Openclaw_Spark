# Latency and Bandwidth Requirements for Edge vs Cloud Control of 6‑DOF Robot Arms

**Date:** 2026-02-13

## Overview
Real‑time control of a 6‑DOF manipulator (e.g., ROS2 MoveIt) typically runs at **100–200 Hz** (5–10 ms per control cycle).  The control loop includes:

1. **Sensor read** (joint encoders, force/torque sensors)
2. **State broadcast** (positions, velocities, torques)
3. **Planner / controller computation** (inverse kinematics, trajectory generation)
4. **Actuator command**

When the computation is performed on an **edge device** (e.g., DGX Spark or an on‑premise Jetson), the round‑trip latency is dominated by network transport and processing overhead.  Off‑loading to the **cloud** adds additional network hops and can introduce higher jitter.

---

## Latency Requirements
| Use‑case | Target latency (one‑way) | Reasoning |
|----------|------------------------|-----------|
| **Low‑level joint control** (torque/position loop) | **≤ 5 ms** | To keep the control loop stable at 200 Hz, the total time from sensor read to actuator command must be <5 ms. Any larger delay leads to phase lag and oscillations. |
| **Mid‑level trajectory planning** (few‑second motion) | **≤ 20 ms** | Planning can tolerate a few milliseconds of delay; 20 ms still allows sub‑100 Hz updates, which is sufficient for smooth trajectories. |
| **High‑level task planning / perception** (vision, SLAM) | **≤ 50–100 ms** | These components run at lower rates (10–20 Hz). Cloud latency of 30‑60 ms is acceptable if bandwidth is sufficient. |

### Evidence
- Edge‑computing surveys report **5–10 ms** response times for on‑premise workloads【source: firecell.io (Edge Computing vs Cloud: Latency Impact)】.
- The ARBot tele‑operation framework measured an **end‑to‑end latency of 19.5 ms** for a high‑fidelity manipulator, indicating that sub‑20 ms is achievable with optimized pipelines【source: arxiv.org (ARBot)】.

## Bandwidth Requirements
| Data type | Approx. size per sample | Sample rate | Bandwidth (approx.) |
|-----------|------------------------|-------------|----------------------|
| **Joint state** (positions, velocities, torques) – 6 DOF × 3 values × 8 bytes ≈ 144 B | 200 Hz | 144 B × 200 ≈ 28.8 KB/s |
| **Camera video** (720p, 30 fps, H.264) | ~1 Mbps (≈ 125 KB/s) | Continuous | 125 KB/s |
| **Depth map** (optional) | ~2 Mbps | 30 fps | 250 KB/s |

### Edge vs Cloud
- **Edge**: Joint state and low‑latency control stay local; video can be streamed to a local viewer or processed on‑edge (e.g., object detection).  Total bandwidth under **~150 KB/s**, well within Gigabit Ethernet.
- **Cloud**: If raw video is sent to the cloud for heavy perception, bandwidth can rise to **> 500 KB/s** per camera.  Compression and selective streaming (ROI) are needed.

## Recommendations for Pat’s Setup
1. **Run the low‑level controller on the DGX Spark (edge)** to guarantee ≤ 5 ms latency.
2. **Off‑load perception and high‑level planning to the cloud** only if network latency stays ≤ 50 ms and bandwidth ≥ 200 KB/s per stream.
3. **Use ROS2 DDS (Fast‑DDS) with QoS settings**:
   - `reliability: reliable`, `deadline: 5ms` for joint state topics.
   - `reliability: best_effort`, `history: keep_last(1)` for video streams.
4. **Benchmark** the actual round‑trip time using `ros2 topic echo` and `ping` between DGX Spark and the chosen cloud endpoint.

---

## Next Steps
- Implement a minimal ROS2 publisher/subscriber test to measure real latency on the lab network.
- Evaluate compression codecs (H.264 vs H.265) for video streaming bandwidth.
- Document a ROS2 DDS profile tuned for edge‑centric control.

*Prepared by Bob (autonomous research agent).*