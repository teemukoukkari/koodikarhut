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
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
steer_motor = Motor(Port.A)
forward = 0
left = 0
robot = DriveBase(left_motor, right_motor, 56, 120)
obstacle_sensor = UltrasonicSensor(Port.S4)

# Show the current voltage and active program
brick.display.text("Voltage is: {}".format(brick.battery.voltage()), (5,110))
wait(2000)
# Read buttons and act accordingly. UP button ends
brick.display.text("RACECAR")
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

while event:
    brick.light(Color.GREEN)
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, event)
    if ev_type == 1:
        if code == 305: 
            # Taskuparkki Ympyralla
            brick.light(Color.RED)
            brick.light(Color.ORANGE)
            steer_motor.track_target(45)
            #brick.sound.beep(500, 1000, 200)
            robot.drive_time(-40, 0, 1000)
            steer_motor.track_target(0)
            #.sound.beep(500, 1000, 200)
            robot.drive_time(-40, 0, 500)
            steer_motor.track_target(-35)
            #brick.sound.beep(500, 1000, 200)
            robot.drive_time(-40, 0, 1000)
            steer_motor.track_target(0)
            #brick.sound.beep(500, 1000, 200)
            robot.drive_time(-30, 0, 300)
            robot.drive_time(30, 0, 500)
            #while obstacle_sensor.distance() > 100:
            #    robot.drive(-100, 0)
            #    brick.sound.beep(500, 1000, 200)
            #    brick.sound.beep(500, 800, 0)    
            # Wait until an obstacle is detected. This is done by repeatedly
            # while the measured distance is still greater than 200 mm.
            brick.sound.beep()    
            brick.light(Color.GREEN)
            robot.stop()
            # Taskuparkki loppu
        if code == 304:
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
            brick.light(Color.RED)
            brick.sound.file(SoundFile.OKEY_DOKEY)
            brick.display.clear()
            brick.display.image('/home/robot/robomest/pics/logo1.bmp')
            if brick.battery.voltage() < 7000:
                brick.light(Color.RED)
                #brick.display.image(ImageFile.bar4)
            if brick.battery.voltage() < 7500:
                brick.light(Color.ORANGE)
                #brick.display.image(ImageFile.bar2)
            if brick.battery.voltage() > 7500:
                brick.light(Color.GREEN)
                #brick.display.image(ImageFile.bar0)
            # Show the current voltage
            brick.display.text("Voltage is: {}".format(brick.battery.voltage()), (10,120))
            wait(5000)
            brick.light(Color.GREEN)
            brick.display.image('/home/robot/robomest/pics/logo3.bmp')
            brick.display.text("PS button to EXIT", (25,110))
        if code == 308:
            brick.light(Color.RED)
            brick.display.image('/home/robot/robomest/pics/logo2.bmp')
            brick.sound.beep(1000, 200, 50)
            brick.display.image('/home/robot/robomest/pics/logo1.bmp')
            brick.sound.beep(1000, 200, 50)
            brick.display.image('/home/robot/robomest/pics/logo2.bmp')
            brick.sound.beep(1000, 200, 50)
            brick.display.image('/home/robot/robomest/pics/logo1.bmp')
            brick.sound.beep(1000, 200, 50)
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
        if code == 3: 
            left = scale(value, (0,255), (45, -45))
            brick.light(Color.RED)
        if code == 1: # Righ stick vertical
            forward = scale(value, (0,255), (100,-100))
            brick.light(Color.RED)
        if code == 2:
            forward = 0
            brick.light(Color.GREEN)
            brick.display.image('/home/robot/robomest/pics/logo3.bmp')
            brick.display.text("PS button to EXIT", (25,110))
        if code == 5:
            forward = 0
            brick.light(Color.GREEN)
            brick.display.image('/home/robot/robomest/pics/logo3.bmp')
            brick.display.text("PS button to EXIT", (25,110))
    # Set motor voltages. 
    left_motor.dc(forward)
    right_motor.dc(forward)

    # Track the steering angle
    steer_motor.track_target(left)

    # Finally, read another event
    event = in_file.read(EVENT_SIZE)

in_file.close()

# PS4 control code ends

# Clear screen, print instructions
brick.display.clear()
brick.display.image('/home/robot/robomest/pics/logo3.bmp')
brick.display.text("Press any button to exit", (5,115))

# Wait until a button is pressed
while not brick.buttons():
    wait(10)
    
brick.sound.file(SoundFile.THANK_YOU)
brick.sound.file(SoundFile.GOODBYE)