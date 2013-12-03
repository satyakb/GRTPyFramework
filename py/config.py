"""
Config File for Robot

#TODO: Setup for Constants File
"""

__author__ = "Sidd Karamcheti"

import wpilib
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController

# Joysticks
lstick = Attack3Joystick(1)
#rstick = Attack3Joystick(2)

#Solenoids (PINS TENTATIVE)
#solenoid = wpilib.Solenoid(7, 1)

compress = wpilib.Compressor(1, 1)
compress.Start()

#Motors 
left1 = wpilib.Talon(1)
left2 = wpilib.Talon(2)
left3 = wpilib.Talon(3)

right1 = wpilib.Talon(4)
right2 = wpilib.Talon(5)
right3 = wpilib.Talon(10)

lshifter = wpilib.Solenoid(1)
#rshifter = wpilib.Solenoid(1)

dt =  DriveTrain(left1, right1, left2, right2, left3, right3)
dt.set_scale_factors(1, -1, 1, -1, 1, -1)
ac = ArcadeDriveController(dt, lstick)

def shift_listener(sensor, state_id, datum):
	if state_id == 'trigger' and datum:
		lshifter.Set(not lshifter.Get())
		#rshifter.Set(datum)

lstick.add_listener(shift_listener)

sp = SensorPoller((lstick, ))