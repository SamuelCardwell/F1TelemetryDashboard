# Not in use for now
# If more information is needed that is not within fastf1 data objects then the class will be used

# name
# initials
# number
# team
# champ points
# position
# tires
# average lap time
# last lap time
# gap forward
# gap backward

from dataclasses import dataclass, field
from typing import List

@dataclass
class Driver:
    name: str