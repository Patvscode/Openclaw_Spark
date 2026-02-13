# Survey of Open‑Source 6‑DOF Robot Arm Projects (GitHub)

Date: 2026‑02‑13

## Selected Projects (Top 10)

| # | Project | Description | Pros | Cons |
|---|---------|-------------|------|------|
| 1 | **SkyentificGit/SmallRobotArm** | 6‑DoF arm built with stepper motors, fully 3D‑printable. | Affordable, open‑source hardware and firmware, good documentation. | Limited payload (~2 kg), stepper precision lower than servos. |
| 2 | **hobofan/collected-robotic-arms** (collection) | Curated list of open‑source arms, includes several 6‑DoF designs. | Acts as a hub to discover multiple projects, includes links to parts. | Not a single project; quality varies across listed arms. |
| 3 | **PCrnjak/Faze4‑Robotic‑arm** | Fully 3D‑printable 6‑axis arm with cycloidal gearboxes. | High precision, compact, community Discord for support. | Requires custom gear manufacturing, more complex assembly. |
| 4 | **AngelLM/Thor** | 6‑DoF printable arm targeting education and makers. | Easy to print, decent payload (750 g), well‑documented build guide. | Lower torque, not suited for heavy tasks. |
| 5 | **smottera/Robot‑Arm** | 6‑DoF arm with detachable end‑effector, PLA parts. | Modular design, interchangeable tools, open‑source CAD files. | PLA strength limits load, requires careful infill tuning. |
| 6 | **ELISAVADevelopmentLab/MOTUS** | 3D‑printed 6‑DoF arm developed by a university lab. | Academic backing, detailed kinematic model, good calibration scripts. | Less community support, parts may need higher‑quality printing. |
| 7 | **ZerO371/6‑dof‑Robot‑Arm‑simulator** | Software‑only simulator for 6‑DoF arms. | Useful for testing control algorithms without hardware. | No physical hardware; purely virtual. |
| 8 | **KongdoleProduction/RoboticArmController** | Arduino shield for 6‑DOF servo arm control. | Simple Arduino integration, good for hobbyists. | Focuses on control board, not full mechanical design. |
| 9 | **tutRPi/6DOF‑Robot‑Arm** | Python scripts for controlling various 6‑DoF arms. | Provides software stack, ROS‑compatible examples. | Dependent on external hardware designs. |
|10| **GitHub topic: 6dof‑robot‑kinematics** | Aggregates many repos related to 6‑DoF kinematics. | Broad resource pool for algorithms and models. | Not a concrete hardware project; requires digging. |

## Observations
- Most projects rely on 3D‑printed PLA/ABS parts, keeping costs low (< $200 for parts). 
- Payloads typically range from 0.5 kg to 2 kg; none approach industrial‑grade loads.
- Precision varies: servo‑based arms (e.g., Faze4) tend to be more accurate than stepper‑based designs.
- Community support is strongest for Thor, Faze4, and the SkyentificGit arm (Discord, wiki). 
- Software ecosystems differ: some provide ROS packages, others simple Arduino sketches.

## Recommendations for Pat
1. **For rapid prototyping** – start with **Thor** or **SkyentificGit/SmallRobotArm**; they have clear build guides and low cost.
2. **For higher precision** – evaluate **Faze4‑Robotic‑arm**; consider ordering custom cycloidal gears.
3. **For software development** – use the **ZerO371 simulator** to test control loops before hardware deployment.
4. **Integration with DGX Spark** – focus on arms with ROS support (e.g., Faze4, Thor) to leverage GPU‑accelerated perception pipelines.

*End of findings.*