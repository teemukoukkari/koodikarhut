#!/usr/bin/env pybricks-micropython

# Own imports
from common import *

# Motor ports
motor_rotation = Motor(Port.A)
motor_angle = Motor(Port.B)
motor_shooter = Motor(Port.C)
motor_missile = Motor(Port.D)

l1down = False
r1down = False

# Event handler, called from common.py
def on_event(event):
    global l1down, r1down

    # Adjusting rotation & hammer motor voltage based on analog stick input
    if event.type == EVENT_ANALOG:
        if event.code == ANALOG_LEFT_HORIZONTAL:
            motor_rotation.dc(scale(event.value))
        elif event.code == ANALOG_LEFT_VERTICAL:
            motor_angle.dc(-scale(event.value))
        elif event.code == ANALOG_RIGHT_HORIZONTAL:
            motor_missile.dc(scale(event.value))

    if event.type == EVENT_BUTTON:
        if event.code == BUTTON_L1:
            if event.value == BUTTON_PRESS:
               l1down = True
            else:
                l1down = False
        elif event.code == BUTTON_R1:
            if event.value == BUTTON_PRESS:
                r1down = True
            else:
                r1down = False
    
    if l1down:
        motor_shooter.dc(100)
    elif r1down:
        motor_shooter.dc(-100)
    else:
        motor_shooter.dc(0)

# _Cleanup function, called from common.py
def on_cleanup():
    motor_rotation.dc(0)
    motor_angle.dc(0)

# Entering main loop, defined in common.py
main_loop(on_event, on_cleanup)