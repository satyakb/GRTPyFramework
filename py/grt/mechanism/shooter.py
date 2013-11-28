class Shooter:
    def __init__(self, joystick, fly_motor1, fly_motor2, shootermotor, luna):
        self.joystick = joystick
        self.fly_motor1 = fly_motor1
        self.fly_motor2 = fly_motor2
        self.shootermotor = shootermotor
        self.luna = luna
        self.joystick.add_listener(self.flywheel_listener)
        self.joystick.add_listener(self.luna_listener)
        self.joystick.add_listener(self.shootermotor_listener)

    def flywheel_listener(self, source, id, datum):
        if id == 'button3':
            if datum:
                self.fly_motor1.Set(1)
                self.fly_motor2.Set(1)
            else:
                self.fly_motor1.Set(0)
                self.fly_motor2.Set(0)

    def luna_listener(self, source, id, datum):
        if id == 'trigger' and self.joystick.button3:
            self.luna.Set(datum)
        if id == 'trigger' and not self.joystick.button3:
            self.luna.Set(False)

    def shootermotor_listener(self, source, id, datum):
        if id == 'y_axis':
            self.shootermotor.Set(-datum)
