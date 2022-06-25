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
        self.pattern_time = 0.1 # Time in seconds of patterns
        self.pattern_percent_power = 100
        self.pattern_percent_power = self.pattern_percent_power / 100
        self.pattern_start_power = 20 * self.pattern_percent_power # Where the first motor in the wave starts by
        self.pattern_max_power = 50 * self.pattern_percent_power # Where the power in the wave is highest
        self.pattern_rate_of_change =  1 * self.pattern_percent_power # The option to change the rate of power increments
        
        
        self.start = 0
        self.end = 0
        
        
        # Sequences
        self.rectangle = [[self.mtr[D][4], self.mtr[E][4]],
                          [self.mtr[D][5], self.mtr[E][5]],
                          [self.mtr[D][6], self.mtr[E][6]],
                          [self.mtr[D][7], self.mtr[E][7]],
                          [self.mtr[D][8], self.mtr[E][8]],
                          [self.mtr[D][9], self.mtr[E][9]],
                          [self.mtr[D][10], self.mtr[E][10]],
                          [self.mtr[D][11], self.mtr[E][11]],
                          [self.mtr[D][12], self.mtr[E][12]],
                          [self.mtr[D][13], self.mtr[E][13]],
                          [self.mtr[D][14], self.mtr[E][14]],
                          [self.mtr[D][15], self.mtr[E][15]],
                          [self.mtr[D][16], self.mtr[E][16], self.mtr[D][17], self.mtr[E][17]],
                          [self.mtr[F][16], self.mtr[F][17]],
                          [self.mtr[G][16], self.mtr[G][17]],
                          [self.mtr[H][16], self.mtr[H][17], self.mtr[I][16], self.mtr[I][17]],
                          [self.mtr[H][15], self.mtr[I][15]],
                          [self.mtr[H][14], self.mtr[I][14]],
                          [self.mtr[H][13], self.mtr[I][13]],
                          [self.mtr[H][12], self.mtr[I][12]],
                          [self.mtr[H][11], self.mtr[I][11]],
                          [self.mtr[H][10], self.mtr[I][10]],
                          [self.mtr[H][9], self.mtr[I][9]],
                          [self.mtr[H][8], self.mtr[I][8]],
                          [self.mtr[H][7], self.mtr[I][7]],
                          [self.mtr[H][6], self.mtr[I][6]],
                          [self.mtr[H][5], self.mtr[I][5]],
                          [self.mtr[H][4], self.mtr[I][4]],
                          [self.mtr[H][3], self.mtr[I][3], self.mtr[H][2], self.mtr[I][2]],
                          [self.mtr[G][2], self.mtr[G][3]],
                          [self.mtr[F][2], self.mtr[F][3]],
                          [self.mtr[D][2], self.mtr[E][2], self.mtr[D][3], self.mtr[E][3]]
                          ]

        
        def __del__(self):
            self.off()

    #self.zigzag = []
    #self.testtopbottom = []
    #self.testtopbottom
    
        
    # Algorithms
    def string_to_sequence(self, string):
        sequence = []
        sequence.append([])
        list = 0 # The list to append to
        element = 0
        count = 0
        x = 0
        y = 0
        for char in range(0, len(string)):
            if count % 3 == 0: # X coordinate
                x = ord(string[char]) - ord('A') + 1
            elif count % 3 == 1: # Y coordinate
                try:
                    if (0 <= (ord(string[char + 1]) - ord('0')) <= 9):
                        y = 10
                        continue
                
                    if y < 10:
                        y = ord(string[char]) - ord('0')
                    elif y == 10:
                        y = y + ord(string[char]) - ord('0')
                    sequence[list].append(self.mtr[x][y])
                except IndexError: 
                    return sequence 
            elif count % 3 == 2: # Operation
                if (string[char] == ' '):
                    element = element + 1
                elif (string[char] == ','):
                    element = 0
                    sequence.append([])
                    list = list + 1
                else:
                    return sequence
            else:
                return sequence
            count = count + 1
            
    
    
    
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
     
     
    def sequence_to_pattern(self, sequence):  # Takes double list of motors and converts to pattern.
        """
        Takes a pattern sequence and translates this into a functional pattern in zenbed.
        """
        if (len(sequence) < self.pattern_wave_length):
            print("Pattern wave length is greater than sequence")
            return
        
        sequence[0][0].increasing = True # Pattern start
            
        while True:
            self.start = time.perf_counter()
            
            for check in range(0, len(sequence), 1):
                
                # Checks if motor is increasing or decreasing
                if sequence[check][0].increasing == True:
                    for motor in range(0, len(sequence[check])):
                        sequence[check][motor].percent(sequence[check][motor].motor_power + self.pattern_rate_of_change)
                elif sequence[check][0].decreasing == True:
                    for motor in range(0, len(sequence[check])):
                        sequence[check][motor].percent(sequence[check][motor].motor_power - self.pattern_rate_of_change)
                
                # Checks if motor power reaches start power
                if sequence[check - 1][0].motor_power == self.pattern_start_power and sequence[check][0].motor_power == 0:
                    sequence[check][0].increasing = True
                elif sequence[check][0].motor_power == self.pattern_max_power:
                    sequence[check][0].decreasing = True
                    sequence[check][0].increasing  = False
                elif sequence[check][0].motor_power == 0:
                    sequence[check][0].decreasing = False
                
            self.end = time.perf_counter() - self.start
            self.status()
    
    
    def status(self):
        for y in range(0, 19):
            for x in range(A, L+1):
                if 10 <= self.mtr[x][y].motor_power <= 99:
                    print( str(self.mtr[x][y].motor_power), end =' ')
                elif self.mtr[x][y].motor_power == 100:
                    print( str(self.mtr[x][y].motor_power), end ='')
                else:
                    print( str(self.mtr[x][y].motor_power), end ='  ')
            print()
        
        print('{:.6f}s for pattern frame'.format(self.end))
        print()
        
            
    def returnrow(self, y):
        returned = []
        for x in range(0, MOTORGRIDXSIZE):
            returned.append([])
            returned[x].append(self.mtr[x][y])
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
