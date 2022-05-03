from motorclass import Motor
import sys
import time

"""
The following class is to contain an array of motors from the motor class as well as patterns for the vibration motors
to follow. Different patterns can be defined from this class to control the bed. Additionally, the bed can have seperate
attributes such as height and width or motorsx and motorsy. The height of motorsx and motorsy will determine the grid.
"""


class ZenBed:
    def __init__(self): #

        # Initializing a a double array of motors
        self.motorsx = 4  # amount of columns
        self.motorsy = 6  # amount of rows
        self.motorgird = []

        # Creates grid of motors
        for i in range(motorsx):
            self.motory = []
            for j in range(motorsy):
                self.motory.append(motor(i, j))
            self.motorgrid.append(motory)

    def CircleLoop():  # Current 1d array loop <- Functional
    
        motor = []
    
        for i in range(10):
            motor.append(Motor(i, 0))
            motor[i].motoron()
            time.sleep(2)
            motor[i].motoroff()

            

