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


# Used for testing.
def init():
    # Creates Motorboard objects
    i2c_bus = busio.I2C(SCL, SDA)
    MotorBoard = PCA9685(i2c_bus)
    MotorBoard.frequency = 60
    
    #MotorGrid Size
    MotorGridXSize = 10
    MotorGridYSize = 10
    
    #Creates MotorGrid
    #MotorGrid = [[Motor(x,y) for x in range(MotorGridXSize)] for y in
                 #range(MotorGridYSize)]
    
    #Instantiates Motors to MotorGrid
    #MotorGrid[0][0] = Motor(0,0)

def main():
    
    
    #Turns on motor 0
    
    Motor0 = Motor(3,0)
    Motor0.MotorOn()
    MotorBoard.channels[0].duty_cycle = 0xfffe
    time.sleep(20)
    Motor0.MotorOff()
    
    #MotorGrid[0][0].on()# Full power for motor

if __name__ == '__main__':
    init()
    main()
