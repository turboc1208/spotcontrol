#!/usr/bin/env python3
from pyirobot import Robot, RobotError, BinStatus
import json

robot_ip = "192.168.2.161"

print("Querying robot password...")
robot_password = Robot.GetPassword(robot_ip)
print(robot_password)
print()

print("Querying robot status...")
r = Robot(robot_ip, robot_password)
status = r.GetStatus()
if status["mission"]["binStatus"] == BinStatus.Full:
    print("Bin is full!")
    print()

print(json.dumps(status, indent=4))

