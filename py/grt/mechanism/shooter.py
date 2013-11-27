class Shooter:
    def __init__(self, fly_motor1, fly_motor2, shootermotor, luna):
        self.fly_motor1 = fly_motor1
        self.fly_motor2 = fly_motor2
        self.shootermotor = shootermotor
        self.luna = luna

    def setflywheelspeed(self, value):
        self.fly_motor1.Set(value)
        self.fly_motor2.Set(value)

    def activateluna(self):
        self.luna.Set(True)

    def deactivateluna(self):
        self.luna.Set(False)

    def setraiserspeed(self, value):
        self.shootermotor.Set(-value)
