"""Wrapper for a Starcraft Switch State reference.

"""


class SCSwitchState:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


CLEARED: SCSwitchState = SCSwitchState('not set')
SET: SCSwitchState = SCSwitchState('set')
