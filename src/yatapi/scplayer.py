"""Wrapper for a Starcraft Player reference.

"""

import re

DIGITS = re.compile(r'[0-9+]')


class SCPlayer:
    def __init__(self, value: str):
        self.value = value

    def to_int(self) -> int:
        return int(DIGITS.search(self.value).group())

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return self.value


ALL_PLAYERS: SCPlayer = SCPlayer('"All players"')
ALLIES: SCPlayer = SCPlayer('"Allies"')
CURRENT_PLAYER: SCPlayer = SCPlayer('"Current Player"')
FOES: SCPlayer = SCPlayer('"Foes"')
PLAYER_1: SCPlayer = SCPlayer('"Player 1"')
PLAYER_2: SCPlayer = SCPlayer('"Player 2"')
PLAYER_3: SCPlayer = SCPlayer('"Player 3"')
PLAYER_4: SCPlayer = SCPlayer('"Player 4"')
PLAYER_5: SCPlayer = SCPlayer('"Player 5"')
PLAYER_6: SCPlayer = SCPlayer('"Player 6"')
PLAYER_7: SCPlayer = SCPlayer('"Player 7"')
PLAYER_8: SCPlayer = SCPlayer('"Player 8"')
PLAYER_9: SCPlayer = SCPlayer('"Player 9"')
PLAYER_10: SCPlayer = SCPlayer('"Player 10"')
PLAYER_11: SCPlayer = SCPlayer('"Player 11"')
PLAYER_12: SCPlayer = SCPlayer('"Player 12"')
