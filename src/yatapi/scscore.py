"""Wrapper for a Starcraft Score reference.

"""


class SCScore:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


BUILDINGS: SCScore = SCScore('Buildings')
CUSTOM: SCScore = SCScore('Custom')
KILLS: SCScore = SCScore('Kills')
KILLS_AND_RAZINGS: SCScore = SCScore('Kills and razings')
RAZINGS: SCScore = SCScore('Razings')
TOTAL: SCScore = SCScore('Total')
UNITS: SCScore = SCScore('Units')
UNITS_AND_BUILDINGS: SCScore = SCScore('Units and buildings')
