# -*- coding: utf-8 -*-
try:
    from .adafruit.PCA import PCA9685
    from board import SCL, SDA  # Only works when board is available
    import busio
except:
    print("Not connected to Zenbed")
    print("Entering remote development mode...")
    remote_dev = True

import os
import time
from tokenize import Name

# I2C

try:
    i2c_bus = busio.I2C(SCL, SDA)
    print("Zenbed connected")
    time.sleep(5)

except NameError as error:
    print("Zenbed not connected")
    time.sleep(5)

# MotorGrid Size

MOTORGRIDXSIZE = 12
MOTORGRIDYSIZE = 18

# Letter variables

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


class Motor:

    def __init__(self, motorX, motorY):  # Motor(x, y) Creating ZenBed Matrix
        try:
            self.PCA = PCA9685(i2c_bus, 0x40)
        except NameError as error:
            print("No PCA detected")
        self.channel = 0  # default value is first channel
        self.motor_power = 0
        self.x = motorX
        self.y = motorY
        self.hold = None
        self.increasing = None  # Set to either true or false
        self.decreasing = None  # Set to either true or false


        if A <= motorX <= F and 1 <= motorY <= 2 or motorY == 3 and A \
                <= motorX <= D:
            
            # PCA1 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x40)
            except NameError as error:
                print("Could not connect to PCA 1")
                pass

            if motorX == A and motorY == 1:
                self.channel = 0
            if motorX == B and motorY == 1:
                self.channel = 1
            if motorX == C and motorY == 1:
                self.channel = 2
            if motorX == D and motorY == 1:
                self.channel = 3
            if motorX == E and motorY == 1:
                self.channel = 4
            if motorX == F and motorY == 1:
                self.channel = 5
            if motorX == A and motorY == 2:
                self.channel = 6
            if motorX == B and motorY == 2:
                self.channel = 7
            if motorX == C and motorY == 2:
                self.channel = 8
            if motorX == D and motorY == 2:
                self.channel = 9
            if motorX == E and motorY == 2:
                self.channel = 10
            if motorX == F and motorY == 2:
                self.channel = 11
            if motorX == A and motorY == 3:
                self.channel = 12
            if motorX == B and motorY == 3:
                self.channel = 13
            if motorX == C and motorY == 3:
                self.channel = 14
            if motorX == D and motorY == 3:
                self.channel = 15
        elif A <= motorX <= F and 4 <= motorY <= 5 or motorY == 3 and E \
                <= motorX <= F or A <= motorX <= B and motorY == 6:

            # PCA2 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x41)
            except NameError as error:
                print("Could not connect to PCA 2")
                pass


            if motorX == E and motorY == 3:
                self.channel = 0
            if motorX == F and motorY == 3:
                self.channel = 1
            if motorX == A and motorY == 4:
                self.channel = 2
            if motorX == B and motorY == 4:
                self.channel = 3
            if motorX == C and motorY == 4:
                self.channel = 4
            if motorX == D and motorY == 4:
                self.channel = 5
            if motorX == E and motorY == 4:
                self.channel = 6
            if motorX == F and motorY == 4:
                self.channel = 7
            if motorX == A and motorY == 5:
                self.channel = 8
            if motorX == B and motorY == 5:
                self.channel = 9
            if motorX == C and motorY == 5:
                self.channel = 10
            if motorX == D and motorY == 5:
                self.channel = 11
            if motorX == E and motorY == 5:
                self.channel = 12
            if motorX == F and motorY == 5:
                self.channel = 13
            if motorX == A and motorY == 6:
                self.channel = 14
            if motorX == B and motorY == 6:
                self.channel = 15
        elif C <= motorX <= F and motorY == 6 or 7 <= motorY <= 8 and A \
                <= motorX <= F:

            # PCA3 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x42)
            except NameError as error:
                print("Could not connect to PCA 3")
                pass


            if motorX == C and motorY == 6:
                self.channel = 0
            if motorX == D and motorY == 6:
                self.channel = 1
            if motorX == E and motorY == 6:
                self.channel = 2
            if motorX == F and motorY == 6:
                self.channel = 3
            if motorX == A and motorY == 7:
                self.channel = 4
            if motorX == B and motorY == 7:
                self.channel = 5
            if motorX == C and motorY == 7:
                self.channel = 6
            if motorX == D and motorY == 7:
                self.channel = 7
            if motorX == E and motorY == 7:
                self.channel = 8
            if motorX == F and motorY == 7:
                self.channel = 9
            if motorX == A and motorY == 8:
                self.channel = 10
            if motorX == B and motorY == 8:
                self.channel = 11
            if motorX == C and motorY == 8:
                self.channel = 12
            if motorX == D and motorY == 8:
                self.channel = 13
            if motorX == E and motorY == 8:
                self.channel = 14
            if motorX == F and motorY == 8:
                self.channel = 15
        elif A <= motorX <= F and motorY == 9:

            # PCA4 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x43)
            except NameError as error:
                print("Could not connect to PCA 4")
                pass


            if motorX == A and motorY == 9:
                self.channel = 0
            if motorX == B and motorY == 9:
                self.channel = 1
            if motorX == C and motorY == 9:
                self.channel = 2
            if motorX == D and motorY == 9:
                self.channel = 3
            if motorX == E and motorY == 9:
                self.channel = 4
            if motorX == F and motorY == 9:
                self.channel = 5
        elif A <= motorX <= F and 10 <= motorY <= 11 or motorY == 12 \
                and A <= motorX <= D:

            # PCA5 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x44)
            except NameError as error:
                print("Could not connect to PCA 5")
                pass


            if motorX == A and motorY == 10:
                self.channel = 0
            if motorX == B and motorY == 10:
                self.channel = 1
            if motorX == C and motorY == 10:
                self.channel = 2
            if motorX == D and motorY == 10:
                self.channel = 3
            if motorX == E and motorY == 10:
                self.channel = 4
            if motorX == F and motorY == 10:
                self.channel = 5
            if motorX == A and motorY == 11:
                self.channel = 6
            if motorX == B and motorY == 11:
                self.channel = 7
            if motorX == C and motorY == 11:
                self.channel = 8
            if motorX == D and motorY == 11:
                self.channel = 9
            if motorX == E and motorY == 11:
                self.channel = 10
            if motorX == F and motorY == 11:
                self.channel = 11
            if motorX == A and motorY == 12:
                self.channel = 12
            if motorX == B and motorY == 12:
                self.channel = 13
            if motorX == C and motorY == 12:
                self.channel = 14
            if motorX == D and motorY == 12:
                self.channel = 15
        elif A <= motorX <= F and 13 <= motorY <= 14 or motorY == 12 \
                and E <= motorX <= F or A <= motorX <= B and motorY == 15:

            # PCA6 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x45)
            except NameError as error:
                print("Could not connect to PCA 6")
                pass

            if motorX == E and motorY == 12:
                self.channel = 0
            if motorX == F and motorY == 12:
                self.channel = 1
            if motorX == A and motorY == 13:
                self.channel = 2
            if motorX == B and motorY == 13:
                self.channel = 3
            if motorX == C and motorY == 13:
                self.channel = 4
            if motorX == D and motorY == 13:
                self.channel = 5
            if motorX == E and motorY == 13:
                self.channel = 6
            if motorX == F and motorY == 13:
                self.channel = 7
            if motorX == A and motorY == 14:
                self.channel = 8
            if motorX == B and motorY == 14:
                self.channel = 9
            if motorX == C and motorY == 14:
                self.channel = 10
            if motorX == D and motorY == 14:
                self.channel = 11
            if motorX == E and motorY == 14:
                self.channel = 12
            if motorX == F and motorY == 14:
                self.channel = 13
            if motorX == A and motorY == 15:
                self.channel = 14
            if motorX == B and motorY == 15:
                self.channel = 15
        elif C <= motorX <= F and motorY == 15 or A <= motorX <= F \
                and 16 <= motorY <= 17:

            # PCA7 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x46)
            except NameError as error:
                print("Could not connect to PCA 7")
                pass

            if motorX == C and motorY == 15:
                self.channel = 0
            if motorX == D and motorY == 15:
                self.channel = 1
            if motorX == E and motorY == 15:
                self.channel = 2
            if motorX == F and motorY == 15:
                self.channel = 3
            if motorX == A and motorY == 16:
                self.channel = 4
            if motorX == B and motorY == 16:
                self.channel = 5
            if motorX == C and motorY == 16:
                self.channel = 6
            if motorX == D and motorY == 16:
                self.channel = 7
            if motorX == E and motorY == 16:
                self.channel = 8
            if motorX == F and motorY == 16:
                self.channel = 9
            if motorX == A and motorY == 17:
                self.channel = 10
            if motorX == B and motorY == 17:
                self.channel = 11
            if motorX == C and motorY == 17:
                self.channel = 12
            if motorX == D and motorY == 17:
                self.channel = 13
            if motorX == E and motorY == 17:
                self.channel = 14
            if motorX == F and motorY == 17:
                self.channel = 15
        elif A <= motorX <= F and motorY == 18:

            # PCA8 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x47)
            except NameError as error:
                print("Could not connect to PCA 8")
                pass

            if motorX == A and motorY == 18:
                self.channel = 0
            if motorX == B and motorY == 18:
                self.channel = 1
            if motorX == C and motorY == 18:
                self.channel = 2
            if motorX == D and motorY == 18:
                self.channel = 3
            if motorX == E and motorY == 18:
                self.channel = 4
            if motorX == F and motorY == 18:
                self.channel = 5
        elif G <= motorX <= L and 1 <= motorY <= 2 or motorY == 3 and G \
                <= motorX <= J:

            # PCA9 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x48)
            except NameError as error:
                print("Could not connect to PCA 9")
                pass

            if motorX == G and motorY == 1:
                self.channel = 0
            if motorX == H and motorY == 1:
                self.channel = 1
            if motorX == I and motorY == 1:
                self.channel = 2
            if motorX == J and motorY == 1:
                self.channel = 3
            if motorX == K and motorY == 1:
                self.channel = 4
            if motorX == L and motorY == 1:
                self.channel = 5
            if motorX == G and motorY == 2:
                self.channel = 6
            if motorX == H and motorY == 2:
                self.channel = 7
            if motorX == I and motorY == 2:
                self.channel = 8
            if motorX == J and motorY == 2:
                self.channel = 9
            if motorX == K and motorY == 2:
                self.channel = 10
            if motorX == L and motorY == 2:
                self.channel = 11
            if motorX == G and motorY == 3:
                self.channel = 12
            if motorX == H and motorY == 3:
                self.channel = 13
            if motorX == I and motorY == 3:
                self.channel = 14
            if motorX == J and motorY == 3:
                self.channel = 15
        elif G <= motorX <= L and 4 <= motorY <= 5 or motorY == 3 and K \
                <= motorX <= L or G <= motorX <= H and motorY == 6:

            # PCA10 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x49)
            except NameError as error:
                print("Could not connect to PCA 10")
                pass

            if motorX == K and motorY == 3:
                self.channel = 0
            if motorX == L and motorY == 3:
                self.channel = 1
            if motorX == G and motorY == 4:
                self.channel = 2
            if motorX == H and motorY == 4:
                self.channel = 3
            if motorX == I and motorY == 4:
                self.channel = 4
            if motorX == J and motorY == 4:
                self.channel = 5
            if motorX == K and motorY == 4:
                self.channel = 6
            if motorX == L and motorY == 4:
                self.channel = 7
            if motorX == G and motorY == 5:
                self.channel = 8
            if motorX == H and motorY == 5:
                self.channel = 9
            if motorX == I and motorY == 5:
                self.channel = 10
            if motorX == J and motorY == 5:
                self.channel = 11
            if motorX == K and motorY == 5:
                self.channel = 12
            if motorX == L and motorY == 5:
                self.channel = 13
            if motorX == G and motorY == 6:
                self.channel = 14
            if motorX == H and motorY == 6:
                self.channel = 15
        elif I <= motorX <= L and motorY == 6 or 7 <= motorY <= 8 and G \
                <= motorX <= L:

            # PCA11 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x4a)
            except NameError as error:
                print("Could not connect to PCA 11")
                pass

            if motorX == I and motorY == 6:
                self.channel = 0
            if motorX == J and motorY == 6:
                self.channel = 1
            if motorX == K and motorY == 6:
                self.channel = 2
            if motorX == L and motorY == 6:
                self.channel = 3
            if motorX == G and motorY == 7:
                self.channel = 4
            if motorX == H and motorY == 7:
                self.channel = 5
            if motorX == I and motorY == 7:
                self.channel = 6
            if motorX == J and motorY == 7:
                self.channel = 7
            if motorX == K and motorY == 7:
                self.channel = 8
            if motorX == L and motorY == 7:
                self.channel = 9
            if motorX == G and motorY == 8:
                self.channel = 10
            if motorX == H and motorY == 8:
                self.channel = 11
            if motorX == I and motorY == 8:
                self.channel = 12
            if motorX == J and motorY == 8:
                self.channel = 13
            if motorX == K and motorY == 8:
                self.channel = 14
            if motorX == L and motorY == 8:
                self.channel = 15
        elif G <= motorX <= L and motorY == 9:

            # PCA12 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x4b)
            except NameError as error:
                print("Could not connect to PCA 12")
                pass

            if motorX == G and motorY == 9:
                self.channel = 0
            if motorX == H and motorY == 9:
                self.channel = 1
            if motorX == I and motorY == 9:
                self.channel = 2
            if motorX == J and motorY == 9:
                self.channel = 3
            if motorX == K and motorY == 9:
                self.channel = 4
            if motorX == L and motorY == 9:
                self.channel = 5
        elif G <= motorX <= L and 10 <= motorY <= 11 or motorY == 12 \
                and G <= motorX <= J:

            # PCA13 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x4c)
            except NameError as error:
                print("Could not connect to PCA 13")
                pass

            if motorX == G and motorY == 10:
                self.channel = 0
            if motorX == H and motorY == 10:
                self.channel = 1
            if motorX == I and motorY == 10:
                self.channel = 2
            if motorX == J and motorY == 10:
                self.channel = 3
            if motorX == K and motorY == 10:
                self.channel = 4
            if motorX == L and motorY == 10:
                self.channel = 5
            if motorX == G and motorY == 11:
                self.channel = 6
            if motorX == H and motorY == 11:
                self.channel = 7
            if motorX == I and motorY == 11:
                self.channel = 8
            if motorX == J and motorY == 11:
                self.channel = 9
            if motorX == K and motorY == 11:
                self.channel = 10
            if motorX == L and motorY == 11:
                self.channel = 11
            if motorX == G and motorY == 12:
                self.channel = 12
            if motorX == H and motorY == 12:
                self.channel = 13
            if motorX == I and motorY == 12:
                self.channel = 14
            if motorX == J and motorY == 12:
                self.channel = 15
        elif G <= motorX <= L and 13 <= motorY <= 14 or motorY == 12 \
                and K <= motorX <= L or G <= motorX <= H and motorY == 15:

            # PCA14 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x4d)
            except NameError as error:
                print("Could not connect to PCA 14")
                pass

            if motorX == K and motorY == 12:
                self.channel = 0
            if motorX == L and motorY == 12:
                self.channel = 1
            if motorX == G and motorY == 13:
                self.channel = 2
            if motorX == H and motorY == 13:
                self.channel = 3
            if motorX == I and motorY == 13:
                self.channel = 4
            if motorX == J and motorY == 13:
                self.channel = 5
            if motorX == K and motorY == 13:
                self.channel = 6
            if motorX == L and motorY == 13:
                self.channel = 7
            if motorX == G and motorY == 14:
                self.channel = 8
            if motorX == H and motorY == 14:
                self.channel = 9
            if motorX == I and motorY == 14:
                self.channel = 10
            if motorX == J and motorY == 14:
                self.channel = 11
            if motorX == K and motorY == 14:
                self.channel = 12
            if motorX == L and motorY == 14:
                self.channel = 13
            if motorX == G and motorY == 15:
                self.channel = 14
            if motorX == H and motorY == 15:
                self.channel = 15
        elif I <= motorX <= L and motorY == 15 or 16 <= motorY <= 17 \
                and G <= motorX <= L:

            # PCA15 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x4e)
            except NameError as error:
                print("Could not connect to PCA 15")
                pass

            if motorX == I and motorY == 15:
                self.channel = 0
            if motorX == J and motorY == 15:
                self.channel = 1
            if motorX == K and motorY == 15:
                self.channel = 2
            if motorX == L and motorY == 15:
                self.channel = 3
            if motorX == G and motorY == 16:
                self.channel = 4
            if motorX == H and motorY == 16:
                self.channel = 5
            if motorX == I and motorY == 16:
                self.channel = 6
            if motorX == J and motorY == 16:
                self.channel = 7
            if motorX == K and motorY == 16:
                self.channel = 8
            if motorX == L and motorY == 16:
                self.channel = 9
            if motorX == G and motorY == 17:
                self.channel = 10
            if motorX == H and motorY == 17:
                self.channel = 11
            if motorX == I and motorY == 17:
                self.channel = 12
            if motorX == J and motorY == 17:
                self.channel = 13
            if motorX == K and motorY == 17:
                self.channel = 14
            if motorX == L and motorY == 17:
                self.channel = 15
        elif G <= motorX <= L and motorY == 18:

            # PCA16 < works correct

            try:
                self.PCA = PCA9685(i2c_bus, 0x4f)
            except NameError as error:
                print("Could not connect to PCA 16")
                pass

            if motorX == G and motorY == 18:
                self.channel = 0
            if motorX == H and motorY == 18:
                self.channel = 1
            if motorX == I and motorY == 18:
                self.channel = 2
            if motorX == J and motorY == 18:
                self.channel = 3
            if motorX == K and motorY == 18:
                self.channel = 4
            if motorX == L and motorY == 18:
                self.channel = 5
        elif motorX == 0 or motorY == 0:

            # Allows grid to be instantiated

            self = None
        else:

            print
            'out of range when x is ' + str(motorX) + ' and y is ' + str(motorY)
            quit()

        try:
            self.PCA.frequency = 60
        except AttributeError as error:
            pass

    # Turns on all motors connected to the PCA to 20%

    def Testpcas(self):
        """
        Tests the PCA attached is functioning.
        In order to ensure that the circuitry for the bed is functioning
        properly this function will turn on all motors connected to the PCA.
        """

        if self.PCA:
            for i in range(0, 15):
                self.PCA.channels[i].duty_cycle = int(0xfffe * 0)  # Turns on to 20%
        else:
            pass

    # Turns on motor

    def on(self):
        """
        Sets motor to full power.
        """

        if self.PCA:
            self.PCA.channels[self.channel].duty_cycle = 0xfffe  # Turns on to full

    # Turns motor to 50%

    def half(self):
        """
        Sets motor to 50% power.
        """
        if self.PCA:
            self.PCA.channels[self.channel].duty_cycle = 0x7FFF  # Turns on to half

    # Turns motor to 0

    def off(self):
        """
        Sets motor to 0% power.
        """
        if self.PCA:
            self.PCA.channels[self.channel].duty_cycle = 0  # Turns off

    # Gives vibration motor percent power

    #

    def percent(self, percentpower):  # Percent on
        """
        Sets motor to user defined power in percent.
        Parameters:
        percentpower (int): percentage of the motor power
        """

        if percentpower > 80:  # safety lock / testing
            percentpower = 80

        if (percentpower < 0):
            print("Negative power level")
        else:

            self.motor_power = int(percentpower)

            try:
                self.PCA.channels[self.channel].duty_cycle = int(0xFFFF
                                                                 * self.motor_power / 100)
            except AttributeError as error:
                pass
