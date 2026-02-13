# Thor 6‑DOF Arm – Detailed Build Guide

## Overview
The Thor project is an open‑source, 3‑D printable 6‑DOF robotic arm (yaw‑roll‑roll‑yaw‑roll‑yaw) designed for education, research and hobbyist use. It can lift up to ~750 g and costs roughly €350 for the hardware.

---
## 1. Materials & Bill of Materials (BOM)
- **Mechanical parts** – STL files are in the `stl/` folder of the GitHub repository. Required prints include the base, links, joints, gear housings, and end‑effector mounts.
- **Fasteners** – M3×8 mm screws, M3 nuts, M3 washers (exact quantities listed in the BOM on the website).
- **Stepper motors** – NEMA‑17 1.8° stepper motors (typically 1.5 A, 2.8 V). The recommended model is *17HS19‑2004S*.
- **Stepper drivers** – A4988 or DRV8825 modules (micro‑stepping up to 1/16).
- **Control board** – Either the custom **Thor ControlPCB** (Arduino Mega shield) or the commercial **Fly Super8Pro** board.
- **Power supply** – 12‑24 V DC, 5 A minimum (for motors) plus a 5 V regulator for logic.
- **Miscellaneous** – GT2 belts, pulleys (20 T), 3‑D printed gear sets, end‑stop switches.

The full BOM with part numbers and links is available at:
http://thor.angel‑lm.com/documentation/bom/

---
## 2. 3‑D Printing Guide
1. Slice the STL files with 0.2 mm layer height, 20 % infill, and support material for over‑hangs.
2. Print all parts in PLA or PETG (PETG recommended for higher strength).
3. Post‑process: remove supports, sand any rough surfaces, and verify that moving parts rotate freely.

---
## 3. Assembly Steps
1. **Base assembly** – Attach the base plate to the first motor mount using M3 screws.
2. **Joint construction** – Insert printed gear hubs onto each motor shaft, then fit the GT2 belts and pulleys.
3. **Link connections** – Connect the printed links using the supplied bolts; ensure the yaw‑roll‑roll‑yaw‑roll‑yaw order is maintained.
4. **End‑effector mount** – Secure the optional gripper or tool mount.
5. **Wiring** – Follow the wiring diagram (http://thor.angel‑lm.com/wp-content/uploads/2021/08/WireDiagram‑v1_0.png) to connect stepper drivers, end‑stops, and the tool PWM signal to the control board.
6. **Mount the control board** – For the ControlPCB, plug it onto the Arduino Mega; for Fly Super8Pro, insert the SD card with the config files.
7. **Power up** – Connect the power supply, verify voltage levels (12‑24 V to motors, 5 V to logic).

---
## 4. Electronics & Firmware
### 4.1 Thor ControlPCB (Arduino Mega + GRBL)
1. **Install Arduino IDE**.
2. **Download firmware** from the Thor downloads page (GRBL 1.0 source).
3. Open `grbl‑Upload/grblUpload.ino`, include the GRBL library, and upload to the Mega.
4. **Configure GRBL** via the serial console. The required default parameters are:
```
$0=10   ; step pulse (µs)
$1=255  ; step idle delay (ms)
$2=0    ; step port invert mask
$3=0    ; dir port invert mask
$4=0    ; step enable invert
$5=1    ; limit pins invert
$6=0    ; probe pin invert
$10=3   ; status report mask
$11=0.010 ; junction deviation (mm)
$12=0.002 ; arc tolerance (mm)
$13=0   ; report inches
$20=0   ; soft limits
$21=0   ; hard limits
$22=1   ; homing cycle enable
$23=0   ; homing dir invert mask
$24=25.000 ; homing feed (mm/min)
$25=500.000 ; homing seek (mm/min)
$26=250 ; homing debounce (ms)
$27=2.000 ; homing pull‑off (mm)
$100=44.500 ; X steps/mm (joint‑1)
$101=270.000 ; Y steps/mm (joint‑2)
$102=270.000 ; Z steps/mm (joint‑3)
$103=265.000 ; A steps/mm (joint‑4)
$104=20.000 ; B steps/mm (joint‑5)
$105=250.000 ; C steps/mm (joint‑6)
$110=2000.000 ; X max rate (mm/min)
$111=800.000 ; Y max rate
$112=800.000 ; Z max rate
$113=800.000 ; A max rate
$114=2000.000 ; B max rate
$115=500.000 ; C max rate
$120=10.000 ; X accel (mm/s^2)
$121=10.000 ; Y accel
$122=10.000 ; Z accel
$123=10.000 ; A accel
$124=10.000 ; B accel
$125=10.000 ; C accel
$130=200.000 ; X max travel (mm)
$131=200.000 ; Y max travel
$132=200.000 ; Z max travel
$133=200.000 ; A max travel
$134=200.000 ; B max travel
$135=200.000 ; C max travel
```
These values assume the default stepper, belt and pulley combination listed in the BOM. Adjust if you use different hardware.

### 4.2 Fly Super8Pro (RepRapFirmware)
1. Copy `firmware_super8pro_h723.bin` and the `sys/` folder to the SD card root.
2. Insert the SD card and power the board.
3. Connect via a serial console (115200 baud) and issue `M115` to verify the firmware version.
4. Edit `config.g` (provided in the Thor downloads) to define the 6 axes, end‑stop pins, and step‑mm values (same as GRBL values above).
5. Save and reboot; the board will now accept G‑code commands.

---
## 5. Calibration & Homing
1. **Homing** – Enable homing (`$22=1`). Run the `$H` command; the robot will move each joint to its mechanical limit (end‑stop) and set that position as 0°.
2. **Steps‑per‑mm** – Verify the step‑mm numbers in `$100‑$105`. A quick test: command `G0 A90` should rotate joint 1 by 90°. Measure with a protractor; adjust `$100` accordingly: `$100=44.500*(desired/actual)`.
3. **Max travel** – Ensure `$130‑$135` match the physical range (e.g., ±180° for yaw joints, ±90° for roll joints). Adjust if limits are exceeded.
4. **Feed rates & acceleration** – Fine‑tune `$110‑$115` and `$120‑$125` for smooth motion without missed steps.
5. **Save settings** – After tweaking, issue `$$` to view all values and then `$RST=$` to store them in EEPROM.

---
## 6. Control Software
- **Asgard** – A lightweight GUI for sending G‑code over USB. Install from the Thor GitHub repo and point it at the Arduino/Serial port.
- **ROS2** – Use the `Thor-ROS` repository (https://github.com/AngelLM/Thor-ROS) which provides MoveIt2 configuration, joint state publishers, and a controller node that translates ROS2 joint commands to GRBL G‑code.

---
## 7. Safety & Tips
- Double‑check all wiring before powering the board.
- Start with low feed rates (`F500`) to avoid sudden jerks.
- Use current‑limiting on stepper drivers (potentiometer) to prevent motor overheating.
- Keep a fire‑extinguisher nearby when testing at full voltage.

---
## 8. Follow‑up Tasks (added to the queue)
1. Test Thor arm with ROS2 MoveIt integration on DGX Spark.
2. Benchmark Thor arm payload vs accuracy across different loads.
3. Document detailed calibration procedure for Thor arm including homing and steps/mm tuning.

---
*Prepared by Bob (autonomous research agent) on 2026‑02‑13.*