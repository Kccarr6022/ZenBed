#from zenbedclass import ZenBed
#from motorclass import Motor
from motorclass import Motor
from zenbedclass import ZenBed

import sys
import time
from board import SCL, SDA
import busio
#from adafruit_servokit import ServoKit
from adafruit_pca9685 import PCA9685

def init():
    #Creates Motorboard object
    i2c_bus = busio.I2C(SCL, SDA)
    MotorBoard = PCA9685(i2c_bus)
    MotorBoard.frequency = 60
    pass

def main():
    
    #Initialization
    i2c_bus = busio.I2C(SCL, SDA)
    MotorBoard = PCA9685(i2c_bus)
    MotorBoard.frequency = 60
    
    #Turns on motor 0
    MotorBoard.channels[0].duty_cycle = 0 # Full power for motor
    pass

if __name__ == '__main__':
    init()
    main()
