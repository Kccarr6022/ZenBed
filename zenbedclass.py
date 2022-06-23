# -*- coding: utf-8 -*-
from motorclass import Motor
import sys
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

        # Algorithms

    def Rectanglepattern(self):  # Current 1d array loop <- Functional
        """
        Rectangle pattern for zenbed.
        """
        while True:
            for i in range(1, 18):
                for j in range(A, L):
                    motora = Motor(j, i)
                    motora.percent(14)
                time.sleep(0.5)
                for j in range(A, L):
                    motora = Motor(j, i)
                    motora.percent(0)
    
    def Circlepattern(self):  # Current 1d array loop <- Functional
        """
        Rectangle pattern for zenbed.
        """
        while True:
            for i in range(1, 18):
                for j in range(A, L):
                    motora = Motor(j, i)
                    motora.percent(0)
                time.sleep(0.5)
                for j in range(A, L):
                    motora = Motor(j, i)
                    motora.percent(0)

    def Zigzagpattern(self):  # Current 1d array loop <- Functional
        """
        Rectangle pattern for zenbed.
        """
        while True:
            for i in range(1, 18):
                for j in range(A, L):
                    motora = Motor(j, i)
                    motora.percent(0)
                time.sleep(0.5)
                for j in range(A, L):
                    motora = Motor(j, i)
                    motora.percent(0)
                    
    def Inifinitypattern(self, speed, power_level, width):
        print("Incomplete")
        
    def on(self, percent):
        for y in range (1, 19):
            for x in range (A, L):
                self.mtr[x][y].percent(percent)
    
    def off(self):
        for y in range (1, 19):
            for x in range (A, L):
                self.mtr[x][y].percent(0)      
