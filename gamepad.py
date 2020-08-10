#!/usr/bin/env pybricks-micropython

import struct

# Event types (event.type)
EVENT_BUTTON = 1
EVENT_ANALOG = 3

# Button codes (event.code)
BUTTON_X = 304
BUTTON_CIRCLE = 305
BUTTON_TRIANGLE = 307
BUTTON_SQUARE = 308
BUTTON_L1 = 310
BUTTON_R1 = 311
BUTTON_L2 = 312
BUTTON_R2 = 313
BUTTON_SHARE = 314
BUTTON_OPTIONS = 315
BUTTON_PS = 316
BUTTON_LEFT_STICK = 317
BUTTON_RIGHT_STICK = 318

# Button states (event.value)
BUTTON_RELEASE = 0
BUTTON_PRESS = 1

# Analog codes (event.code)
ANALOG_LEFT_HORIZONTAL = 0
ANALOG_LEFT_VERTICAL = 1
ANALOG_LEFT_TRIGGER = 2
ANALOG_RIGHT_HORIZONTAL = 3
ANALOG_RIGHT_VERTICAL = 4
ANALOG_RIGHT_TRIGGER = 5
ANALOG_PAD_HORIZONTAL = 16
ANALOG_PAD_VERTICAL = 17

# https://docs.python.org/3/library/struct.html
# C struct format (long, long, unsigned short, unsigned short, unsigned int)
# Size should be 4 + 4 + 2 + 2 + 4 = 16 bytes
STRUCT_FORMAT = "llHHI"
STRUCT_SIZE = struct.calcsize(STRUCT_FORMAT)

# Should be PS4 gamepad file handler
FILE_HANDLER = "/dev/input/event4"

# Simple class for unpacking & storing event data
class GamepadEvent:
    def __init__(self, event):
        (self.sec, self.usec, self.type, self.code, self.value) = struct.unpack(STRUCT_FORMAT, event)

# Gamepad class for both projects
class Gamepad:

     # Opening file in read binary mode
    def __init__(self):
        self.event_file = open(FILE_HANDLER, "rb")
    
    # Reading next event
    def next(self):
        return GamepadEvent(self.event_file.read(STRUCT_SIZE))
    
    # Closing file handler
    def cleanup(self):
        self.event_file.close()