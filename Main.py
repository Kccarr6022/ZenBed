from motorclass import Motor
from zenbedclass import ZenBed
from PCA import PCA9685
import time
import busio
from board import SCL, SDA


# creates i2c object
i2c_bus = busio.I2C(SCL, SDA)

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




         
"""
    Motor on -> Zenbed.mtr[letter][number].percent(percent power)
"""

def main():

    Zenbed = ZenBed()
    #Zenbed.pattern(circle)
    Zenbed.pattern_time = 15
    Zenbed.pattern_rate_of_change = 5
    Zenbed.pattern_power = 50
    #Zenbed.shiftpattern(Zenbed.returnrow(18))
    Zenbed.off()
    
main()
