# race name
# race number (first, second, ...)
# track map file
# track length
# finish positions
# pole lap time
# fastest lap
#

from dataclasses import dataclass, field
from typing import Dict

from driver import Driver
from lap import Lap

@dataclass
class Race:
    name: str
    track_map_file: str
    drivers: Dict[str, Driver] = field(default_factory=dict)
    laps: list = field(default_factory=list)

    def add_lap(self, lap: Lap):
        self.lap.append(lap)
        # more stuff