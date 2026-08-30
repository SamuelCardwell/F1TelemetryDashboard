# Not in use for now
# If more information is needed that is not within fastf1 data objects then the class will be used

from dataclasses import dataclass, field

@dataclass
class Lap:
    number: int
    time: float
    outlap: bool
    inlap: bool
