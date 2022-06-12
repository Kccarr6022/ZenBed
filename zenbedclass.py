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
    def __init__(self): # Initializing all the PCAs / Motors are connected to PCAs
        
        
        # Initializing a a double array of motors
        self.mtr = []

        for x in range(0, 13):
            self.mtr.append([])
            for y in range(0, 19):
                self.mtr[x].append(Motor(x,y))
        
        
        
        
        # Algorithms 
        
    def Waving(): # Current 1d array loop <- Functional
        while True:
            for i in range(1, 18):
                for j in range(A, L):
                    Motora = Motor(j, i)
                    Motora.percent(0)
                time.sleep(0.5)
                for j in range(A, L):
                    Motora = Motor(j, i)
                    Motora.percent(0)
                
    def pattern2():
        while True:
            for x in range (A, L):
                for y in range (1, 18):
                    self.mtr[x][y].percent(0) # 0 to 10
                    self.mtr[x + 1][y].percent(0) # 0 to 10
                time.sleep(1)
                for y in range (1, 19):
                    self.mtr[x][y].percent(0)
