#!/usr/bin/env pybricks-micropython

# Own imports
from common import *

# Motor ports
motor_rotation = Motor(Port.A)
motor_ballshooter = Motor(Port.B)
motor_hammer = Motor(Port.C)

# Event handler, called from common.py
def on_event(event):

    # If button is pressed/released
    if event.type == EVENT_BUTTON:

        # If L1 pressed move shooter motor forward
        # and if R1 move it backward
        # and if either is released stop the motor

        if event.code == BUTTON_L1:
            if event.value == BUTTON_PRESS:
                motor_ballshooter.dc(100)
            else:
                motor_ballshooter.dc(0)
        
        elif event.code == BUTTON_R1:
            if event.value == BUTTON_PRESS:
                motor_ballshooter.dc(-100)
            else:
                motor_ballshooter.dc(0)

    # Adjusting rotation & hammer motor voltage based on analog stick input
    elif event.type == EVENT_ANALOG:
        if event.code == ANALOG_LEFT_HORIZONTAL:
            motor_rotation.dc(scale(event.value))
        elif event.code == ANALOG_RIGHT_VERTICAL:
            motor_hammer.dc(scale(event.value))

# Cleanup function, called from common.py
def on_cleanup():
    motor_rotation.dc(0)
    motor_ballshooter.dc(0)
    motor_hammer.dc(0)

# Entering main loop, defined in common.py
main_loop(on_event, on_cleanup)