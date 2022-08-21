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
#     Motor on -> Zenbed.mtr[letter][number].percent(percent power)
    
#     Put patterns in Zenbed.pattern(pattern)
    
#     Zenbed.pattern_time = 10 # Time in seconds of patterns
#     Zenbed.pattern_percent_power # Percent power for patterns
#     Zenbed.pattern_start_power # Where the first motor in the wave starts by
#     Zenbed.pattern_max_power = # Where the power in the wave is highest
#     Zenbed.pattern_rate_of_change # The option to change the rate of power increments
    
#     """ ===================================================================



def main():
    zenbed.pattern(rectangle) # Forever loop comment out to turn off Motors
    zenbed.status()
    zenbed.off()
    return 0

if __name__ == "__main__":
    main()
