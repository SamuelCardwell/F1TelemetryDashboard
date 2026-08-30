# Not in use for now
# If more information is needed that is not within fastf1 data objects then the class will be used

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
        self.laps.append(lap)
        # more stuff
