#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
import grovepi
from adafruit_servokit import ServoKit #Location on system -> /usr/local/lib/python3.9/dist-packages

#Constants

nbPCAServo=10 #The first 10 pins are filled 

#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[5000, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]

#Objects
pca = ServoKit(channels=16) # Creates an object from class "ServoKit" where channels = 16
pca2 = ServoKit(channels=16) # Second motor for more motors 
# function init 
def init():

    for i in range(nbPCAServo): # Loops for amount of servos connected
        pca.servo[i].set_pulse_width_range(4000 , 5000) # Initialization of pulse


# function main 
def main():

    pcaScenario();


# function pcaScenario 
def pcaScenario():
    """Scenario to test servo"""
    for i in range(nbPCAServo):
        for j in range(MIN_ANG[i],MAX_ANG[i],1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        for j in range(MAX_ANG[i],MIN_ANG[i],-1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        pca.servo[i].angle=None #disable channel
        time.sleep(0.5)




if __name__ == '__main__':
    init()
    main()
