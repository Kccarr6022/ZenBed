from motorclass import Motor
from zenbedclass import ZenBed
from PCA import PCA9685
import time
import busio
from board import SCL, SDA

# creates i2c object
i2c_bus = busio.I2C(SCL, SDA)

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

# Grid (Nested List)
mtr = []

for x in range(0, 13):
    mtr.append([])
    for y in range(0, 19):
        mtr[x].append(Motor(x,y))


# grid test
def print_grid(param):
    for row in param:
        for e in row:
            print(e, end ='')
        print()

# Motor test  
def testallmotors():
    for i in range(0, 15):
        PCA = PCA9685(i2c_bus, 0x40 + i)
        PCA.frequency = 1600
        for j in range(0, 15):
            PCA.channels[j].duty_cycle = int(0xFFFF * 15 / 100)
    time.sleep(5)
    for i in range(0, 15):
        PCA = PCA9685(i2c_bus, 0x40 + i)
        PCA.frequency = 1600
        for j in range(0, 15):
            PCA.channels[j].duty_cycle = int(0xFFFF * 0 / 100)


# Test single motors
def testsinglemotors():
    
    motorC1 = Motor(A, 1)
    motorC1.Testpcas()
"""    
def usercontrol(): #
    while True:
        
        #Command
        
        
        
        
        
        
        
        lmmkl''''''';llkkkl;'';lkkl;'';lkkl;l'lk       mmklmkl
        'll;while Command != 
        #Command = input()
"""

def line(): # Pattern for ZENBED (import to zenbedclass)
    while True:
        for y in range (1, 18):
                for x in range (A, L):
                    mtr[x][y].percent(0) # 0 to 100
                    mtr[x][y+1].percent(0)
                time.sleep(1)
                for x in range (A, L):
                    mtr[x][y].percent(0)
                    mtr[x][y+1].percent(0)

#         for x in range (A, L):
#             mtr[x][y].percent(15) # 0 to 100
#             
#             mtr[x + 1][y].percent(15) # 0 to 100
            
def onebyone(): # Pattern for ZENBED (import to zenbedclass)
    while True:
        for y in range (1, 18):           
            for x in range (I, L):
                mtr[x][y].percent(15) # 0 to 100
                time.sleep(1)
        for x in range (A, L):
            mtr[x][y].percent(15) # 0 to 100
            
            mtr[x + 1][y].percent(15) # 0 to 100

def stop():
    while True:
        for y in range (1, 18):
            for x in range (A, L):
                mtr[x][y].percent(0)
                mtr[x][y+1].percent(0)
            time.sleep(.1)
            for x in range (A, L):
                mtr[x][y].percent(0)
                mtr[x][y+1].percent(0)

           
def pattern3():
    while True:
        for y in range (1, 18):
                for x in range (A, L):
                    mtr[x][y].percent(20)
                    mtr[x][y+1].percent(20)
                time.sleep(1)
                for x in range (A, L):
                    mtr[x][y].percent(10)
                    mtr[x][y+1].percent(10)
                time.sleep(3)
                for x in range (A, L):
                    mtr[x][y].percent(0)
                    mtr[x][y+1].percent(0)

"""
    Motor on -> mtr[letter][number].percent(percent power)
    
"""

def main():
    stop()

main()