import sys
import time
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
import busio


class ZenBed:
    def __init__(self): # Initializing all the PCAs / Motors are connected to PCAs
        i2c_bus = busio.I2C(SCL, SDA)
        MotorBoard = PCA9685(i2c_bus)
        MotorBoard.frequency = 60
        
        #Initializing a a double array of motors
        
    def Dialog(self):
        print("I am the ZenBed")
