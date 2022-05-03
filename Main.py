from motorclass import Motor
import zenbedclass
import sys
import time

# MotorGrid Size
MOTORGRIDXSIZE = 10
MOTORGRIDYSIZE = 10

# Create motor = 



def CircleLoop():
    
    motor = []
    
    for i in range(10):
        motor.append(Motor(i, 0))
        motor[i].motoron()
        time.sleep(2)
        motor[i].motoroff()

    
def main():
    CircleLoop()
    


main()



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