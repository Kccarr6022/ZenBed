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

# MotorGrid Size
MOTORGRIDXSIZE = 10
MOTORGRIDYSIZE = 10


def init(): #
    
    # Creates MotorGrid
    # MotorGrid = [[Motor(x,y) for x in range(MotorGridXSize)] for y in
                 # range(MotorGridYSize)]
    
    # Instantiates Motors to MotorGrid
    # MotorGrid[0][0] = Motor(0,0)


# Used for testing
def main():

    # Instantiates MotorBoard
    self.i2c_bus = busio.I2C(SCL, SDA)
    self.MotorBoard = PCA9685(i2c_bus)
    self.MotorBoard.frequency = 60
    
    motor0 = Motor(3,0)
    Motor0.MotorOn()
    MotorBoard.channels[0].duty_cycle = 0xfffe
    time.sleep(20)
    Motor0.MotorOff()
    
    # MotorGrid[0][0].on()# Full power for motor


if __name__ == '__main__':

    init()
    main()
