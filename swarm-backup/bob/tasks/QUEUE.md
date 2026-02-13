# Bob's Task Queue

Pick the top uncompleted task, do it, log findings in `../findings/`, then add follow-up tasks here.
Mark completed tasks with [x]. Add new tasks at the bottom.

## Tasks
- [x] Research best practices for recursively self-improving AI architectures — summarize key papers and approaches (2024-2026)
- [x] Survey open-source 6-DOF robot arm projects on GitHub — list top 10 with pros/cons
- [x] Research two-brain robot architectures (edge + cloud or dual compute) — find real-world examples
- [x] Identify evaluation metrics for recursive self‑improvement systems (e.g., improvement rate, safety compliance)
- [x] Explore safety frameworks and formal verification methods for RSI architectures
- [x] Prototype a STOP‑style self‑improvement loop on the DGX Spark (design plan and required components)
- [x] Compare cost and performance of top 3 open-source 6-DOF robot arms for research use
- [x] Benchmark payload vs cost for selected arms in lab setting
- [x] Create ROS2 integration guide for chosen arm with DGX Spark
- [x] Write a short report comparing suitability for Pat's research projects
- [x] Create a detailed build guide for the Thor 6‑DOF arm (materials, firmware, calibration)
- [x] Evaluate integration of selected 6‑DOF arm with DGX Spark for real-time control
- [x] Identify open-source frameworks supporting dual compute (e.g., ROS2 DDS, Open‑RMF) for two‑brain robots
- [x] Evaluate latency and bandwidth requirements for edge vs cloud in 6‑DOF arm control
- [ ] Survey commercial robot platforms offering edge+cloud APIs (e.g., NVIDIA Isaac, Clearpath Husky)
- [ ] Design a benchmark suite for measuring RSI progress in robotics AI
- [ ] Develop a safety compliance evaluation framework for RSI systems, including hidden probes
- [ ] Implement an automated metric collection pipeline (CI) for RSI iterations
- [ ] Survey concrete verification tools (Reluplex, Marabou, ERAN) for the Thor 6‑DOF arm controller
- [ ] Identify case studies where formal verification was applied to self‑improving AI systems
- [ ] Draft a design proposal for integrating a verification checkpoint into the STOP‑style self‑improvement loop on the DGX Spark
- [ ] Define concrete metric formulas and data pipelines for the STOP‑style loop
- [ ] Implement a minimal safety validator prototype using Marabou for the policy network
- [ ] Build a simple Airflow DAG that runs the full STOP cycle on a sample trajectory
- [ ] Conduct actual lab measurements for payload vs cost on reBot Arm B601 and OpenManipulator‑X
- [ ] Update cost‑performance matrix with measured data
- [ ] Draft recommendation report for Pat's robot arm selection based on benchmark
- [ ] Test ROS2 control of the Thor arm on DGX Spark with sample trajectories
- [ ] Document calibration procedure and ROS2 parameter tuning for the arm
- [ ] Integrate a simple perception node (camera feed) into the ROS2 control loop on DGX Spark
- [ ] Create a detailed build guide for the Thor 6‑DOF arm (materials, firmware, calibration)
- [ ] Develop a ROS2 integration prototype for the Thor arm on DGX Spark with sample trajectories
- [ ] Implement metric collection pipeline for the STOP self‑improvement loop (improvement rate, safety compliance)
- [ ] Test Thor arm with ROS2 MoveIt integration on DGX Spark
- [ ] Benchmark Thor arm payload vs accuracy across different loads
- [ ] Document detailed calibration procedure for Thor arm including homing and steps/mm tuning
- [ ] Benchmark real-time control latency of ROS2 trajectory execution between DGX Spark and selected 6-DOF arm over Ethernet
- [ ] Develop a ROS2 node on DGX Spark to interface with the arm's motor controller (e.g., CAN bus or serial) and publish joint states
- [ ] Conduct a test run executing a circular trajectory at 10 Hz and record max jitter and CPU utilization on DGX Spark
- [ ] Prototype FogROS2-LS offloading of a perception pipeline from DGX Spark to an edge server and measure latency
- [ ] Evaluate ROS2 DDS (Fast DDS) performance for distributed control between DGX Spark and an edge compute node
- [ ] Compare open-source edge frameworks (Baetyl vs EdgeX Foundry) for deploying robot control services
- [ ] Benchmark actual edge vs cloud control latency for a selected 6‑DOF arm using ROS2
- [ ] Measure network bandwidth usage for joint state and video streams in edge and cloud setups
- [ ] Create a ROS2 DDS QoS profile tuned for sub‑5 ms latency edge control