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
        self.pattern_percent_power = 100
        self.pattern_percent_power = self.pattern_percent_power / 100
        self.pattern_start_power = 20 * self.pattern_percent_power # Where the first motor in the wave starts by
        self.pattern_max_power = 50 * self.pattern_percent_power # Where the power in the wave is highest
        self.pattern_rate_of_change =  1 * self.pattern_percent_power # The option to change the rate of power increments
        
        
        self.start = 0
        self.end = 0
        
        def __del__(self):
            self.off()


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
            for current in range(0, len(sequence), 1):
                self.start = time.perf_counter()
                for wave_pos in range(0, self.pattern_wave_length + 1, 1):
                    if (sequence[current+wave_pos].x <= MOTORGRIDXSIZE or sequence[current+wave_pos].y <= MOTORGRIDYSIZE):
                        if (wave_pos <= (self.pattern_wave_length/2 + 1)):
                            sequence[current+wave_pos].percent(self.pattern_start_power + self.pattern_rate_of_change * wave_pos)
                        else:
                            sequence[current+wave_pos].percent(self.pattern_max_power - self.pattern_rate_of_change * (wave_pos - (self.pattern_wave_length/2 + 1)))
                        

                    else:
                        return
                if (sequence[current-1] != None):
                    sequence[current-1].percent(0) # Turns off previous motor
                self.end = time.perf_counter() - self.start
                time.sleep(self.end) # Pattern time will be pattern_time seconds
                self.end = time.perf_counter() - self.start
                self.status()
     
     
    def shiftpattern(self, sequence):  # Takes double list of motors and converts to pattern.
        """
        Takes a pattern sequence and translates this into a functional pattern in zenbed.
        """
        if (len(sequence) < self.pattern_wave_length):
            print("Pattern wave length is greater than sequence")
            return
        
        sequence[0].increasing = True # Pattern start
            
        while True:
            self.start = time.perf_counter()
            
            for check in range(0, len(sequence), 1):
                
                # Checks if motor is increasing or decreasing
                if sequence[check].increasing == True:
                    sequence[check].percent(sequence[check].motor_power + self.pattern_rate_of_change)
                elif sequence[check].decreasing == True:
                    sequence[check].percent(sequence[check].motor_power - self.pattern_rate_of_change)
                
                # Checks if motor power reaches start power
                if sequence[check - 1].motor_power == self.pattern_start_power and sequence[check].motor_power == 0:
                    sequence[check].increasing = True
                elif sequence[check].motor_power == self.pattern_max_power:
                    sequence[check].decreasing = True
                    sequence[check].increasing  = False
                elif sequence[check].motor_power == 0:
                    sequence[check].decreasing = False
                
            self.end = time.perf_counter() - self.start
            print(self.end)
    
    
    def status(self):
        
        for x in range(A, L+1):
            for y in range(0, 19):
                print((str(self.mtr[x][y].motor_power)), end ='')
            print()
        
        print('{:.6f}s for pattern frame'.format(self.end))
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
