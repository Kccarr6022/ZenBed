# -*- coding: utf-8 -*-
# Grid size
MOTORGRIDXSIZE = 12
MOTORGRIDYSIZE = 18


class Pattern:
    def __init__(self) -> None:
        self.name = ""
        self.intervals_per_second: int = 5  # default time per frame
        self.percent_power: int = 100 # default percentage power
        self.start_power: int = 20 # default start power
        self.max_power: int = 50 # default max power
        self.interval_power: int = 4 # default rate of change
        self.hold: int = 0 # when set to 0/ false by default
        self.reverse: bool = False
        self.sequence: str = "" # default sequence

