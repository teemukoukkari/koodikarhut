#!/usr/bin/env pybricks-micropython

#System imports
from pybricks import ev3brick as brick

#Own imports
from gamepad import *

brick.sound.beep() # Playing sound on startup

gamepad = Gamepad() # Creating gamepad handler

event = gamepad.next() # Reading first event
while event:

    #Playing sound if X pressed
    if event.type == EVENT_BUTTON and event.code == BUTTON_X and event.value == BUTTON_PRESS:
        brick.sound.beep(500, 500, 50) 
    
    event = gamepad.next() # Reading next event

gamepad.cleanup() # Cleaning up gamepad