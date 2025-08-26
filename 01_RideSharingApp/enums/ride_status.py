from enum import Enum

class RideStatus(Enum):
    REQUESTED = 1
    ONGOING = 2
    COMPLETED = 3
    CANCELLED = 4
