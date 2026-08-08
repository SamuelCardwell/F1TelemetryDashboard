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