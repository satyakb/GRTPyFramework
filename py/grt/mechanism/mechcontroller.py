"""
Module for various drivetrain control mechanisms.
Listens to Attack3Joysticks or XboxJoysticks.
"""
#For Mock Build shop project, F period

class Attack3MechController:
    """
    Class for controlling DT in arcade drive mode, with one or two joysticks.
    """

    def __init__(self, joystick1, joystick2, pickup, shooter):
        """
        Initialize arcade drive controller with a DT and up to two joysticks.
        """
        self.dt = dt
        self.joystick1 = joystick1
        self.joystick2 = joystick2
        self.pickup = pickup
        self.shooter = shooter

        self.joystick1.add_listener(self._joy1listener)
        self.joystick2.add_listener(self._joy2listener)

    def _joy1listener(self, sensor, state_id, datum):
        if state_id == 'button2':
            if datum:
                self.pickpup.startep()
            else:
                self.pickup.endep()


    def _joy2listener(self, sensor, state_id, datum):
        if state_id == 'trigger' and self.joystick2.button3:
            self.shooter.fire()
        if state_id == 'trigger' and not self.joystick2.button3:
            self.shooter.retract()
        if state_id == 'button3':
            self.shooter.set_speed(1)


class XboxMechController:
    """
    Class for controlling DT in tank drive mode with two joysticks.
    """

    def __init__(self, dt, l_joystick, r_joystick, pickup, shooter):
        """
        Initializes self with a DT and left and right joysticks.
        """
        self.dt = dt
        self.l_joystick = l_joystick
        self.r_joystick = r_joystick
        l_joystick.add_listener(self._joylistener)
        r_joystick.add_listener(self._joylistener)
        self.pickup = pickup
        self.shooter = shooter

    def _joylistener(self, sensor, state_id, datum):
        if sensor in (self.joystick1, self.joystick2) and state_id in ('x_axis', 'y_axis'):
            self.dt.set_dt_output(self.l_joystick.y_axis,
                                  self.r_joystick.y_axis)
        if state_id == 'r_shoulder' and self.l_shoulder:
            self.shooter.fire()
        if state_id == 'r_shoulder' and not self.l_shoulder:
            slef.shooter.retract()
        if state_id == 'l_shoulder':
            if datum:
                self.shooter.set_speed(1)
            else:
                self.shooter.set_speed(0)
        if state_id == 'x_button':
            if datum:
                self.pickup.startep()
            else:
                self.pickup.endep()

