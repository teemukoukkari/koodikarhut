#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import struct

# import rpyc

# Create a RPyC connection to the remote ev3dev device.
# Use the hostname or IP address of the ev3dev device.
# If this fails, verify your IP connectivty via ``ping X.X.X.X``
# conn = rpyc.classic.connect('X.X.X.X')

# import ev3dev2 on the remote ev3dev device
#ev3dev2_motor = conn.modules['ev3dev2.motor']
#ev3dev2_sensor = conn.modules['ev3dev2.sensor']
#ev3dev2_sensor_lego = conn.modules['ev3dev2.sensor.lego']

# Use the LargeMotor and TouchSensor on the remote ev3dev device
#motor2 = ev3dev2_motor.LargeMotor(ev3dev2_motor.OUTPUT_A)
#ts = ev3dev2_sensor_lego.TouchSensor(ev3dev2_sensor.INPUT_1)

# If the TouchSensor is pressed, run the motor
#while True:
#    ts.wait_for_pressed()
#    motor.run_forever(speed_sp=200)
#
#    ts.wait_for_released()
#    motor.stop()


# Start sequence Robomestarit
brick.display.image('/home/robot/robomest/pics/logo3.bmp')
brick.sound.file(SoundFile.OVERPOWER)
brick.display.image('/home/robot/robomest/pics/logo2.bmp')
wait(300)
brick.display.image('/home/robot/robomest/pics/logo3.bmp')
wait(300)
brick.display.image('/home/robot/robomest/pics/logo2.bmp')
wait(300)
brick.display.image('/home/robot/robomest/pics/logo3.bmp')
wait(300)
# Joukkueiden logot
#brick.display.image('/home/robot/robomest/pics/bittipol.bmp')
#brick.sound.file(SoundFile.HORN_1)
#wait(2000)
#brick.display.image('/home/robot/robomest/pics/virtaluu.bmp')
#brick.sound.file(SoundFile.LASER)
#wait(2000)
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

# Kutsutaan racecar ohjelma
# import racecar.py

# Kutsutaan tankki ohjelmaa
# import tank_4motors.py

# Kutsutaan tankkitorni ohjelmaa
import tank_turret.py

# Clear screen, print instructions
brick.display.clear()
brick.display.image('/home/robot/robomest/pics/logo3.bmp')
brick.display.text("Press any button to exit", (5,115))

# Wait until a button is pressed
while not brick.buttons():
    wait(10)
    
brick.sound.file(SoundFile.THANK_YOU)
brick.sound.file(SoundFile.GOODBYE)