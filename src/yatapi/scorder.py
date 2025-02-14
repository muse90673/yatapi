"""Wrapper for a Starcraft Order reference.

"""


class SCOrder:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


ATTACK: SCOrder = SCOrder('attack')
MOVE: SCOrder = SCOrder('move')
PATROL: SCOrder = SCOrder('patrol')
