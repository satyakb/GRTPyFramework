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
from grt.mechanism.climber import Climber
from grt.mechanism.shooter import Shooter
from grt.mechanism.intake import Intake
from grt.mechanism.mechcontroller import Attack3Mechcontroller
from grt.mechanism.mechcontroller import XboxMechController
# from grt.mechanism.mechs import Mechanisms

# Joysticks
lstick = Attack3Joystick(1)
rstick = Attack3Joystick(2)

sp = SensorPoller((lstick, rstick, ))

#Solenoids (PINS TENTATIVE)
#solenoid = wpilib.Solenoid(7, 1)

#Motors
lfm = wpilib.Talon(3)
lrm = wpilib.Talon(4)
rfm = wpilib.Talon(1)
rrm = wpilib.Talon(2)

#Shifting solenoids
leftShift = wpilib.Solenoid(5)
rightShift = wpilib.Solenoid(6)

shooter_pivot_motor = wpilib.Victor(8)
flywheel_1 = wpilib.Talon(9)
flywheel_2 = wpilib.Talon(10)

belts = wpilib.Victor(5)
ep_raiser = wpilib.Victor(6)
ep_roller = wpilib.Victor(7)

luna = wpilib.Solenoid(8)
climber_solenoid = wpilib.Solenoid(7)

compressor = wpilib.Compressor(1, 1)
compressor.Start()

climber = Climber(climber_solenoid)
shooter = Shooter(flywheel_1, flywheel_2, shooter_pivot_motor, luna)
intake = Intake(belts, ep_roller)

dt = DriveTrain(lfm, rfm, lrm, rrm, leftShift, rightShift)
dt.set_scale_factors(1, -1, 1, -1)

# MechXontrollers:

# Xbox Joystick
xc = XboxMechController(dt, lstick, rstick, climber, intake, shooter)
atc = Attack3MechController(lstick, rstick, climber, intake, shooter)
ac = ArcadeDriveController(dt, lstick)
