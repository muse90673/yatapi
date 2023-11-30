"""Wrapper for a Starcraft State reference.

"""


class SCState:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


DISABLED: SCState = SCState('disabled')
ENABLED: SCState = SCState('enabled')
TOGGLE: SCState = SCState('toggle')
