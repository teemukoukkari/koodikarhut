#!/usr/bin/env pybricks-micropython

# Documentation:
# https://docs.pybricks.com/en/latest/hubs.html#ev3-brick-mindstorms

#System imports
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

#Own imports
from gamepad import *

# Converting from range (0,255) to (-100,100)
def scale(val):
    return 200 * float(val/255) - 100

# Motor ports
# A B
# C D
front_left = Motor(Port.A)
front_right = Motor(Port.B)
back_left = Motor(Port.C)
back_right = Motor(Port.D)

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
            left_voltage = scale(event.value)
            front_left.dc(left_voltage)
            back_left.dc(-left_voltage)
        if event.code == ANALOG_RIGHT_VERTICAL:
            right_voltage = scale(event.value)
            front_right.dc(right_voltage)
            back_right.dc(-right_voltage)
    
    event = gamepad.next() # Reading next event

gamepad.cleanup() # Cleaning up gamepad