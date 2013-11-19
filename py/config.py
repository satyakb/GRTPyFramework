"""
Config File for Robot

#TODO: Setup for Constants File
"""

__author__ = "Sidd Karamcheti"

import wpilib
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller
# from grt.mechanism.drivetrain import DriveTrain
# from grt.mechanism.drivecontroller import ArcadeDriveController

# Joysticks
lstick = Attack3Joystick(1)
#rstick = Attack3Joystick(2)

#Solenoids (PINS TENTATIVE)
#solenoid = wpilib.Solenoid(7, 1)

#Motors 
motor1 = wpilib.Talon(3)
motor2 = wpilib.Talon(1)
motor3 = wpilib.Talon(2)

def motor_listener(source, id, datum):
	if id == 'y_axis':
		motor1.Set(datum)
		motor2.Set(datum)
		motor3.Set(datum)

lstick.add_listener(motor_listener)

sp = SensorPoller((lstick, ))