# -*- coding: utf-8 -*-
from classes.motorclass import Motor
from classes.patternclass import Pattern
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


class Zenbed:

    def __init__(self):  # Initializing all the PCAs / Motors are connected to PCAs
        # Initializing a a double list of motors
        self.mtr = []
        for x in range(0, MOTORGRIDXSIZE + 1):
            self.mtr.append([])
            for y in range(0, MOTORGRIDYSIZE + 1):
                self.mtr[x].append(Motor(x, y))

        # Pattern variables
        self.pattern_wave_length = 3
        self.pattern_time = 0.1  # Time in seconds of patterns
        self.pattern_percent_power = 100
        self.pattern_percent_power = self.pattern_percent_power / 100
        self.pattern_start_power = 20 * self.pattern_percent_power  # Where the first motor in the wave starts by
        self.pattern_max_power = 50 * self.pattern_percent_power  # Where the power in the wave is highest
        self.pattern_rate_of_change = 1 * self.pattern_percent_power  # The option to change the rate of power increments

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

        self.string_rectangle = """D4 E4, D5 E5, D6 E6, D7 E7, D8 E8, D9 E9, D10 E10, D11 E11, D12 E12, D13 E13, 
                                D14 E14, D15 E15, D16 D17 E16 E17, F16 F17, G16 G17, H16 H17 I16 I17, H15 I15,
                                "H14 I14, H13 I13, H12 I12, H11 I11, H10 I10, H9 I9, H8 I8, H7 I7, H6 I6, H5 I5,
                                "H4 I4, H3 I3 H2 I2, G2 G3, F2 F3, D2 E2 D3 E3 """

        # self.string_test = "D4 E14, D5 E5"
        # self.zigzag = []

        def __del__(self):
            self.off()

    # Algorithms
    def string_to_sequence(self, string):
        """
        Takes a string of Coordinates and converts to a double array of motors.
        :param string: "Letter (A-L) -> number (1-18) - > comma (divides motor object)"
        :return:
        """
        string = string + "!"
        list = 0
        element = 0
        sequence = []
        motors = []
        x = 0
        y = 0
        for char in range(0, len(string), 1):

            if 'A' <= string[char] <= 'L':
                x = ord(string[char]) - ord('A') + 1

            elif '0' <= string[char] <= '9':
                if '0' <= string[char + 1] <= '9':
                    y = 10
                    continue
                y = y + ord(string[char]) - ord('0')
                motors.insert(element, self.mtr[x][y])
                print("Added motor " + chr(x + 64) + str(y) + " to list ")
                x = 0
                y = 0

            elif string[char] == ',':
                sequence.insert(list, motors)
                print("Motors", end=' ')
                for x in motors:
                    print(chr(x.x + 64) + str(x.y), end=' ')
                print("passed successfully.")
                list = list + 1
                motors = []

            elif string[char] == '!':
                sequence.insert(list, motors)
                list = list + 1
                print("Motors ")
                for x in motors:
                    print(chr(x.x + 64) + str(x.y), end=' ')
                print("passed successfully.")
                return sequence
            else:
                continue

    def sequence_to_pattern(self, sequence):  # Takes double list of motors and converts to pattern.
        """
        Takes a pattern sequence and translates this into a functional pattern in zenbed.
        """
        sequence[0][0].increasing = True  # Pattern start

        while True:
            self.start = time.perf_counter()

            for check in range(0, len(sequence), 1):

                # Checks if motor is increasing or decreasing
                if sequence[check][0].increasing:
                    for motor in range(0, len(sequence[check])):
                        sequence[check][motor].percent(sequence[check][motor].motor_power + self.pattern_rate_of_change)
                elif sequence[check][0].decreasing:
                    for motor in range(0, len(sequence[check])):
                        sequence[check][motor].percent(sequence[check][motor].motor_power - self.pattern_rate_of_change)

                # Checks if motor power reaches start power
                if sequence[check - 1][0].motor_power >= self.pattern_start_power and sequence[check][
                    0].motor_power == 0:
                    sequence[check][0].increasing = True
                elif sequence[check][0].motor_power >= self.pattern_max_power:
                    sequence[check][0].decreasing = True
                    sequence[check][0].increasing = False
                elif sequence[check][0].motor_power == 0:
                    sequence[check][0].decreasing = False

            self.end = time.perf_counter() - self.start
            try:
                time.sleep(self.pattern_time - self.end)
            except ValueError as error:
                print("The pattern frame ran ", '{:.6f}s '.format(-1 * (self.pattern_time - self.end)),
                      "over the set latency!")

            self.end = time.perf_counter() - self.start
            self.status()

    def pattern(self, pattern):
        """ Takes a pattern and variables to process pattern frames to a functioning sequence.

        Args:
            pattern (_type_): 
        """
        self.pattern_time = pattern.time
        self.pattern_percent_power = pattern.percent_power
        self.pattern_start_power = pattern.start_power
        self.pattern_max_power = pattern.max_power
        self.pattern_rate_of_change = pattern.rate_of_change
        self.sequence(pattern.sequence)

    def sequence(self, pattern):
        """
        Takes a sting and converts directly into a Zen Bed pattern
        :param pattern (string): "Letter (A-L) -> number (1-18) - > comma (divides motor object)"
        :return:
        """
        self.sequence_to_pattern(self.string_to_sequence(pattern))

    def all_motors_increase(self):  # Takes double list of motors and converts to pattern.
        """
        Gradually increases and decreases motors.
        """
        while True:
            self.start = time.perf_counter()
            for x in range(0, MOTORGRIDXSIZE + 1):
                for y in range(0, MOTORGRIDYSIZE + 1):
                    # Checks if motor is increasing or decreasing
                    if self.mtr[1][1].motor_power < self.pattern_max_power and self.mtr[1][1].decreasing != True:
                        self.mtr[x][y].percent(self.mtr[x][y].motor_power + self.pattern_rate_of_change)
                    elif self.mtr[1][1].decreasing:
                        self.mtr[x][y].percent(self.mtr[x][y].motor_power - self.pattern_rate_of_change)
                    elif self.mtr[1][1].motor_power >= self.pattern_max_power:
                        self.mtr[1][1].decreasing = True
                    else:
                        self.mtr[x][y].percent(self.mtr[x][y].motor_power - self.pattern_rate_of_change)

            self.end = time.perf_counter() - self.start
            self.status()

    def status(self):
        """
        Relays grid information and algorithm delay/ frame delay
        :return:
        """
        for y in range(1, 19):
            for x in range(A, L + 1):
                if 10 <= self.mtr[x][y].motor_power <= 99:
                    print(str(self.mtr[x][y].motor_power), end=' ')
                elif self.mtr[x][y].motor_power == 100:
                    print(str(self.mtr[x][y].motor_power), end='')
                else:
                    print(str(self.mtr[x][y].motor_power), end='  ')
            print()

        print('{:.6f}s for pattern frame'.format(self.end))
        print()

    def return_row(self, y):
        """
        Returns row into a double list
        :param y(int): row number
        :return:
        """
        returned = []
        for x in range(0, MOTORGRIDXSIZE):
            returned.append([])
            returned[x].append(self.mtr[x][y])
        return returned

    def return_column(self, x):
        """
        returns column into a double list which can be processed by pattern_to_sequence
        :param x(int): grid coordinate
        :return:
        """
        returned = []
        for y in range(1, 19):
            returned.append(self.mtr[x][y])
        return returned

    def row(self, y, percent):
        """
        Turns row into percent power
        :param y(int): grid coordinate
        :param percent(int): percent on
        :return:
        """
        for x in range(A, L):
            self.mtr[x][y].percent(percent)

    def column(self, x, percent):
        """
        Turns column into percent power
        :param x(int): grid coordinate
        :param percent(int): percent on
        :return:
        """
        for y in range(1, 19):
            self.mtr[x][y].percent(percent)

    def on(self):
        """
        Turns on all motors to 15% power
        :return:
        """
        for y in range(1, 19):
            for x in range(A, L + 1):
                self.mtr[x][y].percent(15)

    def on(self, percent):
        """
        Takes percent and turns on to the percent parameter
        :param percent(int): Percent motors are on
        :return:
        """
        for y in range(1, 19):
            for x in range(A, L + 1):
                self.mtr[x][y].percent(percent)

    def off(self):
        """
        Turns all motors off
        :return:
        """
        for y in range(1, 19):
            for x in range(A, L + 1):
                self.mtr[x][y].percent(0)
