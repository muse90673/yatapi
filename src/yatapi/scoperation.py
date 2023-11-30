"""Wrapper for a Starcraft Operation reference.

"""


class SCOperation:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


ADD: SCOperation = SCOperation('Add')
SET_TO: SCOperation = SCOperation('Set To')
SUBTRACT: SCOperation = SCOperation('Subtract')
