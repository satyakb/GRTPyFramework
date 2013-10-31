"""
Config File for Robot
"""

__author__ = "Sidd Karamcheti"

import wpilib
from threading import Thread
import time
from grt.sensors.attack_joystick import Attack3Joystick
from grt.core import SensorPoller

# Joysticks
lstick = Attack3Joystick(1)

voldemort = wpilib.Solenoid(6)

terminator = wpilib.Solenoid(4)

zombie = wpilib.Solenoid(1)
door = wpilib.Solenoid(7)

cookiemonster = wpilib.Solenoid(2)

voodoodoll = wpilib.Solenoid(5)

spiderbear = wpilib.Talon(1)

# Mechs:
# Voldemort, SpiderBear, VoodooDoll, Terminator, ZombieDoor, CookieMonster


def delay_actuate(actuator, datum, delaytime):
    time.sleep(delaytime)
    actuator.Set(datum)


def print_listener(source, id, datum):
    print(id + str(datum))


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
            Thread(target=delay_actuate, args=(zombie, True, 2)).start()
        else:
            zombie.Set(False)
            Thread(target=delay_actuate, args=(door, False, 0.5)).start()
    if id == 'button6' and datum:
        door.Set(not door.Get())
    elif id == 'button7' and datum:
        zombie.Set(not zombie.Get())


def bear_listener(source, id, datum):
    if id == 'y_axis':
        spiderbear.Set(datum * 0.25)


def cook_listener(source, id, datum):
    if id == 'button4' and datum:
        cookiemonster.Set(not cookiemonster.Get())


def vood_listener(source, id, datum):
    if id == 'button5' and datum:
        voodoodoll.Set(not voodoodoll.Get())

for l in (vold_listener, term_listener, zomb_listener,
          cook_listener, bear_listener, vood_listener):
    lstick.add_listener(l)


sp = SensorPoller((lstick, ))
