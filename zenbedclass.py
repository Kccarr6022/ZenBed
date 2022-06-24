# -*- coding: utf-8 -*-
from motorclass import Motor
import time

# Grid size

MOTORGRIDXSIZE = 12
MOTORGRIDYSIZE = 18

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


class ZenBed:

    def __init__(self):  # Initializing all the PCAs / Motors are connected to PCAs
        # Initializing a a double list of motors
        self.mtr = []
        for x in range(0, MOTORGRIDXSIZE + 1):
            self.mtr.append([])
            for y in range(0, MOTORGRIDYSIZE + 1):
                self.mtr[x].append(Motor(x, y))
        
        # Pattern variables
        self.pattern_wave_length = 3
        self.pattern_time = 10 # Time in seconds of patterns
        self.pattern_start_power = 10 # Where the first motor in the wave starts by
        self.pattern_max_power = 50 # Where the power in the wave is highest
        self.pattern_rate_of_change =  int(((self.pattern_max_power - self.pattern_start_power) * 2) / (self.pattern_wave_length - 1))# The option to change the rate of power increments
        

        

    # Sequences
    
    
        
        # Algorithms

    def linearpattern(self, sequence):  # Takes double list of motors and converts to pattern.
        """
        Takes a pattern sequence and translates this into a functional pattern in zenbed.
        """
        if (len(sequence) < self.pattern_wave_length):
            print("Pattern wave length is greater than sequence")
            return
        while True:
            for x in range(0, len(sequence), 1):
                for current in range(0, self.pattern_wave_length, 1):
                    if (sequence[x+current].x <= MOTORGRIDXSIZE or sequence[x+current].y <= MOTORGRIDYSIZE):
                        if (current <= (self.pattern_wave_length/2 + 1)):
                            sequence[x+current].percent(self.pattern_start_power + self.pattern_rate_of_change * current)
                        else:
                            sequence[x+current].percent(self.pattern_start_power - self.pattern_rate_of_change * (current - (self.pattern_wave_length/2 + 1)))
                        self.status()

                    else:
                        return
                if (sequence[x-1] != None):
                    sequence[x-1].percent(0) # Turns off previous motor
                time.sleep(1/(len(sequence)) * self.pattern_time) # Pattern time will be pattern_time seconds
                    
    def status(self):
        """
        Outputs current power levels of motors in grid
        """
        for x in range(A, L+1):
            for y in range(0, 19):
                print((str(self.mtr[x][y].motor_power)), end ='')
            print()
        print()
            
    def returnrow(self, y):
        returned = []
        for x in range(A, L):
            returned.append(self.mtr[x][y])
        return returned
        
    def returncolumn(self, x):
        returned = []
        for y in range(1, 19):
            returned.append(self.mtr[x][y])
        return returned
        
        
    def row(self, y, percent):
        for x in range(A, L):
            self.mtr[x][y].percent(percent)
        
    def column(self, x, percent):
        for y in range(1, 19):
            self.mtr[x][y].percent(percent)
            
    def on(self):
        for y in range (1, 19):
            for x in range (A, L+1):
                self.mtr[x][y].percent(15)        
    
    def on(self, percent):
        for y in range (1, 19):
            for x in range (A, L+1):
                self.mtr[x][y].percent(percent)
    
    def off(self):
        for y in range (1, 19):
            for x in range (A, L+1):
                self.mtr[x][y].percent(0)      
