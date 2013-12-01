#Pickup mechanism for F Period mock build project
class Pickup:
    '''
    The Pickup mechanism consists of only one motor
    and a linked belt system
    '''
    def __init__(self, motor):
        self.motor = motor
    def startep(self):
        self.motor.Set(1)
    def endep(self):
        self.motor.Set(-1)

    
