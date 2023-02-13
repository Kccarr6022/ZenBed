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

    def __init__(self, connect: bool):  # Initializing all the PCAs / Motors are connected to PCAs
        # Initializing a a double list of motors
        if connect:
            print("\033[92mConnecting to Motors...\033[0m")
        else:
            print("\033[91mNot connecting to Motors...\033[0m")

        self.connect = connect
        self.mtr = []
        for x in range(0, MOTORGRIDXSIZE + 1):
            self.mtr.append([])
            for y in range(0, MOTORGRIDYSIZE + 1):
                self.mtr[x].append(Motor(x, y, connect))

        # Pattern variables  
        self.pattern_active: bool = False
        self.pattern_wave_length: int = 3
        self.pattern_intervals_per_second: float = 3 # frequency of element adjustment (every .1 seconds it increases by the rate of change)
        self.pattern_percent_power: int = 100
        self.pattern_percent_power: float = self.pattern_percent_power / 100
        self.pattern_start_power: float = 20 * self.pattern_percent_power  # Power level previous element must reach for the next element to start increasing
        self.pattern_max_power: int = 50 * self.pattern_percent_power  # Where the power in the wave is highest
        self.pattern_interval_power: int = 1 * self.pattern_percent_power  # The percent of power that an element adjusts by.
        self.pattern_reverse: bool = False
        self.cycle_time: float = 0

        self.string_rectangle = """D4 E4, D5 E5, D6 E6, D7 E7, D8 E8, D9 E9, D10 E10, D11 E11, D12 E12, D13 E13, 
                                D14 E14, D15 E15, D16 D17 E16 E17, F16 F17, G16 G17, H16 H17 I16 I17, H15 I15,
                                "H14 I14, H13 I13, H12 I12, H11 I11, H10 I10, H9 I9, H8 I8, H7 I7, H6 I6, H5 I5,
                                "H4 I4, H3 I3 H2 I2, G2 G3, F2 F3, D2 E2 D3 E3 """

        # keeps list of frame times as it runs so we can get an average and also calculate variance
        self.frame_list = []
        # keeps a running total of frame time so we don't have to sum the frame_list twice
        self.total_frame_time: float = 0
        self.frame_high: float = 0 # the highest frame time
        self.frame_low: float = 0 # the lowest frame time
        # the number of motors which that had their power change during a frame/cycle
        self.motors_changed_this_cycle: int = 0

        def __del__(self):
            self.stop()

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
                #print("Added motor " + chr(x + 64) + str(y) + " to list ")
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
                print("Motors", end=' ')
                for x in motors:
                    print(chr(x.x + 64) + str(x.y), end=' ')
                print("passed successfully.")
                return sequence
            else:
                continue

    def pattern(self, pattern: Pattern) -> None:  # Takes double list of motors and converts to pattern.
        """
        Takes a pattern sequence and translates this into a functional pattern in zenbed.
        """


        self.pattern_intervals_per_second: float = pattern.intervals_per_second
        self.pattern_percent_power: float = pattern.percent_power
        self.pattern_start_power: int = pattern.start_power
        self.pattern_max_power: int = pattern.max_power
        self.pattern_interval_power: int = pattern.interval_power
        self.pattern_reverse: bool = True
        sequence = self.string_to_sequence(pattern.sequence)
        
        # Allows us to loop with named variables
        prev_sequence = list(sequence)
        prev_sequence.insert(0, sequence[-1])

        # Pattern start
        self.pattern_active = True
        sequence[0][0].increasing = True
        
        while self.pattern_active:
            start_time= time.perf_counter()
            self.motors_changed_this_cycle = 0

            for prev_element, curr_element in zip(prev_sequence, sequence):


                # sequence_indexs if motor is increasing or decreasing
                if curr_element[0].increasing:
                    for motor in curr_element:
                        motor.percent(motor.motor_power + self.pattern_interval_power)
                        self.motors_changed_this_cycle += 1
                elif curr_element[0].decreasing:
                    for motor in curr_element:
                        motor.percent(motor.motor_power - self.pattern_interval_power)
                        self.motors_changed_this_cycle += 1

                # sequence_indexs if motor power reaches start power
                if prev_element[0].motor_power >= self.pattern_start_power and curr_element[
                    0].motor_power == 0:
                    curr_element[0].increasing = True
                elif curr_element[0].motor_power >= self.pattern_max_power:
                    if pattern.hold and sequence[-1][0].motor_power < pattern.max_power:
                        curr_element[0].increasing = False
                        
                    elif pattern.hold and sequence[-1][0].motor_power >= pattern.max_power:
                        for hold_second in range(pattern.hold):
                            print("Hold for " + str(pattern.hold - hold_second) + " more seconds...")
                            time.sleep(1)
                        self.stop()
                        sequence[0][0].increasing = True  # Pattern start
                    else:
                        curr_element[0].decreasing = True
                        curr_element[0].increasing = False
                elif curr_element[0].motor_power == 0:
                    curr_element[0].decreasing = False

            self.cycle_time = time.perf_counter() - start_time
            try:
                time.sleep( 1/self.pattern_intervals_per_second - self.cycle_time)
            except ValueError as error:
                print("The pattern frame ran ", '{:.6f}s '.format(-1 * ( 1/self.pattern_intervals_per_second - self.cycle_time)),
                      "over the set latency!")

            self.cycle_time = time.perf_counter() - start_time
            self.status()


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
            for x in range(0, MOTORGRIDXSIZE + 1):
                for y in range(0, MOTORGRIDYSIZE + 1):
                    # sequence_indexs if motor is increasing or decreasing
                    if self.mtr[1][1].motor_power < self.pattern_max_power and self.mtr[1][1].decreasing != True:
                        self.mtr[x][y].percent(self.mtr[x][y].motor_power + self.pattern_interval_power)
                    elif self.mtr[1][1].decreasing:
                        self.mtr[x][y].percent(self.mtr[x][y].motor_power - self.pattern_interval_power)
                    elif self.mtr[1][1].motor_power >= self.pattern_max_power:
                        self.mtr[1][1].decreasing = True
                    else:
                        self.mtr[x][y].percent(self.mtr[x][y].motor_power - self.pattern_interval_power)

            self.status()

    def status(self):
        """
        Relays grid information and algorithm delay/ frame delay
        :return:
        """          
        on_or_off = '\033[92m' if self.connect else '\033[91m'
        print(f'   {on_or_off}A1 B2 C3 D4 E5 F6 G7 H8 I9 J0 K1 L12 \033[0m')

        for y in range(1, 19):
            for x in range(A, L + 1):
                if x == 1:
                    if y < 10:
                        print('{} {}|\033[0m'.format(on_or_off, y), end=' ')
                    else:
                        print('{}{}|\033[0m'.format(on_or_off, y), end=' ')
                if 10 <= self.mtr[x][y].motor_power <= 99:
                    print(str(self.mtr[x][y].motor_power), end=' ')
                elif self.mtr[x][y].motor_power == 100:
                    print(str(self.mtr[x][y].motor_power), end='')
                elif self.mtr[x][y].motor_power == 0:
                    print("-", end='  ')
                else:
                    print(str(self.mtr[x][y].motor_power), end='  ')
            print()

        if self.pattern_active:
            self.status_frame_info()

    def status_frame_info(self):
        # subtract the delay added by SLEEP to get the true cycle time
        frame_time_offset: float = 1 / self.pattern_intervals_per_second
        frame_time: float = self.cycle_time - frame_time_offset if self.cycle_time > 0 else 0
        
        self.frame_list.append(frame_time)
        frame_count: int = len(self.frame_list)

        # average frame time
        self.total_frame_time += frame_time
        average_time = self.total_frame_time / frame_count if frame_count > 0 else 0

        # add up how much each frame differs from the new average frame time
        total_variance: float = 0
        for frame_time in self.frame_list:
            total_variance += abs(frame_time - average_time)

        # average variance
        average_variance: float = total_variance / frame_count if frame_count > 0 else 0
        average_variance_perc: float = 100 * (average_variance / average_time) if average_time > 0 else 0

        # frame variance
        frame_variance: float = abs(frame_time - average_time)
        frame_variance_perc = 100 * (frame_variance / average_time) if average_time > 0 else 0
        
        # \033[0m = end coloring
        # \033[91m = red
        # \033[92m = green
        # \033[93m = yellow
        # \033[94m = blue
        print('{:.7f}s average frame time (\033[94m{}\033[0m frames)'.format(average_time, frame_count))
        print('{:.7f}s frame time (\033[94m{}\033[0m motors changed)'.format(frame_time, self.motors_changed_this_cycle))
        text_color = '\033[91m' if frame_variance > average_variance else '\033[92m' # red if variance was higher than average
        print('{:.7f}s frame variance   {}{:.1f}%\033[0m'.format(frame_variance, text_color, frame_variance_perc))
        print('{:.7f}s average variance \033[33m{:.1f}%\033[0m'.format(average_variance, average_variance_perc))

        # update high/low
        if frame_count == 1:
            self.frame_high = frame_time
            self.frame_low = frame_time
            print('Slowest Frame: \033[33m{:.7f}s\033[0m'.format(self.frame_high))
            print('Fastest Frame: \033[33m{:.7f}s\033[0m'.format(self.frame_low))
        else:
            if frame_time > self.frame_high:
                precent_change: float = 100 * (frame_time - self.frame_high) / self.frame_high if self.frame_high > 0 else 0
                self.frame_high = frame_time
                # a new high gets colored
                print('Slowest Frame: \033[91m{:.7f}s\033[0m  (\033[91m{:.1f}%\033[0m slower)'.format(self.frame_high, precent_change))
                print('Fastest Frame: {:.7f}s'.format(self.frame_low))
            elif frame_time < self.frame_low:
                precent_change: float = 100 * (self.frame_low - frame_time) / self.frame_low if self.frame_low > 0 else 0
                self.frame_low = frame_time
                # a new low gets colored
                print('Slowest Frame: {:.7f}s'.format(self.frame_high))
                print('Fastest Frame: \033[91m{:.7f}s\033[0m  (\033[91m{:.1f}%\033[0m faster)'.format(self.frame_low, precent_change))
            else:
                print('Slowest Frame: {:.7f}s'.format(self.frame_high))
                print('Fastest Frame: {:.7f}s'.format(self.frame_low))
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

    def motoron(self, percent):
        """
        Takes percent and turns on to the percent parameter
        :param percent(int): Percent motors are on
        :return:
        """
        for y in range(1, 19):
            for x in range(A, L + 1):
                self.mtr[x][y].percent(percent)

    def testmtrs(self):
        """
        Turns on selected range of motors to 25% power
        :return:
        """
        for y in range(10, 14):
            for x in range(E, H + 1):
                self.mtr[x][y].percent(30)

    def testeachmotor(self):
        for x in range(1, 13):
            for y in range(1, 19):
                self.mtr[x][y].percent(30)
                self.status()
                time.sleep(2)
                self.stop()
                self.status()
                time.sleep(1)

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

    def stop(self):
        """
        Turns all motors off
        :return:
        """
        self.pattern_active = False
        for y in range(1, 19):
            for x in range(A, L + 1):
                self.mtr[x][y].percent(0)
                self.mtr[x][y].increasing = False
                self.mtr[x][y].decreasing = False
