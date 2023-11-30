"""Wrapper for a Starcraft Order reference.

"""


class SCOrder:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


ATTACK = SCOrder('attack')
MOVE = SCOrder('move')
PATROL = SCOrder('patrol')
