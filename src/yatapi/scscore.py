"""Wrapper for a Starcraft Score reference.

"""


class SCScore:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


BUILDINGS = SCScore('Buildings')
CUSTOM = SCScore('Custom')
KILLS = SCScore('Kills')
KILLS_AND_RAZINGS = SCScore('Kills and razings')
RAZINGS = SCScore('Razings')
TOTAL = SCScore('Total')
UNITS = SCScore('Units')
UNITS_AND_BUILDINGS = SCScore('Units and buildings')
