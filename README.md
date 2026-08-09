# ROS 2 Robot Command Controller

A ROS 2 Python package that controls robot movement through publisher and controller nodes.

## Features

- Forward movement
- Left and right turning
- Stop command
- ROS 2 publisher-subscriber communication
- Command-line robot control

## Technologies

- Python
- ROS 2
- rclpy
- Publisher/Subscriber communication

## Package Structure

- `command_publisher.py` — publishes robot movement commands
- `command_controller.py` — receives commands and controls robot behavior
- `setup.py` — Python package configuration
- `package.xml` — ROS 2 package metadata

## How to Run

Build the package:

```bash
cd ~/ros2_ws
colcon build --packages-select robot_command_controller
source install/setup.bash
