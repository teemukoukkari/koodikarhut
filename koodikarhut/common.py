#!/usr/bin/env pybricks-micropython

# Pybricks imports
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Own imports
from gamepad import *

# Converting from range (0,255) to (-100,100)
def scale(val):
    return 200 * float(val/255) - 100

# Function playing beep sound
def beep():
    brick.sound.beep(500, 500, 100)

# Main loop, called from alaosa.py or ylaosa.py
def main_loop(on_event, on_cleanup):
  
    # Creating gamepad handler
    gamepad = Gamepad()

    # Beeping when ready
    beep()

    # Reading first event & entering event loop
    event = gamepad.next()
    while event:

        # Handling exit & connection test
        if event.type == EVENT_BUTTON and event.value == BUTTON_PRESS:
            
            # Exiting if options button is pressed
            if event.code == BUTTON_OPTIONS:
                break
            
            # Playing beep if share button is pressed
            elif event.code == BUTTON_SHARE:
                beep()
        
        # Running project specific event code
        on_event(event)
        
        # Reading next event
        event = gamepad.next()

    # Running project specific cleanup code
    on_cleanup()

    # Cleaning up gamepad
    gamepad.cleanup()

    # Beeping on shutdown
    brick.sound.beep(500, 500, 100)