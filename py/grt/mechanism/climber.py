class Climber:

    def __init__(self, climbersolenoid):
        self.climbersolenoid = climbersolenoid

    def raiseclimber(self):
        self.climbersolenoid.Set(True)

    def lowerclimber(self):
        self.climbersolenoid.Set(False)
