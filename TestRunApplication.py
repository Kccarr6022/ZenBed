#from zenbedclass import ZenBed
#from motorclass import Motor
from motorclass import Motor
import zenbedclass

import sys
import time
from board import SCL, SDA
import busio
#from adafruit_servokit import ServoKit
from adafruit_pca9685 import PCA9685



def init():
    #Creates Motorboard objects
    i2c_bus = busio.I2C(SCL, SDA)
    MotorBoard = PCA9685(i2c_bus)
    MotorBoard.frequency = 60
    pass

def main():
    i2c_bus = busio.I2C(SCL, SDA)
    MotorBoard = PCA9685(i2c_bus)
    MotorBoard.frequency = 60
    MotorBoard.channels[3].duty_cycle = 0
    pass

if __name__ == '__main__':
    init()
    main()
