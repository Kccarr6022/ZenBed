from classes.zenbedclass import Zenbed
from imported.patterns import expanding_circle, rectangle, goacross, flow, strobe, circle, leaf1, leaf2, duelrectangle, infinity, zigzag, scan, scans

import sqlite3
import time
import requests


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
    
# #     Zenbed.pattern_intervals_per_second = 10 # number of intervals per secondz
# #     Zenbed.pattern_percent_power # Percent power for patterns
# #     Zenbed.pattern_start_power # Where the first motor in the wave starts by
# #     Zenbed.pattern_max_power = # Where the power in the wave is highest
# #     Zenbed.pattern_interval_power # The option to change the rate of power increments
    
#     """ ===================================================================

"""
Patterns
==========
rectangle
expanding_circle
goacross
flow
"""

def testeachmotor():
    for x in range(1, 13):
        for y in range(1, 19):
            zenbed.mtr[x][y].percent(30)
            zenbed.status()
            time.sleep(2)
            zenbed.off()
            zenbed.status()
            time.sleep(1)            
            

def main():
    
    zenbed.off()
    zenbed.status()
    return 0

if __name__ == "__main__":
    main()