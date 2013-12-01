#Ball shooter for the mock build shop project, F period
class Shooter:
    '''
    The shooter mechanism consists of two motors (fly1, fly2)
    and an actuator (act)
    '''
    def __init__(self, fly1, fly2, act):
        self.fly1 = fly1
        self.fly2 = fly2
        self.act = act
    def set_speed(self, speed)
        self.fly1.Set(speed)
        self.fly2.Set(speed)
    def shoot(self):
        self.act.Set(True)
    def retract(self):
        self.act.Set(False)
