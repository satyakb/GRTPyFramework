from threading import Timer
class Pickup:
    def __init__(self, motor):
        self.motor = motor
    def startep(self):
        self.motor.Set(1)
    def endep(self):
        self.motor.Set(-1)

    
