from motorclass import Motor
from zenbedclass import ZenBed
from enum import Enum
import sys
import time

class Leters(Enum):
    A = 1
    B = 2
    C = 3
    D = 4

Letter = Letters() # Letter.A - > 1

# MotorGrid Size
MOTORGRIDXSIZE = 4
MOTORGRIDYSIZE = 6


def main():
    
    zenbed = ZenBed() # Creates ZenBed object
    zenbed.CircleLoop() # Uses object function "CircleLoop"
    


main()



# Sample algorithm
"""def patternfullon():
    
    motor = []
    power = 100
    
    for i in range(10):
        for i in range(power)
            motor.append(Motor(i, 0))
            motor[i].motorpercenton(power/100)
            time.sleep(2)
        
    for i in range(10):
        motor.append(Motor(i, 0))
        motor[i].motoroff()
        time.sleep(2)
"""