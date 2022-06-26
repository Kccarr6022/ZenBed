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
    
    Zenbed.pattern_wave_length = 3
    Zenbed.pattern_time = 10 # Time in seconds of patterns
    Zenbed.pattern_percent_power = 100
    Zenbed.pattern_percent_power = self.pattern_percent_power / 100
    Zenbed.pattern_start_power = 20 * self.pattern_percent_power # Where the first motor in the wave starts by
    Zenbed.pattern_max_power = 50 * self.pattern_percent_power # Where the power in the wave is highest
    Zenbed.pattern_rate_of_change =  1 * self.pattern_percent_power # The option to change the rate of power increments
"""


Rectangle = "A1 A2 A3 A4 A5 A6 A7 A8 A9 A9, B1"

def pattern(bed, pattern):
    bed.sequence_to_pattern(bed.string_to_seq(pattern))

def main():
    Zenbed = ZenBed()
    #rectangle_array = Zenbed.string_to_seq(Zenbed.string_rectangle)
    Zenbed.pattern_rate_of_change = 5
    #Zenbed.status()
    #Zenbed.sequence_to_pattern(Zenbed.rectangle)
    #pattern(Zenbed, Zenbed.string_rectangle)
    pattern(Zenbed, input("Enter in a pattern: "))
    Zenbed.off()
    
    
main()