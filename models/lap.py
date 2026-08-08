from dataclasses import dataclass, feild

@dataclass
class Lap:
    number: int
    time: float
    outlap: bool
    inlap: bool