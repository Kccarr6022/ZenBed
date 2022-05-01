from adafruit_pca9685 import PCA9685
from zenbedclass import ZenBed
from board import SCL, SDA
import busio


"""
    The motor class is intended to have attributes and functions for each motor in the ZenBed. These motors
    are intended to be placed in a double array inside the ZenBed class to be easily callable down the line.
"""


class Motor(ZenBed):
    def __init__(self, motorx, motory):
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
        self.MotorBoard = PCA9685(i2c_bus)
        self.MotorBoard.frequency = 60
        
        pass

    # Turns on motor
    def motoron(self): # Error
        if 0 < self.MotorLocationX < 10: # Checks what PCI to call from
            if 0 < self.MotorLocationY < 10: # For later in project
                self.MotorBoard.channels[self.MotorLocationX].duty_cycle = 0xfffe

        pass 

    # Turns motor to 50%

    def motorhalfon(self):  # Error
        if 0 < self.MotorLocationX < 10:  # Checks what PCI to call from
            if 0 < self.MotorLocationY < 10:  # For later in project
                self.MotorBoard.channels[self.MotorLocationX].duty_cycle = 0x7fff

        pass

    # Turns motor to 0
    def motoroff(self):  # Error
        if 0 < self.MotorLocationX < 10:  # Checks what PCI to call from
            if 0 < self.MotorLocationY < 10:  # For later in project
                self.MotorBoard.channels[self.MotorLocationX].duty_cycle = 0

        pass

    # Gives vibration motor percent power
    def motoroff(self, percentpower):
        if percentpower > 1:  # safety lock
            percentpower = 1
        if 0 < self.MotorLocationX < 10:  # Checks what PCI to call from
            if 0 < self.MotorLocationY < 10:  # For later in project
                self.MotorBoard.channels[self.MotorLocationX].duty_cycle = 0xfffe * percentpower

        pass
