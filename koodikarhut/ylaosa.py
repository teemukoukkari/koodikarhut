#!/usr/bin/env pybricks-micropython

# Own imports
from common import *

# Motor ports
motor_rotation = Motor(Port.A)
motor_hammer = Motor(Port.C)

# Event handler, called from common.py
def on_event(event):

    # Adjusting rotation & hammer motor voltage based on analog stick input
    if event.type == EVENT_ANALOG:
        if event.code == ANALOG_LEFT_HORIZONTAL:
            motor_rotation.dc(scale(event.value))
        elif event.code == ANALOG_RIGHT_VERTICAL:
            motor_hammer.dc(scale(event.value))

# Cleanup function, called from common.py
def on_cleanup():
    motor_rotation.dc(0)
    motor_hammer.dc(0)

# Entering main loop, defined in common.py
main_loop(on_event, on_cleanup)