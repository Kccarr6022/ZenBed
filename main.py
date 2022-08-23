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


# Zenbed Initialization
zenbed = Zenbed()


# """ COMMANDS =============================================================
#
#     Set power level of all motors
#         zenbed.on()
#     
#     Set power level of specific motor
#         zenbed.mtr[X][Y].percent()
#
#     Set power level of specific group of motors (This has to be edited in zenbedclass.py)
#         zenbed.testmtrs()
#
#     Turn all motors off
#         zenbed.off()
#
#     Select pattern
#        zenbed.pattern()
    
# #     Zenbed.pattern_time = 10 # Time in seconds of patterns
# #     Zenbed.pattern_percent_power # Percent power for patterns
# #     Zenbed.pattern_start_power # Where the first motor in the wave starts by
# #     Zenbed.pattern_max_power = # Where the power in the wave is highest
# #     Zenbed.pattern_rate_of_change # The option to change the rate of power increments
    
#     """ ===================================================================

"""
Patterns
==========
rectangle
expanding_circle
goacross
flow
"""

def main():
    #zenbed.mtr[A][17].percent(20)
    #zenbed.pattern(expanding_circle) # Forever loop comment out to turn off Motors
    zenbed.status()
    zenbed.off()
    return 0

if __name__ == "__main__":
    main()
