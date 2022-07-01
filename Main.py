# Sets directory to project directory
from directory_path import ROOT_DIR
import os
os.chdir(ROOT_DIR)

from classes.zenbedclass import Zenbed
from imported.patterns import expanding_circle, rectangle
import sqlite3
import time


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

# database connection
connection = sqlite3.connect('zenbed-database.db')

c = connection.cursor()

# c.execute("""CREATE TABLE patterns (
#             name text,
#             time integer,
#             rate_of_change integer,
#             max_power integer,
#             start_power integer,
#             percent_power integer,
#             sequence text
#             )""")

#c.execute("INSERT INTO patterns VALUES ('rectangle', 0.1, 100, 20, 50, 1, 'D4 E4, D5 E5, D6 E6, D7 E7, D8 E8, D9 E9, D10 E10, D11 E11, D12 E12, D13 E13, D14 E14, D15 E15, D16 D17 E16 E17, F16 F17, G16 G17, H16 H17 I16 I17, H15 I15, H14 I14, H13 I13, H12 I12, H11 I11, H10 I10, H9 I9, H8 I8, H7 I7, H6 I6, H5 I5, H4 I4, H3 I3 H2 I2, G2 G3, F2 F3, D2 E2 D3 E3')")


connection.commit()

connection.close()




# time.sleep(4)

# """
#     Motor on -> Zenbed.mtr[letter][number].percent(percent power)
    
#     Put patterns in Zenbed.pattern(pattern)
    
#     Zenbed.pattern_time = 10 # Time in seconds of patterns
#     Zenbed.pattern_percent_power # Percent power for patterns
#     Zenbed.pattern_start_power # Where the first motor in the wave starts by
#     Zenbed.pattern_max_power = # Where the power in the wave is highest
#     Zenbed.pattern_rate_of_change # The option to change the rate of power increments
    
#     """



# def main():
#     zenbed = ZenBed()
#     zenbed.pattern(rectangle)
#     zenbed.status()
#     zenbed.off()
#     return 0


# main()
