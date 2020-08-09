#!/usr/bin/env pybricks-micropython

#System imports
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

#Own imports
from gamepad import *

# Linear scaling function
def scale(val, src, dst):
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

# Motor ports
# A B
# C D
front_left = Motor(Port.A)
front_right = Motor(Port.B)
back_left = Motor(Port.C)
back_right = Motor(Port.D)

# Declaring motor speed variables
left_speed = 0
right_speed = 0

gamepad = Gamepad() # Creating gamepad handler
brick.sound.beep() # Playing sound when ready

event = gamepad.next() # Reading first event
while event:

    #Playing sound if X pressed
    if event.type == EVENT_BUTTON and event.code == BUTTON_X and event.value == BUTTON_PRESS:
        brick.sound.beep(500, 500, 50)
        
    # Reading analog stick input and adjusting motor speed
    if event.type == EVENT_ANALOG:
        if event.code == ANALOG_LEFT_VERTICAL: 
            left_speed = scale(event.value, (0,255), (100,-100))
        if event.code == ANALOG_RIGHT_VERTICAL:
            right_speed = scale(event.value, (0,255), (100,-100))
    
    # Setting motor voltages
    front_left.dc(left_speed)
    front_right.dc(right_speed)
    back_left.dc(-left_speed)
    back_right.dc(-right_speed)

    event = gamepad.next() # Reading next event

gamepad.cleanup() # Cleaning up gamepad