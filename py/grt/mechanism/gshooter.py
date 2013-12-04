# Shooter for G Period

class GShooter:
    def __init__(self, solenoid):
        self.solenoid = solenoid
    
    def fire(self):
        self.solenoid.Set(True)

    def unfire(self):
        self.solenoid.Set(False)

