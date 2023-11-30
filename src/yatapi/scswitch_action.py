"""Wrapper for a Starcraft Switch Action reference.

"""


class SCSwitchAction:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


CLEAR = SCSwitchAction('clear')
RANDOMIZE = SCSwitchAction('randomize')
SET = SCSwitchAction('set')
TOGGLE = SCSwitchAction('toggle')
