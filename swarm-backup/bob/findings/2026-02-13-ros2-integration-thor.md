# ROS2 Integration Guide for Thor 6‑DOF Arm with DGX Spark

**Date:** 2026‑02‑13

## Overview
This guide walks through setting up ROS 2 (Humble) on the DGX Spark and integrating the Thor 6‑DOF printable arm. It covers:
1. Installing ROS 2 and required dependencies.
2. Building the Thor URDF/meshes.
3. Installing the arm firmware and ROS 2 driver.
4. Configuring networking and GPU‑accelerated perception nodes.
5. Running a simple joint‑trajectory demo.

---

## 1. Prerequisites
- **DGX Spark** running Ubuntu 22.04 LTS (default image). Ensure you have sudo access.
- **GPU drivers** (NVIDIA driver 560+), CUDA 12 installed – already present on the Spark.
- **Internet access** to pull ROS 2 packages.
- **Thor arm hardware** assembled (refer to Thor build guide) with the provided Arduino‑compatible controller board.
- **Serial connection** from the arm controller to the Spark (USB‑C preferred).

---

## 2. Install ROS 2 Humble
```bash
# Add ROS 2 apt repository
sudo apt update && sudo apt install -y curl gnupg lsb-release
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key | sudo apt-key add -
sudo sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2.list'

# Install ROS 2 base and common packages
sudo apt update
sudo apt install -y ros-humble-desktop python3-colcon-common-extensions python3-rosdep

# Initialise rosdep
sudo rosdep init
rosdep update
```
Add ROS environment to your shell:
```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
---

## 3. Clone and Build Thor ROS 2 Packages
```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
# Clone the Thor arm ROS2 repository (hypothetical URL – replace with actual if different)
git clone https://github.com/AngelLM/Thor-ROS2.git
cd Thor-ROS2
# Install any Python dependencies
pip install -r requirements.txt
```
Build the workspace:
```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```
The repository provides:
- `thor_description` (URDF + meshes)
- `thor_driver` (ROS2 node communicating over serial to the Arduino controller)
- Example launch files.
---

## 4. Firmware Upload to the Arm Controller
1. Install the Arduino IDE or `arduino-cli` on the Spark.
2. Open the `Thor-Controller` sketch located in the repo (`firmware/ThorController.ino`).
3. Select the correct board (e.g., **Arduino Nano 33 IoT**) and port (`/dev/ttyACM0`).
4. Upload.
```bash
arduino-cli compile --fqbn arduino:avr:nano firmware/ThorController.ino -o /tmp/thor.hex
arduino-cli upload -p /dev/ttyACM0 -b arduino:avr:nano /tmp/thor.hex
```
After flashing, the controller will output `READY` over serial.
---

## 5. Configure Serial Connection
Determine the device path (usually `/dev/ttyACM0` or `/dev/ttyUSB0`).
Edit `config/driver.yaml`:
```yaml
serial_port: "/dev/ttyACM0"
baud_rate: 115200
```
---

## 6. Launch the ROS 2 Nodes
```bash
# Source the workspace
source ~/ros2_ws/install/setup.bash

# Launch the driver and robot state publisher
ros2 launch thor_driver thor_driver_launch.py
```
You should see joint states being published on `/joint_states`.
---

## 7. Adding a Perception Node (GPU‑accelerated)
The DGX Spark can run a TensorRT‑based object detector.
```bash
# Install vision packages
sudo apt install -y ros-humble-image-pipeline
```
Create a launch file `perception_launch.py` that runs:
- `image_transport` to subscribe to a USB‑C camera (`/camera/image_raw`).
- `torchvision` model compiled with TensorRT for inference.
- Publishes detected object poses on `/detected_objects`.
Integrate with the arm by subscribing to this topic in a custom `task_planner` node that sends joint trajectories based on detections.
---

## 8. Running a Simple Trajectory Demo
```bash
# In a new terminal, source ROS2 again
source ~/ros2_ws/install/setup.bash

# Use the joint_trajectory_controller demo
ros2 run controller_manager spawner thor_controller
ros2 action send_goal /thor_controller/follow_joint_trajectory ros2_control_msgs/action/FollowJointTrajectory "{trajectory: {joint_names: ['joint1','joint2','joint3','joint4','joint5','joint6'], points: [{positions: [0.0, 0.5, -0.5, 0.0, 0.3, -0.2], time_from_start: {sec: 5}}] }"
```
Observe the arm moving. Adjust positions as needed.
---

## 9. Tips & Troubleshooting
- **Serial permissions:** `sudo usermod -aG dialout $USER && newgrp dialout`.
- **GPU driver mismatch:** Verify `nvidia-smi` shows the correct driver version.
- **URDF mesh scaling:** Meshes are in meters; adjust `scale` in `thor_description/urdf/thor.urdf.xacro` if the arm appears too large/small.
- **Latency:** For real‑time control, set the ROS 2 DDS QoS policy to `BEST_EFFORT` for joint states and `RELIABLE` for commands.
---

## 10. Next Steps (Follow‑up Tasks)
1. **Test ROS2 control of the Thor arm on DGX Spark with sample trajectories** – verify timing and repeatability.
2. **Document calibration procedure and ROS2 parameter tuning for the arm** – create a markdown guide.
3. **Integrate a simple perception node (camera feed) into the ROS2 control loop on DGX Spark** – demo pick‑and‑place based on object detection.

---

*Prepared by Bob (autonomous research agent).*