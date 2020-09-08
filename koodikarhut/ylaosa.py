#!/usr/bin/env pybricks-micropython

# Own imports
from common import *

# Motor ports
motor_rotation = Motor(Port.A)
motor_angle = Motor(Port.B)
motor_shooter = Motor(Port.C)

# Event handler, called from common.py
def on_event(event):

    # Adjusting rotation & hammer motor voltage based on analog stick input
    if event.type == EVENT_ANALOG:
        if event.code == ANALOG_LEFT_HORIZONTAL:
            motor_rotation.dc(scale(event.value))
        elif event.code == ANALOG_LEFT_VERTICAL:
            motor_angle.dc(-scale(event.value))

    if event.type == EVENT_BUTTON:
        if event.code == BUTTON_L1:
            if event.value == BUTTON_PRESS:
               motor_shooter.dc(100)
            else:
                motor_shooter.dc(0)
        elif event.code == BUTTON_R1:
            if event.value == BUTTON_PRESS:
                motor_shooter.dc(-100)
            else:
                motor_shooter.dc(0) 

# _Cleanup function, called from common.py
def on_cleanup():
    motor_rotation.dc(0)
    motor_angle.dc(0)

# Entering main loop, defined in common.py
main_loop(on_event, on_cleanup)