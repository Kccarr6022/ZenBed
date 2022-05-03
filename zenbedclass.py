from motorclass import Motor
import sys
import time

class ZenBed:
    def __init__(self): # Initializing all the PCAs / Motors are connected to PCAs
        
        
        # Initializing a a double array of motors
        self.rows = []
        self.columns = []
        
        self.grid
        
        
        # Algorithms 
        
    def CircleLoop(): # Current 1d array loop <- Functional
    
        motor = []
    
        for i in range(10):
            motor.append(Motor(i, 0))
            motor[i].motoron()
            time.sleep(2)
            motor[i].motoroff()

            

