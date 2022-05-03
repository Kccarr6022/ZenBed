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



def __init__():
    #Place Initialization code in here
    pass

def main():
    #initialization of board1
    i2c_bus = busio.I2C(SCL, SDA)
    MotorBoard = PCA9685(i2c_bus)
    MotorBoard.frequency = 60
    
             #Motor0 on testing
    MotorBoard.channels[0].duty_cycle = 0xfffe
    time.sleep(20)
    MotorBoard.channels[0].duty_cycle = 0

    pass

if __name__ == '__main__':
    __init__()
    main()
