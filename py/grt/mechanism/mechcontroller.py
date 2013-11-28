"""
Module for various drivetrain control mechanisms.
Listens to Attack3Joysticks or XboxJoysticks.
"""


class Attack3MechController:
    """
    Class for controlling DT in arcade drive mode, with one or two joysticks.
    """

    def __init__(self, joystick1, joystick2, climber, intake, shooter):
        """
        Initialize arcade drive controller with a DT and up to two joysticks.
        """
        self.dt = dt
        self.joystick1 = joystick1
        self.joystick2 = joystick2
        self.climber = climber
        self.intake = intake
        self.shooter = shooter

        self.joystick1.add_listener(self._joy1listener)
        self.joystick2.add_listener(self._joy2listener)

    def _joy1listener(self, sensor, state_id, datum):
        if state_id == 'button2':
            if datum:
                self.intake.startpickup()
            else:
                self.intake.endpickup()
        elif state_id == 'button3':
            if datum:
                self.intake.kickoutfrisbees()
            else:
                self.intake.stopkickoutfrisbees()


    def _joy2listener(self, sensor, state_id, datum):
        if state_id == 'button4':
            if datum:
                self.climber.raiseclimber()
            else:
                self.climber.lowerclimber()
        if state_id == 'trigger' and self.joystick2.button3:
            self.shooter.activateluna()
        if state_id == 'trigger' and not self.joystick2.button3:
            self.shooter.deactivateluna()
        if state_id == 'y_axis':
            self.shooter.setraiserspeed(datum)
        if state_id == 'button3':
            if datum:
                self.shooter.setflywheelspeed(1)
            else:
                self.shooter.setflywheelspeed(0)



class XboxMechController:
    """
    Class for controlling DT in tank drive mode with two joysticks.
    """

    def __init__(self, dt, l_joystick, r_joystick, climber, intake, shooter):
        """
        Initializes self with a DT and left and right joysticks.
        """
        self.dt = dt
        self.l_joystick = l_joystick
        self.r_joystick = r_joystick
        l_joystick.add_listener(self._joylistener)
        r_joystick.add_listener(self._joylistener)
        self.climber = climber

    def _joylistener(self, sensor, state_id, datum):
        if sensor in (self.joystick1, self.joystick2) and state_id in ('x_axis', 'y_axis'):
            self.dt.set_dt_output(self.l_joystick.y_axis,
                                  self.r_joystick.y_axis)
        if state_id == "y_button":
            if datum:
                self.climber.raiseclimber()
            else:
                self.climber.lowerclimber()
        if state_id == 'r_shoulder' and self.l_shoulder:
            self.shooter.activateluna()
        if state_id == 'r_shoulder' and not self.l_shoulder:
            self.shooter.deactivateluna()
        if state_id == 'l_shoulder':
            if datum:
                self.shooter.setflywheelspeed(1)
            else:
                self.shooter.setflywheelspeed(0)
        if state_id == 'x_button':
            if datum:
                self.intake.startpickup()
            else:
                self.intake.endpickup()
        if state_id == 'a_button':
            if datum:
                self.intake.kickoutfrisbees()
            else:
                self.intake.stopkickoutfrisbees()