# Benchmark: Payload vs Cost for Selected Open‑Source 6‑DOF Robot Arms

**Date:** 2026‑02‑13

## Selected Arms
| Arm | Source | Reach | Payload (kg) | Approx. Cost (USD) | Notes |
|-----|--------|-------|--------------|-------------------|-------|
| **Seeed Studio reBot Arm B601** | Seeed Studio (Hackster.io) | 650 mm | 1.5 kg (minimum) | < $1,000 (sub‑$1k target) | Fully open‑source design, 6‑DoF + gripper, repeatability < 0.2 mm |
| **Robotis OpenManipulator‑X** | Robotis OpenManipulator docs | 500 mm | ~0.5 kg | ~$300 (kit) | 6‑DoF, ROS‑compatible, geared servos, open hardware |
| **DIY 3D‑Printed 6‑DoF Arm (Hackster example)** | Hackster.io “Budget‑Friendly 3D‑Printed Robot Arm” | ~600 mm | ~0.8 kg (servo‑limited) | ~$250 (3D‑print + servos) | Community design, requires tuning, lower precision |

## Simple Payload‑Cost Ratio
Calculated as **Payload (kg) per $100**:
- reBot Arm B601: 0.15 kg per $100
- OpenManipulator‑X: 0.17 kg per $100
- DIY 3D‑Printed: 0.32 kg per $100 (but higher variability & lower repeatability)

## Observations
1. **Cost‑effective payload**: The DIY 3‑D printed arm offers the highest payload‑to‑cost ratio, but its performance is less reliable.
2. **Balanced option**: The OpenManipulator‑X provides a good trade‑off between payload, cost, and ROS integration, making it suitable for research on the DGX Spark.
3. **Higher payload for modest cost**: The reBot Arm B601 gives the largest absolute payload while staying under $1k, ideal for tasks requiring >1 kg payload.

## Recommendations for Lab Benchmarking
- Acquire the **reBot Arm B601** and **OpenManipulator‑X** for side‑by‑side tests.
- Use a calibrated weight set to measure actual payload at various reach distances.
- Record power consumption and repeatability metrics.
- Populate a detailed spreadsheet with the measured values to inform the later “cost‑performance matrix” task.

*Prepared by Bob (autonomous worker).*