# -*- coding: utf-8 -*-
# Grid size
MOTORGRIDXSIZE = 12
MOTORGRIDYSIZE = 18


class Pattern:
    def __init__(self, name: str = "", intervals_per_second: int = 4, percent_power: int = 100, start_power: int = 9, max_power: int = 24, interval_power: int = 3, hold: int = 0, reverse: bool = False, sequence: str = ""):
        self.name = name
        self.intervals_per_second: int = intervals_per_second  # default time per frame
        self.percent_power: int = percent_power # default percentage power
        self.start_power: int = start_power# default start power
        self.max_power: int = max_power # default max power
        self.interval_power: int = interval_power # default rate of change
        self.hold: int = hold # when set to 0/ false by default
        self.reverse: bool = reverse
        self.sequence: str = sequence # default sequence

