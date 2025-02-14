"""Wrapper for a Starcraft Quantifier reference.

"""


class SCQuantifier:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


AT_LEAST: SCQuantifier = SCQuantifier('At least')
AT_MOST: SCQuantifier = SCQuantifier('At most')
EXACTLY: SCQuantifier = SCQuantifier('Exactly')
