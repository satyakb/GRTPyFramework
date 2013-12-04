"""
Config File for Robot

#TODO: Setup for Constants File
"""



import wpilib
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.pickup import Pickup
from grt.mechanism.shooter import Shooter
from grt.mechanism.gshooter import GShooter
from grt.mechanism.mechcontroller import Attack3MechController
from grt.mechanism.mechcontroller import Attack3MechControllerG
from grt.mechanism.mechcontroller import XboxMechController
# Joysticks
lstick = Attack3Joystick(1)
rstick = Attack3Joystick(2)
sp = SensorPoller((lstick, rstick))


#Solenoids (PINS TENTATIVE)
#solenoid = wpilib.Solenoid(7, 1)

#Motors (PINS TENTATIVE)
lfm = wpilib.Talon(3)
lrm = wpilib.Talon(4)
rfm = wpilib.Talon(1)
rrm = wpilib.Talon(2)

#Shifting solenoids
leftShift = wpilib.Solenoid(5)
rightShift = wpilib.Solenoid(6)

fly1 = wpilib.Talon(9)
fly2 = wpilib.Talon(10)

# F Period
# epmotor = wpilib.Victor(5)

# act = wpilib.Solenoid(8)

# G Period
epmotor = wpilib.Victor(5)
shooter = wpilib.Solenoid(8)

compressor = wpilib.Compressor(1, 1)
compressor.Start()

# F Period
# shooter = Shooter(fly1, fly2, act)
# pickup = Pickup(epmotor)

# G Period
pickup = Pickup(epmotor)
gshooter = GShooter(shooter)


dt = DriveTrain(lfm, rfm, lrm, rrm, leftShift, rightShift)

dt.set_scale_factors(1, -1, 1, -1)
# F Period
# xc = XboxMechController(dt, lstick, rstick, pickup, shooter)
# atc = Attack3MechController(lstick, rstick, pickup, shooter)

# G Period
atcg = Attack3MechControllerG(lstick, rstick, pickup, gshooter)


ac = ArcadeDriveController(dt, lstick)
