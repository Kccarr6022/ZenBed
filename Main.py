from motorclass import Motor
from zenbedclass import ZenBed


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
    Pattern -> variable_name = "Capital letter first (X coordinate) -> number (Y coordinate) -> comma (Seperates the elements grouped)" 
    
    Put variable_name in Zenbed.pattern(variable_name)
    
    Zenbed.pattern_wave_length = 3
    Zenbed.pattern_time = 10 # Time in seconds of patterns
    Zenbed.pattern_percent_power = 100
    Zenbed.pattern_percent_power = self.pattern_percent_power / 100
    Zenbed.pattern_start_power = 20 * self.pattern_percent_power # Where the first motor in the wave starts by
    Zenbed.pattern_max_power = 50 * self.pattern_percent_power # Where the power in the wave is highest
    Zenbed.pattern_rate_of_change =  1 * self.pattern_percent_power # The option to change the rate of power increments
    
    for x in range(A,L + 1): 
        for y in range(1,19):
            Zenbed.mtr[x][y].percent(20) #Set all motors to power level
    """



def pattern(bed, pattern):
    bed.sequence_to_pattern(bed.string_to_seq(pattern))

rectangle = "D4 E4, D5 E5, D6 E6, D7 E7, D8 E8, D9 E9, D10 E10, D11 E11, D12 E12, D13 E13, D14 E14, D15 E15, D16 D17 E16 E17, F16 F17, G16 G17, H16 H17 I16 I17, H15 I15, H14 I14, H13 I13, H12 I12, H11 I11, H10 I10, H9 I9, H8 I8, H7 I7, H6 I6, H5 I5, H4 I4, H3 I3 H2 I2, G2 G3, F2 F3, D2 E2 Dsd3 E3"

randodiagnal = "A1, B2, C3, D4, E5, F6, G7 H7, G8 H8, G9 H9, G10 H10, G11 G12 H11 H12, F11 F12, E11 E12, D11 D12, C11 C12, B11 B12, A11 A12, A10, A9, A8, A7, A6, A5, A4, A3, A2, A1"

def main():
    Zenbed = ZenBed()
    #rectangle_array = Zenbed.string_to_seq(Zenbed.string_rectangle)
    Zenbed.pattern_rate_of_change = 15
    Zenbed.pattern_max_power = 40
    Zenbed.pattern_start_power = 10
    #Zenbed.sequence_to_pattern(Zenbed.rectangle)
    #pattern(Zenbed, Zenbed.string_rectangle)
    #Zenbed.all_motors_increase()
    #Zenbed.pattern(rectangle)
    #Zenbed.mtr[B][18].percent(30) #Set the power level of a single motor
    #Zenbed.on(20) #Also sets all motors to power level
    Zenbed.status()
    time.sleep(10)
    Zenbed.off()
    
    
main()