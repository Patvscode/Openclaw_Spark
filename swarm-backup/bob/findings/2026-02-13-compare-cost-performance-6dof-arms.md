# Comparison of Top 3 Open‑Source 6‑DOF Robot Arms (Research Use)

Date: 2026‑02‑13

## Arms Evaluated
| Arm | Reach (mm) | Payload (kg) | Repeatability (mm) | Approx. Cost (USD) | Notes |
|-----|------------|--------------|--------------------|-------------------|-------|
| **Annin AR4 (MK4)** | 630 mm (24.75 in) | 1.9 kg (4.15 lb) | 0.2 mm | **~1,791** (complete kit, excludes motors; motors bought separately) | Well‑documented, ROS/Arduino support, good community, higher weight (≈27 kg) |
| **myCobot Pro 630** | 600 mm (≈23.6 in) | 2 kg | ~0.2 mm (claimed) | **~7,999** (incl. accessories) | Commercial‑grade, higher price, robust firmware, good for lab automation |
| **reBot Arm B601** | 650 mm | 1.5 kg | <0.2 mm | **< 1,000** (sub‑$1 k) | Very low cost, open‑source hardware/software stack, ROS2 support planned |

## Cost vs Performance Summary
- **Cost per kg payload**: reBot (~$667/kg), AR4 (~$943/kg), myCobot (~$4,000/kg). The AR4 offers a middle ground in cost while providing the highest payload.
- **Reach**: reBot leads slightly, but differences are marginal for typical research bench‑top setups.
- **Repeatability**: All claim ~0.2 mm, sufficient for most manipulation tasks.
- **Overall suitability**: For Pat’s research on recursive self‑improvement and dual‑brain robotics, the **AR4** gives a balanced platform with solid community resources and ROS integration. The **reBot** is attractive for budget‑constrained prototypes. The **myCobot** is over‑engineered cost‑wise unless commercial reliability is needed.

## Sources
- Annin AR4 specs & cost: Open Source Ecology wiki (≈$1,791)【source=AR4 Wiki】
- AR4 payload/reach/repeatability from product page【source=AR4 specs】
- myCobot Pro 630 price listed as $7,999 on Elephant Robotics shop【source=MyCobot price】
- reBot Arm B601 specs (reach 650 mm, payload ≥1.5 kg, repeatability <0.2 mm, sub‑$1k) from Seeed Studio Hackster article【source=ReBot specs】
