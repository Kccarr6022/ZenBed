from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio

# I2C
i2c_bus = busio.I2C(SCL, SDA)

# Letter variables

A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8
I = 9
J = 10
K = 11
L = 12



"""
    The motor class is intended to have attributes and functions for each motor in the ZenBed. These motors
    are intended to be placed in a double array inside the ZenBed class to be easily callable down the line.
"""


class Motor():
    def __init__(self, motorx, motory): # Motor(x, y) Creating ZenBed Matrix
        
        self.MotorLocationXmax = 12
        self.MotorLocationYmax = 18
        self.MotorLocationX = motorx  # Location of x value (int)\character value 0=A
        self.MotorLocationY = motory  # Location of y value (int)

        """
            During later implementation include if statements using conditions motorx and motory to determine which
            self.PCA board to instantiate to declare variable "MotorBoard".
        """
    
        # Instantiates self.PCA address based on coordinates
        
        # self.PCA0
        if (A <= motorx <= F and 1 <= motory <= 2 or motory == 3 and A <= motory <= D):
            self.PCA = PCA9685(i2c_bus)
        
        # self.PCA1
        elif (A <= motorx <= F and 4 <= motory <= 5 or
            motory == 3 and E <= motory <= F or
            A <= motorx <= B and motory == 6):
            self.PCA = PCA9685(0x41)
        
        # self.PCA2
        elif (C <= motorx <= F and motory == 6 or
            7 <= motory <= 8 and A <= motory <= F):
            self.PCA = PCA9685(0x42)
            
        # self.PCA3
        elif (A <= motorx <= F and motory == 9):
            self.PCA = PCA9685(0x43)
        
        # self.PCA4
        elif (A <= motorx <= F and 10 <= motory <= 11 or motory == 12 and A <= motory <= D):
            self.PCA = PCA9685(0x44)
            
        # self.PCA5
        elif (A <= motorx <= F and 13 <= motory <= 14 or
            motory == 12 and E <= motory <= F or
            A <= motorx <= B and motory == 15):
            self.PCA = PCA9685(0x45)
            
        # self.PCA6
        elif (C <= motorx <= F and motory == 15 or
            16 <= motory <= 17 and A <= motory <= F):
            self.PCA = PCA9685(0x46)
            
        # self.PCA7
        elif (A <= motorx <= F and motory == 18):
            self.PCA = PCA9685(0x47)
            
        # self.PCA8
        elif (G <= motorx <= L and 1 <= motory <= 2 or motory == 3 and G <= motory <= J):
            self.PCA = PCA9685(0x48)
            
        # self.PCA9    
        elif (G <= motorx <= L and 4 <= motory <= 5 or
            motory == 3 and K <= motory <= L or
            G <= motorx <= H and motory == 6):
            self.PCA = PCA9685(0x49)
            
        # self.PCA10
        elif (I <= motorx <= L and motory == 6 or
            7 <= motory <= 8 and G <= motory <= L):
            self.PCA = PCA9685(0x50)
            
        # self.PCA11
        elif (G <= motorx <= L and motory == 9):
            self.PCA = PCA9685(0x51)
            
        # self.PCA12
        elif (G <= motorx <= L and 10 <= motory <= 11 or motory == 12 and G <= motory <= J):
            self.PCA = PCA9685(0x52)
            
        # self.PCA13
        elif (G <= motorx <= L and 13 <= motory <= 14 or
            motory == 12 and K <= motory <= L or
            G <= motorx <= H and motory == 15):
            self.PCA = PCA9685(0x53)
            
        # self.PCA14
        elif (I <= motorx <= L and motory == 15 or
            16 <= motory <= 17 and G <= motory <= L):
            self.PCA = PCA9685(0x54)
        
        # self.PCA15
        elif (G <= motorx <= L and motory == 18):
            self.PCA = PCA9685(0x55)
            
            
        else:
            print("Motor coordinates out of bounds.\n\a")
        
        
        self.PCA.frequency = 60
        """
        Old decleration code

        self.i2c_bus = busio.I2C(SCL, SDA)
        self.MotorBoard = self.PCA9685(self.i2c_bus)
        self.MotorBoard.frequency = 60
        """
        pass

    # Turns on motor
    def motoron(self): # Error
        self.PCA.channels[self.MotorLocationX].duty_cycle = 0xfffe # Turns on to full

    # Turns motor to 50%

    def motorhalfon(self):  # Error
        self.PCA = self.PCA9685(0x40)
 # Turns to half


    # Turns motor to 0
    def motoroff(self):  # Error
        self.PCA.channels[self.MotorLocationX].duty_cycle = 0 # Turns off

    # Gives vibration motor percent power
    def motorpercenton(self, percentpower): # Percent on
        if percentpower > 100:  # safety lock
            percentpower = 100
        self.PCA.channels[0].duty_cycle = 0xfffe * (percentpower / 100)
