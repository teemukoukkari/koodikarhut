#!/usr/bin/env pybricks-micropython

# Own imports
from common import *

# Motor ports
# A B
# C D
front_left = Motor(Port.A)
front_right = Motor(Port.B)
back_left = Motor(Port.C)
back_right = Motor(Port.D)

# Function that stops all motors
def stop_motors():
    front_left.dc(0)
    front_right.dc(0)
    back_left.dc(0)
    back_right.dc(0)

# Event handler, called from common.py
def on_event(event):

    # Reading analog stick input and adjusting motor voltages
    if event.type == EVENT_ANALOG:
        if event.code == ANALOG_LEFT_VERTICAL: 
            left_voltage = scale(event.value)
            front_left.dc(-left_voltage)
            back_left.dc(left_voltage)
        elif event.code == ANALOG_RIGHT_VERTICAL:
            right_voltage = scale(event.value)
            front_right.dc(-right_voltage)
            back_right.dc(right_voltage)

# Cleanup function, called from common.py
def on_cleanup():
    stop_motors()

# Entering main loop, defined in common.py
main_loop(on_event, on_cleanup)