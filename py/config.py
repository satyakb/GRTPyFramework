"""
Config File for Robot
"""

__author__ = "Sidd Karamcheti"

import wpilib
import thread
import time
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller

# Joysticks
lstick = Attack3Joystick(1)

voldemort = wpilib.Solenoid(1)

terminator = wpilib.Solenoid(2)

zombie = wpilib.Solenoid(3)
door = wpilib.Solenoid(4)

cookiemonster = wpilib.Solenoid(5)

voodoodoll = wpilib.Solenoid(6)

spiderbear = wpilib.Talon(1)

# Mechs:
# Voldemort, SpiderBear, VoodooDoll, Terminator, ZombieDoor, CookieMonster


def delay_actuate(actuator, datum, delaytime):
    time.sleep(delaytime)
    actuator.Set(datum)


def vold_listener(source, id, datum):
    if id == 'trigger' and datum:
        voldemort.Set(not voldemort.Get())


def term_listener(source, id, datum):
    if id == 'button2' and datum:
        terminator.Set(not terminator.Get())


def zomb_listener(source, id, datum):
    if id == 'button3' and datum:
        if door.Get() is False:
            door.Set(True)
            thread.start_new_thread(delay_actuate, (zombie, True, 2))
        else:
            zombie.Set(False)
            thread.start_new_thread(delay_actuate, (door, True, 2))
    elif id == 'button10' and datum:
        door.Set(not door.Get())
    elif id == 'button11' and datum:
        zombie.Set(not zombie.Get())


def bear_listener(source, id, datum):
    if id == 'y_axis':
        spiderbear.Set(datum * 0.25)


def cook_listener(source, id, datum):
    if id == 'button4' and datum:
        cookiemonster.Set(not cookiemonster.Get())


def vood_listener(source, id, datum):
    if id == 'button5' and datum:
        voldemort.Set(not voldemort.Get())

for l in (vold_listener, term_listener, zomb_listener,
          cook_listener, bear_listener):
    lstick.add_listener(l)


sp = SensorPoller((lstick, ))
