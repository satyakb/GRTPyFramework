"""
Config File for Robot

#TODO: Setup for Constants File
"""

__author__ = "Sidd Karamcheti"

import wpilib
from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.buttonbard import ButtonBoard
from grt.core import SensorPoller
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController

#Button Board
bboard = ButtonBoard()

def bBoardListener(sensor, state_id, datum):
	print(sensor, state_id, datum)

bboard.add_listener(bBoardListener)

# Joysticks
lstick = Attack3Joystick(1)

sp = SensorPoller((lstick, bboard, ))



#Solenoids (PINS TENTATIVE)
#solenoid = wpilib.Solenoid(7, 1)

#Motors (PINS TENTATIVE)
lfm = wpilib.Talon(3)
lrm = wpilib.Talon(4)
rfm = wpilib.Talon(1)
rrm = wpilib.Talon(2)

dt = DriveTrain(lfm, rfm, lrm, rrm)
dt.set_scale_factors(1, -1, -1, 1)

ac = ArcadeDriveController(dt, lstick)
