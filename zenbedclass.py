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
        self.rows = []
        self.columns = []
        self.grid
        
        
        
        
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
                
            

