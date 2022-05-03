from adafruit_pca9685 import PCA9685
from zenbedclass import ZenBed
from board import SCL, SDA
import busio


"""
    The motor class is intended to have attributes and functions for each motor in the ZenBed. These motors
    are intended to be placed in a double array inside the ZenBed class to be easily callable down the line.
"""


class Motor(ZenBed):
    def __init__(self, motorx, motory): # Motor(x, y)
        self.MotorLocationXmax = 10
        self.MotorLocationYmax = 10
        self.MotorLocationX = motorx  # Location of x value (int)\character value 0=A
        self.MotorLocationY = motory  # Location of y value (int)

        """
            During later implementation include if statements using conditions motorx and motory to determine which
            PCA board to instantiate to declare variable "MotorBoard".
        """

        # Creates Motorboard objects from first PCA.
        self.i2c_bus = busio.I2C(SCL, SDA)
        self.MotorBoard = PCA9685(self.i2c_bus)
        self.MotorBoard.frequency = 60
        
        pass

    # Turns on motor
    def motoron(self): # Error
        self.MotorBoard.channels[self.MotorLocationX].duty_cycle = 0xfffe # Turns on to full

    # Turns motor to 50%

    def motorhalfon(self):  # Error
        self.MotorBoard.channels[self.MotorLocationX].duty_cycle = 0x7fff # Turns to half


    # Turns motor to 0
    def motoroff(self):  # Error
        self.MotorBoard.channels[self.MotorLocationX].duty_cycle = 0 # Turns off

    # Gives vibration motor percent power
    def motorpercenton(self, percentpower): # Percent on
        if percentpower > 1:  # safety lock
            percentpower = 1
        self.MotorBoard.channels[self.MotorLocationX].duty_cycle = 0xfffe * percentpower
