# -*- coding: utf-8 -*-
# Grid size
MOTORGRIDXSIZE = 12
MOTORGRIDYSIZE = 18


class Pattern:
    def __init__(self) -> None:
        self.name = ""
        self.time = 0.1  # default time per frame
        self.percent_power = 100 # default percentage power
        self.start_power = 20 # default start power
        self.max_power = 50 # default max power
        self.rate_of_change = 4 # default rate of change
        self.hold = 3 # when set to 0/ false by default
        self.sequence = "" # default sequence
        pass

