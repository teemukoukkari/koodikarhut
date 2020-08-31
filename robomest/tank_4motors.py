#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import struct

# Initialize motors and sensors
right_motor1 = Motor(Port.A)
right_motor2 = Motor(Port.B)
left_motor1 = Motor(Port.C)
left_motor2 = Motor(Port.D)
forward = 0
forward_r = 0
forward_l = 0
#obstacle_sensor = UltrasonicSensor(Port.S4)

# fLASH SOME LIGHTS
brick.light(Color.BLACK)
wait(200)
brick.light(Color.GREEN)
wait(200)
brick.light(Color.ORANGE)
wait(200)
brick.light(Color.RED)
wait(200)
brick.light(Color.YELLOW)
wait(200)

# Read buttons and act accordingly. PS button end program
brick.display.text("USE PS4 CONTROLLER")
brick.light(None)

# PS4 control code

# A helper function for converting stick values (0 - 255)
# to more usable numbers (-100 - 100)
def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
 
    val: float or int
    src: tuple
    dst: tuple
 
    example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
    """
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]


# Find the PS3 Gamepad:
# /dev/input/event3 is the usual file handler for the gamepad.
# look at contents of /proc/bus/input/devices if it doesn't work.
infile_path = "/dev/input/event4"

# open file in binary mode
in_file = open(infile_path, "rb")

# Read from the file
# long int, long int, unsigned short, unsigned short, unsigned int
FORMAT = 'llHHI'    
EVENT_SIZE = struct.calcsize(FORMAT)
event = in_file.read(EVENT_SIZE)
brick.sound.file(SoundFile.READY)
while event:
    brick.light(Color.GREEN)
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, event)
    if ev_type == 1:
        if code == 305: 
            # Ympyra nappi
            # Joukkueiden logot
            #brick.display.image('/home/robot/robomest/pics/bittipol.bmp')
            #brick.sound.file(SoundFile.HORN_1)
            #wait(2000)
            #wait(2000)
            #brick.display.image('/home/robot/robomest/pics/virtaluu.bmp')
            #brick.sound.file(SoundFile.LASER)
            wait(2000)
        if code == 304:
            # X nappi, soitetaan musiikkia
            brick.light(Color.ORANGE)
            brick.display.clear()
            brick.display.image('/home/robot/robomest/pics/logo3.bmp')
            brick.display.text("STOP to listen", (25,110))
            brick.display.text("to the anthem!")
            brick.sound.file('/home/robot/robomest/pics/robomestarit.wav',100)
            brick.display.image('/home/robot/robomest/pics/logo3.bmp')
            brick.light(Color.GREEN)
            brick.display.text("PS button to EXIT", (25,110))
        if code == 307:
            # Kolmio näyttää akun tilan
            # Show the current voltage on screen and with light colour
            brick.display.clear()
            brick.display.image('/home/robot/robomest/pics/logo1.bmp')
            if brick.battery.voltage() < 6899:
                brick.light(Color.RED)
                brick.display.image('/home/robot/robomest/pics/Bar 0.bmp')
            if brick.battery.voltage() < 7199 and brick.battery.voltage() > 6900:
                brick.light(Color.YELLOW)
                brick.display.image('/home/robot/robomest/pics/Bar 1.bmp')
            if brick.battery.voltage() < 7499 and brick.battery.voltage() > 7200:
                brick.light(Color.ORANGE)
                brick.display.image('/home/robot/robomest/pics/Bar 2.bmp')
            if brick.battery.voltage() < 7899 and brick.battery.voltage() > 7500:
                brick.light(Color.GREEN)
                brick.display.image('/home/robot/robomest/pics/Bar 3.bmp')
            if brick.battery.voltage() > 7900:
                brick.light(Color.GREEN)
                brick.display.image('/home/robot/robomest/pics/Bar 4.bmp')
            wait(2000)
            # Show the current voltage
            brick.display.text("Voltage is: {}".format(brick.battery.voltage()), (10,120))
            wait(3000)
            brick.display.image('/home/robot/robomest/pics/logo3.bmp')
            brick.display.text("PS button to EXIT", (25,110))
        if code == 308:
            # Nelio nappi, soitetaan musiikkia
            brick.light(Color.ORANGE)
            brick.display.clear()
            brick.display.image('/home/robot/robomest/pics/logo3.bmp')
            brick.display.text("STOP to listen", (25,110))
            brick.display.text("to the anthem!")
            brick.sound.file('/home/robot/robomest/pics/imperial.wav',100)
            brick.display.image('/home/robot/robomest/pics/logo3.bmp')
            brick.light(Color.GREEN)
            brick.display.text("PS button to EXIT", (25,110))
        if code == 316:
            break
    # Type 1 event - buttons
        # Code 304 - X
        # Code 308 - Square
        # Code 307 - Triangle
        # Code 305 - Circle
        # Code 318 - right stick pressed
        # Code 317 - l stick pressed
        # Code 310 - L1 trigger
        # Code 311 - R1 trigger
        # Code 314 - Share button
        # Code 315 - Options button
        # Code 316 - PS button
    elif ev_type == 3:
    # Type 3 event - sticks
        # Code 3 - right stick horizontal
        # Code 2 - L2 trigger
        # Code 5 - R2 trigger
        # Code 0 - left stick horizontal (left is 0)
        # Code 1 - left stick vertical (forward is 0)
        # Code 4 - r stick vertical
        # Code 17 - dpad vertical
        # Code 16 - dpad horizontal
        if code == 1: # Vasen tatti ylos/alas
            forward_l = scale(value, (0,255), (100,-100))
            brick.light(Color.RED)
        if code == 4: # Oikea tatti ylos/alas
            forward_r = scale(value, (0,255), (100,-100))
            brick.light(Color.RED)
    # Asetetaan tattien skaalatut signaalit moottreiden jannitteeksi
    left_motor1.dc(-forward_l)
    right_motor1.dc(-forward_r)
    left_motor2.dc(forward_l)
    right_motor2.dc(forward_r)

    # Finally, read another event
    event = in_file.read(EVENT_SIZE)

in_file.close()

# PS4 control code ends
# Clear screen, print instructions
brick.display.clear()
brick.display.image('/home/robot/robomest/pics/logo3.bmp')
brick.display.text("Press any button to exit", (1,115))

# Wait until a button is pressed
while not brick.buttons():
    wait(10)
    
brick.sound.file(SoundFile.THANK_YOU)
brick.sound.file(SoundFile.GOODBYE)