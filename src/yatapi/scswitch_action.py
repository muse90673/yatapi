"""Wrapper for a Starcraft Switch Action reference.

"""


class SCSwitchAction:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


CLEAR: SCSwitchAction = SCSwitchAction('clear')
RANDOMIZE: SCSwitchAction = SCSwitchAction('randomize')
SET: SCSwitchAction = SCSwitchAction('set')
TOGGLE: SCSwitchAction = SCSwitchAction('toggle')
