from PCA import PCA9685
from board import SCL, SDA
import busio

# I2C
i2c_bus = busio.I2C(SCL, SDA)

# MotorGrid Size
MOTORGRIDXSIZE = 12
MOTORGRIDYSIZE = 18

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
    def __init__(self, motorX, motorY): # Motor(x, y) Creating ZenBed Matrix
        
        self.MotorLocationXmax = 12
        self.MotorLocationYmax = 18
        self.channel = 0 # default value is first channel

        """
            During later implementation include if statements using conditions motorX and motorY to determine which
            self.PCA board to instantiate to declare variable "MotorBoard".
        """
    
        # Instantiates PCA address and channel based on coordinates O(n^2) startup
        # Gives channel number at startup time allowing O(1) time complexity at run
        
        
        # Algorithm to detect where motor is in array
        """
        for X in range(A, MOTORGRIDXSIZE):
            for Y in range(1, MOTORYSIZE):
                
                if(F < X and 9 < Y): 
                    X = A
                    Y += 1
                X += 1
                self.channel 
       
        
        
        
            
            # Motor 1 - 16 Matches
            
            # Algorithm to channel to use
            for count in range(0, 15):
                X = 0 # one below initial range
                Y = 1
                if(F < X):
                    X = A
                    Y += 1
                X += 1
       """
        
        # PCA0
        if ( A <= motorX <= F and 1 <= motorY <= 2 or
            motorY == 3 and A <= motorY <= D):
            self.PCA = PCA9685(i2c_bus, 0x40)
            
            if (motorX == A and motorY == 1):
                self.channel = 0
            if (motorX == B and motorY == 1):
                self.channel = 1
            if (motorX == C and motorY == 1):
                self.channel = 2
            if (motorX == D and motorY == 1):
                self.channel = 3
            if (motorX == E and motorY == 1):
                self.channel = 4
            if (motorX == F and motorY == 1):
                self.channel = 5
            if (motorX == A and motorY == 2):
                self.channel = 6
            if (motorX == B and motorY == 2):
                self.channel = 7
            if (motorX == C and motorY == 2):
                self.channel = 8
            if (motorX == D and motorY == 2):
                self.channel = 9
            if (motorX == E and motorY == 2):
                self.channel = 10
            if (motorX == F and motorY == 2):
                self.channel = 11
            if (motorX == A and motorY == 3):
                self.channel = 12
            if (motorX == B and motorY == 3):
                self.channel = 13
            if (motorX == C and motorY == 3):
                self.channel = 14
            if (motorX == D and motorY == 3):
                self.channel = 15
                
        
        # PCA1
        elif (A <= motorX <= F and 4 <= motorY <= 5 or
            motorY == 3 and E <= motorY <= F or
            A <= motorX <= B and motorY == 6):
            self.PCA = PCA9685(i2c_bus, 0x41)
            
            if (motorX == E and motorY == 3):
                self.channel = 0
            if (motorX == F and motorY == 3):
                self.channel = 1
            if (motorX == A and motorY == 4):
                self.channel = 2
            if (motorX == B and motorY == 4):
                self.channel = 3
            if (motorX == C and motorY == 4):
                self.channel = 4
            if (motorX == D and motorY == 4):
                self.channel = 5
            if (motorX == E and motorY == 4):
                self.channel = 6
            if (motorX == F and motorY == 4):
                self.channel = 7
            if (motorX == A and motorY == 5):
                self.channel = 8
            if (motorX == B and motorY == 5):
                self.channel = 9
            if (motorX == C and motorY == 5):
                self.channel = 10
            if (motorX == D and motorY == 5):
                self.channel = 11
            if (motorX == E and motorY == 5):
                self.channel = 12
            if (motorX == F and motorY == 5):
                self.channel = 13
            if (motorX == A and motorY == 6):
                self.channel = 14
            if (motorX == B and motorY == 6):
                self.channel = 15
        
        # PCA2
        elif (C <= motorX <= F and motorY == 6 or
            7 <= motorY <= 8 and A <= motorY <= F):
            self.PCA = PCA9685(i2c_bus, 0x42)
            
            if (motorX == C and motorY == 6):
                self.channel = 0
            if (motorX == D and motorY == 6):
                self.channel = 1
            if (motorX == E and motorY == 6):
                self.channel = 2
            if (motorX == F and motorY == 6):
                self.channel = 3
            if (motorX == A and motorY == 7):
                self.channel = 4
            if (motorX == B and motorY == 7):
                self.channel = 5
            if (motorX == C and motorY == 7):
                self.channel = 6
            if (motorX == D and motorY == 7):
                self.channel = 7
            if (motorX == E and motorY == 7):
                self.channel = 8
            if (motorX == F and motorY == 7):
                self.channel = 9
            if (motorX == A and motorY == 8):
                self.channel = 10
            if (motorX == B and motorY == 8):
                self.channel = 11
            if (motorX == C and motorY == 8):
                self.channel = 12
            if (motorX == D and motorY == 8):
                self.channel = 13
            if (motorX == E and motorY == 8):
                self.channel = 14
            if (motorX == F and motorY == 8):
                self.channel = 15
            
        # PCA3
        elif (A <= motorX <= F and motorY == 9):
            self.PCA = PCA9685(i2c_bus, 0x43)
            
            if (motorX == A and motorY == 9):
                self.channel = 0
            if (motorX == B and motorY == 9):
                self.channel = 1
            if (motorX == C and motorY == 9):
                self.channel = 2
            if (motorX == D and motorY == 9):
                self.channel = 3
            if (motorX == E and motorY == 9):
                self.channel = 4
            if (motorX == F and motorY == 9):
                self.channel = 5
            
        
        # PCA4
        elif (A <= motorX <= F and 10 <= motorY <= 11 or
              motorY == 12 and A <= motorY <= D):
            self.PCA = PCA9685(i2c_bus, 0x44)
            
            if (motorX == A and motorY == 10):
                self.channel = 0
            if (motorX == B and motorY == 10):
                self.channel = 1
            if (motorX == C and motorY == 10):
                self.channel = 2
            if (motorX == D and motorY == 10):
                self.channel = 3
            if (motorX == E and motorY == 10):
                self.channel = 4
            if (motorX == F and motorY == 10):
                self.channel = 5
            if (motorX == A and motorY == 11):
                self.channel = 6
            if (motorX == B and motorY == 11):
                self.channel = 7
            if (motorX == C and motorY == 11):
                self.channel = 8
            if (motorX == D and motorY == 11):
                self.channel = 9
            if (motorX == E and motorY == 11):
                self.channel = 10
            if (motorX == F and motorY == 11):
                self.channel = 11
            if (motorX == A and motorY == 12):
                self.channel = 12
            if (motorX == B and motorY == 12):
                self.channel = 13
            if (motorX == C and motorY == 12):
                self.channel = 14
            if (motorX == D and motorY == 12):
                self.channel = 15
            
        # PCA5
        elif (A <= motorX <= F and 13 <= motorY <= 14 or
            motorY == 12 and E <= motorY <= F or
            A <= motorX <= B and motorY == 15):
            self.PCA = PCA9685(i2c_bus, 0x45)
            
            if (motorX == E and motorY == 12):
                self.channel = 0
            if (motorX == F and motorY == 12):
                self.channel = 1
            if (motorX == A and motorY == 13):
                self.channel = 2
            if (motorX == B and motorY == 13):
                self.channel = 3
            if (motorX == C and motorY == 13):
                self.channel = 4
            if (motorX == D and motorY == 13):
                self.channel = 5
            if (motorX == E and motorY == 13):
                self.channel = 6
            if (motorX == F and motorY == 13):
                self.channel = 7
            if (motorX == A and motorY == 14):
                self.channel = 8
            if (motorX == B and motorY == 14):
                self.channel = 9
            if (motorX == C and motorY == 14):
                self.channel = 10
            if (motorX == D and motorY == 14):
                self.channel = 11
            if (motorX == E and motorY == 14):
                self.channel = 12
            if (motorX == F and motorY == 14):
                self.channel = 13
            if (motorX == A and motorY == 15):
                self.channel = 14
            if (motorX == B and motorY == 15):
                self.channel = 15
            
        # PCA6
        elif (C <= motorX <= F and motorY == 15 or
             A <= motorX <= F and 16 <= motorY <= 17):
            self.PCA = PCA9685(i2c_bus, 0x46)
            
            if (motorX == C and motorY == 15):
                self.channel = 0
            if (motorX == D and motorY == 15):
                self.channel = 1
            if (motorX == E and motorY == 15):
                self.channel = 2
            if (motorX == F and motorY == 15):
                self.channel = 3
            if (motorX == A and motorY == 16):
                self.channel = 4
            if (motorX == B and motorY == 16):
                self.channel = 5
            if (motorX == C and motorY == 16):
                self.channel = 6
            if (motorX == D and motorY == 16):
                self.channel = 7
            if (motorX == E and motorY == 16):
                self.channel = 8
            if (motorX == F and motorY == 16):
                self.channel = 9
            if (motorX == A and motorY == 17):
                self.channel = 10
            if (motorX == B and motorY == 17):
                self.channel = 11
            if (motorX == C and motorY == 17):
                self.channel = 12
            if (motorX == D and motorY == 17):
                self.channel = 13
            if (motorX == E and motorY == 17):
                self.channel = 14
            if (motorX == F and motorY == 17):
                self.channel = 15
            
        # PCA7
        elif (A <= motorX <= F and motorY == 18):
            self.PCA = PCA9685(i2c_bus, 0x47)
            
            if (motorX == A and motorY == 18):
                self.channel = 0
            if (motorX == B and motorY == 18):
                self.channel = 1
            if (motorX == C and motorY == 18):
                self.channel = 2
            if (motorX == D and motorY == 18):
                self.channel = 3
            if (motorX == E and motorY == 18):
                self.channel = 4
            if (motorX == F and motorY == 18):
                self.channel = 5
            
        # PCA8
        elif (G <= motorX <= L and 1 <= motorY <= 2
              or motorY == 3 and G <= motorY <= J):
            self.PCA = PCA9685(i2c_bus, 0x48)
            
            if (motorX == G and motorY == 1):
                self.channel = 0
            if (motorX == H and motorY == 1):
                self.channel = 1
            if (motorX == I and motorY == 1):
                self.channel = 2
            if (motorX == J and motorY == 1):
                self.channel = 3
            if (motorX == K and motorY == 1):
                self.channel = 4
            if (motorX == L and motorY == 1):
                self.channel = 5
            if (motorX == G and motorY == 2):
                self.channel = 6
            if (motorX == H and motorY == 2):
                self.channel = 7
            if (motorX == I and motorY == 2):
                self.channel = 8
            if (motorX == J and motorY == 2):
                self.channel = 9
            if (motorX == K and motorY == 2):
                self.channel = 10
            if (motorX == L and motorY == 2):
                self.channel = 11
            if (motorX == G and motorY == 3):
                self.channel = 12
            if (motorX == H and motorY == 3):
                self.channel = 13
            if (motorX == I and motorY == 3):
                self.channel = 14
            if (motorX == J and motorY == 3):
                self.channel = 15
            
        # PCA9    
        elif (G <= motorX <= L and 4 <= motorY <= 5 or
            motorY == 3 and K <= motorY <= L or
            G <= motorX <= H and motorY == 6):
            self.PCA = PCA9685(i2c_bus, 0x49)
            
            if (motorX == K and motorY == 3):
                self.channel = 0
            if (motorX == L and motorY == 3):
                self.channel = 1
            if (motorX == G and motorY == 4):
                self.channel = 2
            if (motorX == H and motorY == 4):
                self.channel = 3
            if (motorX == I and motorY == 4):
                self.channel = 4
            if (motorX == J and motorY == 4):
                self.channel = 5
            if (motorX == K and motorY == 4):
                self.channel = 6
            if (motorX == L and motorY == 4):
                self.channel = 7
            if (motorX == G and motorY == 5):
                self.channel = 8
            if (motorX == H and motorY == 5):
                self.channel = 9
            if (motorX == I and motorY == 5):
                self.channel = 10
            if (motorX == J and motorY == 5):
                self.channel = 11
            if (motorX == K and motorY == 5):
                self.channel = 12
            if (motorX == L and motorY == 5):
                self.channel = 13
            if (motorX == G and motorY == 6):
                self.channel = 14
            if (motorX == H and motorY == 6):
                self.channel = 15
            
        # PCA10
        elif (I <= motorX <= L and motorY == 6 or
            7 <= motorY <= 8 and G <= motorY <= L):
            self.PCA = PCA9685(i2c_bus, 0x4a)
            
            if (motorX == I and motorY == 6):
                self.channel = 0
            if (motorX == J and motorY == 6):
                self.channel = 1
            if (motorX == K and motorY == 6):
                self.channel = 2
            if (motorX == L and motorY == 6):
                self.channel = 3
            if (motorX == G and motorY == 7):
                self.channel = 4
            if (motorX == H and motorY == 7):
                self.channel = 5
            if (motorX == I and motorY == 7):
                self.channel = 6
            if (motorX == J and motorY == 7):
                self.channel = 7
            if (motorX == K and motorY == 7):
                self.channel = 8
            if (motorX == L and motorY == 7):
                self.channel = 9
            if (motorX == G and motorY == 8):
                self.channel = 10
            if (motorX == H and motorY == 8):
                self.channel = 11
            if (motorX == I and motorY == 8):
                self.channel = 12
            if (motorX == J and motorY == 8):
                self.channel = 13
            if (motorX == K and motorY == 8):
                self.channel = 14
            if (motorX == L and motorY == 8):
                self.channel = 15
            
        # PCA11
        elif (G <= motorX <= L and motorY == 9):
            self.PCA = PCA9685(i2c_bus, 0x4b)
            
            if (motorX == G and motorY == 9):
                self.channel = 0
            if (motorX == H and motorY == 9):
                self.channel = 1
            if (motorX == I and motorY == 9):
                self.channel = 2
            if (motorX == J and motorY == 9):
                self.channel = 3
            if (motorX == K and motorY == 9):
                self.channel = 4
            if (motorX == L and motorY == 9):
                self.channel = 5
            
        # PCA12
        elif (G <= motorX <= L and 10 <= motorY <= 11 or
              motorY == 12 and G <= motorY <= J):
            self.PCA = PCA9685(i2c_bus, 0x4c)
            
            if (motorX == G and motorY == 10):
                self.channel = 0
            if (motorX == H and motorY == 10):
                self.channel = 1
            if (motorX == I and motorY == 10):
                self.channel = 2
            if (motorX == J and motorY == 10):
                self.channel = 3
            if (motorX == K and motorY == 10):
                self.channel = 4
            if (motorX == L and motorY == 10):
                self.channel = 5
            if (motorX == G and motorY == 11):
                self.channel = 6
            if (motorX == H and motorY == 11):
                self.channel = 7
            if (motorX == I and motorY == 11):
                self.channel = 8
            if (motorX == J and motorY == 11):
                self.channel = 9
            if (motorX == K and motorY == 11):
                self.channel = 10
            if (motorX == L and motorY == 11):
                self.channel = 11
            if (motorX == G and motorY == 12):
                self.channel = 12
            if (motorX == H and motorY == 12):
                self.channel = 13
            if (motorX == I and motorY == 12):
                self.channel = 14
            if (motorX == J and motorY == 12):
                self.channel = 15
            
        # PCA13
        elif (G <= motorX <= L and 13 <= motorY <= 14 or
            motorY == 12 and K <= motorY <= L or
            G <= motorX <= H and motorY == 15):
            self.PCA = PCA9685(i2c_bus, 0x4d)
            
            if (motorX == K and motorY == 12):
                self.channel = 0
            if (motorX == L and motorY == 12):
                self.channel = 1
            if (motorX == G and motorY == 13):
                self.channel = 2
            if (motorX == H and motorY == 13):
                self.channel = 3
            if (motorX == I and motorY == 13):
                self.channel = 4
            if (motorX == J and motorY == 13):
                self.channel = 5
            if (motorX == K and motorY == 13):
                self.channel = 6
            if (motorX == L and motorY == 13):
                self.channel = 7
            if (motorX == G and motorY == 14):
                self.channel = 8
            if (motorX == H and motorY == 14):
                self.channel = 9
            if (motorX == I and motorY == 14):
                self.channel = 10
            if (motorX == J and motorY == 14):
                self.channel = 11
            if (motorX == K and motorY == 14):
                self.channel = 12
            if (motorX == L and motorY == 14):
                self.channel = 13
            if (motorX == G and motorY == 15):
                self.channel = 14
            if (motorX == H and motorY == 15):
                self.channel = 15
            
        # PCA14
        elif (I <= motorX <= L and motorY == 15 or
            16 <= motorY <= 17 and G <= motorY <= L):
            self.PCA = PCA9685(i2c_bus, 0x4e)
            
            if (motorX == I and motorY == 15):
                self.channel = 0
            if (motorX == J and motorY == 15):
                self.channel = 1
            if (motorX == K and motorY == 15):
                self.channel = 2
            if (motorX == L and motorY == 15):
                self.channel = 3
            if (motorX == G and motorY == 16):
                self.channel = 4
            if (motorX == H and motorY == 16):
                self.channel = 5
            if (motorX == I and motorY == 16):
                self.channel = 6
            if (motorX == J and motorY == 16):
                self.channel = 7
            if (motorX == K and motorY == 16):
                self.channel = 8
            if (motorX == L and motorY == 16):
                self.channel = 9
            if (motorX == G and motorY == 17):
                self.channel = 10
            if (motorX == H and motorY == 17):
                self.channel = 11
            if (motorX == I and motorY == 17):
                self.channel = 12
            if (motorX == J and motorY == 17):
                self.channel = 13
            if (motorX == K and motorY == 17):
                self.channel = 14
            if (motorX == L and motorY == 17):
                self.channel = 15
        
        # PCA15
        elif (G <= motorX <= L and motorY == 18):
            self.PCA = PCA9685(i2c_bus, 0x4f)
            
            if (motorX == G and motorY == 18):
                self.channel = 0
            if (motorX == H and motorY == 18):
                self.channel = 1
            if (motorX == I and motorY == 18):
                self.channel = 2
            if (motorX == J and motorY == 18):
                self.channel = 3
            if (motorX == K and motorY == 18):
                self.channel = 4
            if (motorX == L and motorY == 18):
                self.channel = 5
            
        else:
            print("Motor coordinates out of bounds.\n\a")
            quit()
        
        
        self.PCA.frequency = 60
        """
        Old decleration code

        self.i2c_bus = busio.I2C(SCL, SDA)
        self.MotorBoard = self.PCA9685(i2c_bus, self.i2c_bus)
        self.MotorBoard.frequency = 60
        """
        pass
    
    # Turns on all motors connected to the PCA to 20%
    def Testpcas(self, percent):
        for i in range(0, 5):
            self.PCA.channels[i].duty_cycle = (0xfffe * 0.1) # Turns on to 20%

    # Turns on motor
    def motoron(self):
        self.PCA.channels[self.channel].duty_cycle = 0xfffe # Turns on to full

    # Turns motor to 50%
    def motorhalfon(self):
        self.PCA.channels[self.channel].duty_cycle = 0x7FFF # Turns on to half


    # Turns motor to 0
    def motoroff(self):
        self.PCA.channels[self.channel].duty_cycle = 0 # Turns off

    # Gives vibration motor percent power
    def motorpercenton(self, percentpower): # Percent on
        if percentpower > 50:  # safety lock / testing
            percentpower = 50
        self.PCA.channels[self.channel].duty_cycle = int(0xFFFF * percentpower / 100)
