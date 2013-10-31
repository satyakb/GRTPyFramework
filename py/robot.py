__author__ = "Sidd Karamcheti, Calvin Huang"

import wpilib
from config import sp, lstick
import random


def CheckRestart():
    if lstick.button10:
        raise RuntimeError("Restart")


class MyRobot(wpilib.SimpleRobot):
    def Disabled(self):
        while self.IsDisabled():
            CheckRestart()
            wpilib.Wait(0.01)

    def Autonomous(self):
        self.GetWatchdog().SetEnabled(False)
        while self.IsAutonomous() and self.IsEnabled():
            lstick.button2 = True
            lstick.button2 = False
            wpilib.Wait(random.uniform(2.0 / 5, 3))
            lstick.button3 = True
            lstick.button3 = False
            wpilib.Wait(random.uniform(2.0 / 5, 3))
            lstick.button4 = True
            lstick.button4 = False
            wpilib.Wait(random.uniform(2.0 / 5, 3))
            lstick.button5 = True
            lstick.button5 = False
            wpilib.Wait(random.uniform(2.0 / 5, 3))
            lstick.trigger = True
            lstick.trigger = False
            wpilib.Wait(random.uniform(2.0 / 5, 3))
            CheckRestart()

    def OperatorControl(self):
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)

        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            CheckRestart()

            # Motor control
            sp.poll()

            wpilib.Wait(0.04)
            #Testing Github editor


def run():
    robot = MyRobot()
    robot.StartCompetition()
