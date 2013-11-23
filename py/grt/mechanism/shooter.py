import wpilib
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller

class Shooter:
	def __init__(self, joystick, flyMotor1, flyMotor2, shooterMotor, luna):
		self.joystick = joystick
		self.flyMotor1 = flyMotor1
		self.flyMotor2 = flyMotor2
		self.shooterMotor = shooterMotor
		self.luna = luna
                self.running = False #is the flywheel motor running?
		self.joystick.add_listener(self.flywheel_listener)
		self.joystick.add_listener(self.luna_listener)
		self.joystick.add_listener(self.shooterMotor_listener)

	def flywheel_listener(self, source, id, datum):
		if id == 'button3':
        		self.running = True
			if datum:
				self.flyMotor1.Set(1)
				self.flyMotor2.Set(1)
			else:
				self.flyMotor1.Set(0)
				self.flyMotor2.Set(0)
		else:
			self.running = False

	def luna_listener(self, source, id, datum):
		if id == 'trigger' and self.running:
			self.luna.Set(datum)


	def shooterMotor_listener(self, source, id, datum):
		if id == 'y_axis':
			self.shooterMotor.Set(-datum)

