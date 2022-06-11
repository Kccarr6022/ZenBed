from motorclass import Motor
from zenbedclass import ZenBed
from PCA import PCA9685
import sys
import time
import busio
from board import SCL, SDA

# Letters
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


# MotorGrid Size
MOTORGRIDXSIZE = 12
MOTORGRIDYSIZE = 18


def main():
    
    """zenbed = ZenBed() # Creates ZenBed object
    zenbed.CircleLoop() # Uses object function "CircleLoop"
    """
    
    # Object create
    i2c_bus = busio.I2C(SCL, SDA)
    
    #def __init__( self, i2c_bus: I2C, *, address: int = 0x40, reference_clock_speed: int = 25000000
    PCA = PCA9685(i2c_bus, 0x41)
    print(str(SCL))
    print(str(SDA))
    print(str(i2c_bus))
    PCA.frequency = 60
    PCA.channels[0].duty_cycle = 0    
    



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