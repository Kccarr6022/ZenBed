from motorclass import Motor
from zenbedclass import ZenBed
from PCA import PCA9685
import sys
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

# Motor Array
Matrix = [[0 for x in range(MOTORGRIDXSIZE)] for y in range(MOTORGRIDYSIZE)]

# Motor test  
def testallmotors():
    for i in range(0, 15):
        PCA = PCA9685(i2c_bus, 0x40 + i)
        PCA.frequency = 60
        for j in range(0, 15):
            PCA.channels[j].duty_cycle = int(0xFFFF * 15 / 100)
    time.sleep(10)
    for i in range(0, 15):
        PCA = PCA9685(i2c_bus, 0x40 + i)
        PCA.frequency = 1600
        for j in range(0, 15):
            PCA.channels[j].duty_cycle = int(0xFFFF * 0 / 100)


# Test single motors
def testsinglemotors():
    motorC1 = Motor(J, 14)
    motorC1.motorpercenton(15)
    time.sleep(5)
    motorC1.motorpercenton(0)
    
def userinput():
    int(input("Motor to turn on(letter+num = {0...100}"))


def main():
    testsinglemotors()
    
    
main()

"""
    MotorB = Motor(G, 10)
    MotorB.motorpercenton(10)
    
    MotorC = Motor(A, 1) # check
    MotorC.motorpercenton(0)
    
    MotorD = Motor(A, 16)
    MotorD.motorpercenton(0)

    
    count = 0
    PCA[16]
    for i in range(0, 15):
        PCA[i] = PCA9685(i2c_bus, 0x40 + i)
        PCA[i].frequency = 60
        for j in range(0, 15):
            PCA[count].channels[j].duty_cycle = 0x
    """    




# Sample algorithm
"""def patternfullon():
    
    motor = []
    power = 100
    
    for i in range(10):
        for i in range(power)
            motor.append(Motor(i, 0))
            motor[i].motorpercenton(power/100)
            time.sleep(2)
        
    for i in range(10):
        motor.append(Motor(i, 0))
        motor[i].motoroff()
        time.sleep(2)
"""