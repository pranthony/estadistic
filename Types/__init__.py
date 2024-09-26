from enum import Enum

class FrequencyType(Enum):
    ABSOLUTE = 'absolute'
    RELATIVE = 'relative'
    ABSOLUTE_CUMULATIVE = 'absolute_cumulative'
    RELATIVE_CUMULATIVE = 'relative_cumulative'
    ABSOLUTE_CUMULATIVE_LT = 'absolute_ut'
    RELATIVE_CUMULATIVE_LT = 'relative_lt'