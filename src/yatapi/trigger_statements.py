"""

"""

__all__ = (
    'Statement', 'Condition', 'Action', 'Accumulate', 'Always', 'Bring', 'Command',
    'CommandTheLeast', 'CommandTheLeastAt', 'CommandTheMost', 'CommandsTheMostAt',
    'CountdownTimer', 'Deaths', 'ElapsedTime', 'HighestScore', 'Kill', 'LeastKills',
    'LeastResources', 'LowestScore', 'MostKills', 'MostResources', 'Never', 'Opponents',
    'Score', 'Switch', 'CenterView', 'Comment', 'CreateUnit', 'CreateUnitWithProperties',
    'Defeat', 'DisplayTextMessage', 'Draw', 'GiveUnitsToPlayer', 'KillUnit', 'KillUnitAtLocation',
    'LeaderBoardControl', 'LeaderBoardControlAtLocation', 'LeaderBoardGreed', 'LeaderBoardKills',
    'LeaderBoardPoints', 'LeaderBoardResources', 'LeaderboardComputerPlayers', 'LeaderboardGoalControl',
    'LeaderboardGoalControlAtLocation', 'LeaderboardGoalKills', 'LeaderboardGoalPoints',
    'LeaderboardGoalResources', 'MinimapPing', 'ModifyUnitEnergy', 'ModifyUnitHangerCount',
    'ModifyUnitHitPoints', 'ModifyUnitResourceAmount', 'ModifyUnitShieldPoints', 'MoveLocation',
    'MoveUnit', 'MuteUnitSpeech', 'Order', 'PauseGame', 'PauseTimer', 'PlayWav', 'PreserveTrigger',
    'RemoveUnit', 'RemoveUnitAtLocation', 'RunAiScript', 'RunAiScriptAtLocation', 'SetAllianceStatus',
    'SetCountdownTimer', 'SetDeaths', 'SetDoodadState', 'SetInvincibility', 'SetMissionObjectives',
    'SetNextScenario', 'SetResources', 'SetScore', 'SetSwitch', 'TalkingPortrait', 'Transmission',
    'UnmuteUnitSpeech', 'UnpauseGame', 'UnpauseTimer', 'Victory', 'Wait'
)

import abc
import inspect
import re
import typing

from yatapi.scalliance import SCAlliance
from yatapi.sccount import SCCount
from yatapi.scoperation import SCOperation
from yatapi.scorder import SCOrder
from yatapi.scplayer import SCPlayer
from yatapi.scquantifier import SCQuantifier
from yatapi.scresource import SCResource
from yatapi.scscore import SCScore
from yatapi.scscript import SCScript
from yatapi.scstate import SCState
from yatapi.scswitch_action import SCSwitchAction
from yatapi.scswitch_state import SCSwitchState
from yatapi.scunit import SCUnit
from yatapi.scvisibility import ALWAYS_DISPLAY


class Statement(abc.ABC):
    _trigedit_name = 'statement'
    _quoted_fields = frozenset()

    def __init__(self):
        pass

    def _is_quoted(self, value):
        return True if re.search(r'^".+?"$', value) is not None else False

    def _quote_value(self, value):
        return '"{}"'.format(value)

    def _get_values(self, pretty=False) -> typing.List:
        """Extracts the value of each statement argument in order as determined by the `__init__` method.

        :return: a list of values associated with the syntax of the corresponding TrigEdit statement
        :rtype: list
        """
        values = []
        for arg in inspect.getfullargspec(self.__init__).args:
            if arg != 'self':
                value = getattr(self, arg)
                if arg in self.__class__._quoted_fields and type(value) == str:
                    if not self._is_quoted(value):
                        value = self._quote_value(value)
                if pretty:
                    values.append('{}={}'.format(arg, value if type(value) == str else str(value)))
                else:
                    values.append(value if type(value) == str else str(value))
        return values

    def compile(self, pretty=False) -> str:
        """Compiles the action/condition into format usable by SCMDraft TrigEdit.

        :param pretty: whether to include name of each argument (cannot be used in TrigEdit); use for debugging
        :type pretty: bool
        :return: a string representing the TrigEdit format for the trigger action or condition
        :rtype: str
        """
        values = self._get_values(pretty=pretty)
        return '{}({});'.format(self.__class__._trigedit_name, ', '.join(values))

    def __repr__(self):
        return self.compile()


class Condition(Statement):
    _trigedit_name = 'condition'

    def __init__(self):
        super().__init__()
        self.type = self.__class__.__name__


class Action(Statement):
    _trigedit_name = 'action'

    def __init__(self):
        super().__init__()
        self.type = self.__class__.__name__


# actions and conditions go here
class Accumulate(Condition):
    _trigedit_name = "Accumulate"
    _quoted_fields = frozenset(["player"])

    def __init__(self, player: SCPlayer, quantifier: SCQuantifier, amount: int, resource: SCResource):
        super().__init__()
        self.player = player
        self.quantifier = quantifier
        self.amount = amount
        self.resource = resource


class Always(Condition):
    _trigedit_name = "Always"
    _quoted_fields = frozenset()

    def __init__(self):
        super().__init__()


class Bring(Condition):
    _trigedit_name = "Bring"
    _quoted_fields = frozenset(["player", "unit", "location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, location: str, quantifier: SCQuantifier, count: int):
        super().__init__()
        self.player = player
        self.unit = unit
        self.location = location
        self.quantifier = quantifier
        self.count = count


class Command(Condition):
    _trigedit_name = "Command"
    _quoted_fields = frozenset(["player", "unit"])

    def __init__(self, player: SCPlayer, unit: SCUnit, quantifier: SCQuantifier, count: int):
        super().__init__()
        self.player = player
        self.unit = unit
        self.quantifier = quantifier
        self.count = count


class CommandTheLeast(Condition):
    _trigedit_name = "Command the Least"
    _quoted_fields = frozenset(["unit"])

    def __init__(self, unit: SCUnit):
        super().__init__()
        self.unit = unit


class CommandTheLeastAt(Condition):
    _trigedit_name = "Command the Least At"
    _quoted_fields = frozenset(["unit", "location"])

    def __init__(self, unit: SCUnit, location: str):
        super().__init__()
        self.unit = unit
        self.location = location


class CommandTheMost(Condition):
    _trigedit_name = "Command the Most"
    _quoted_fields = frozenset(["unit"])

    def __init__(self, unit: SCUnit):
        super().__init__()
        self.unit = unit


class CommandsTheMostAt(Condition):
    _trigedit_name = "Commands the Most At"
    _quoted_fields = frozenset(["unit", "location"])

    def __init__(self, unit: SCUnit, location: str):
        super().__init__()
        self.unit = unit
        self.location = location


class CountdownTimer(Condition):
    _trigedit_name = "Countdown Timer"
    _quoted_fields = frozenset()

    def __init__(self, quantifier: SCQuantifier, seconds: int):
        super().__init__()
        self.quantifier = quantifier
        self.seconds = seconds


class Deaths(Condition):
    _trigedit_name = "Deaths"
    _quoted_fields = frozenset(["player", "unit"])

    def __init__(self, player: SCPlayer, unit: SCUnit, quantifier: SCQuantifier, count: int):
        super().__init__()
        self.player = player
        self.unit = unit
        self.quantifier = quantifier
        self.count = count


class ElapsedTime(Condition):
    _trigedit_name = "Elapsed Time"
    _quoted_fields = frozenset()

    def __init__(self, quantifier: SCQuantifier, seconds: int):
        super().__init__()
        self.quantifier = quantifier
        self.seconds = seconds


class HighestScore(Condition):
    _trigedit_name = "Highest Score"
    _quoted_fields = frozenset()

    def __init__(self, score: SCScore):
        super().__init__()
        self.score = score


class Kill(Condition):
    _trigedit_name = "Kill"
    _quoted_fields = frozenset(["player", "unit"])

    def __init__(self, player: SCPlayer, unit: SCUnit, quantifier: SCQuantifier, count: int):
        super().__init__()
        self.player = player
        self.unit = unit
        self.quantifier = quantifier
        self.count = count


class LeastKills(Condition):
    _trigedit_name = "Least Kills"
    _quoted_fields = frozenset(["unit"])

    def __init__(self, unit: SCUnit):
        super().__init__()
        self.unit = unit


class LeastResources(Condition):
    _trigedit_name = "Least Resources"
    _quoted_fields = frozenset()

    def __init__(self, resource: SCResource):
        super().__init__()
        self.resource = resource


class LowestScore(Condition):
    _trigedit_name = "Lowest Score"
    _quoted_fields = frozenset()

    def __init__(self, score: SCScore):
        super().__init__()
        self.score = score


class MostKills(Condition):
    _trigedit_name = "Most Kills"
    _quoted_fields = frozenset(["unit"])

    def __init__(self, unit: SCUnit):
        super().__init__()
        self.unit = unit


class MostResources(Condition):
    _trigedit_name = "Most Resources"
    _quoted_fields = frozenset()

    def __init__(self, resource: SCResource):
        super().__init__()
        self.resource = resource


class Never(Condition):
    _trigedit_name = "Never"
    _quoted_fields = frozenset()

    def __init__(self):
        super().__init__()


class Opponents(Condition):
    _trigedit_name = "Opponents"
    _quoted_fields = frozenset(["player"])

    def __init__(self, player: SCPlayer, quantifier: SCQuantifier, count: int):
        super().__init__()
        self.player = player
        self.quantifier = quantifier
        self.count = count


class Score(Condition):
    _trigedit_name = "Score"
    _quoted_fields = frozenset(["player"])

    def __init__(self, player: SCPlayer, score: SCScore, quantifier: SCQuantifier, amount: int):
        super().__init__()
        self.player = player
        self.score = score
        self.quantifier = quantifier
        self.amount = amount


class Switch(Condition):
    _trigedit_name = "Switch"
    _quoted_fields = frozenset(["switch"])

    def __init__(self, switch: str, state: SCSwitchState):
        super().__init__()
        self.switch = switch
        self.state = state


class CenterView(Action):
    _trigedit_name = "Center View"
    _quoted_fields = frozenset(["location"])

    def __init__(self, location: str):
        super().__init__()
        self.location = location


class Comment(Action):
    _trigedit_name = "Comment"
    _quoted_fields = frozenset(["text"])

    def __init__(self, text: str):
        super().__init__()
        self.text = text


class CreateUnit(Action):
    _trigedit_name = "Create Unit"
    _quoted_fields = frozenset(["player", "unit", "location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, count: int, location: str):
        super().__init__()
        self.player = player
        self.unit = unit
        self.count = count
        self.location = location


class CreateUnitWithProperties(Action):
    _trigedit_name = "Create Unit with Properties"
    _quoted_fields = frozenset(["player", "unit", "location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, count: int, location: str, properties: int):
        super().__init__()
        self.player = player
        self.unit = unit
        self.count = count
        self.location = location
        self.properties = properties


class Defeat(Action):
    _trigedit_name = "Defeat"
    _quoted_fields = frozenset()

    def __init__(self):
        super().__init__()


class DisplayTextMessage(Action):
    _trigedit_name = "Display Text Message"
    _quoted_fields = frozenset(["text"])

    def __init__(self, text: str):
        super().__init__()
        self.text = text

    def _get_values(self, pretty=False):
        """ Override the method to fill in the unused parameter. """
        args = super()._get_values(pretty)
        return [str(ALWAYS_DISPLAY)] + args


class Draw(Action):
    _trigedit_name = "Draw"
    _quoted_fields = frozenset()

    def __init__(self):
        super().__init__()


class GiveUnitsToPlayer(Action):
    _trigedit_name = "Give Units to Player"
    _quoted_fields = frozenset(["from_player", "to_player", "unit", "location"])

    def __init__(self, from_player: SCPlayer, to_player: SCPlayer, unit: SCUnit, count: typing.Union[int, SCCount],
                 location: str):
        super().__init__()
        self.from_player = from_player
        self.to_player = to_player
        self.unit = unit
        self.count = count
        self.location = location


class KillUnit(Action):
    _trigedit_name = "Kill Unit"
    _quoted_fields = frozenset(["player", "unit"])

    def __init__(self, player: SCPlayer, unit: SCUnit):
        super().__init__()
        self.player = player
        self.unit = unit


class KillUnitAtLocation(Action):
    _trigedit_name = "Kill Unit At Location"
    _quoted_fields = frozenset(["player", "unit", "location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, count: typing.Union[int, SCCount], location: str):
        super().__init__()
        self.player = player
        self.unit = unit
        self.count = count
        self.location = location


class LeaderBoardControl(Action):
    _trigedit_name = "Leader Board Control"
    _quoted_fields = frozenset(["title", "unit"])

    def __init__(self, title: str, unit: SCUnit):
        super().__init__()
        self.title = title
        self.unit = unit


class LeaderBoardControlAtLocation(Action):
    _trigedit_name = "Leader Board Control At Location"
    _quoted_fields = frozenset(["title", "unit", "location"])

    def __init__(self, title: str, unit: SCUnit, location: str):
        super().__init__()
        self.title = title
        self.unit = unit
        self.location = location


class LeaderBoardGreed(Action):
    _trigedit_name = "Leaderboard Greed"
    _quoted_fields = frozenset()

    def __init__(self, amount: int):
        super().__init__()
        self.amount = amount


class LeaderBoardKills(Action):
    _trigedit_name = "Leader Board Kills"
    _quoted_fields = frozenset(["title", "unit"])

    def __init__(self, title: str, unit: SCUnit):
        super().__init__()
        self.title = title
        self.unit = unit


class LeaderBoardPoints(Action):
    _trigedit_name = "Leader Board Points"
    _quoted_fields = frozenset(["title"])

    def __init__(self, title: str, score: SCScore):
        super().__init__()
        self.title = title
        self.score = score


class LeaderBoardResources(Action):
    _trigedit_name = "Leader Board Resources"
    _quoted_fields = frozenset(["title"])

    def __init__(self, title: str, resource: SCResource):
        super().__init__()
        self.title = title
        self.resource = resource


class LeaderboardComputerPlayers(Action):
    _trigedit_name = "Leaderboard Computer Players"
    _quoted_fields = frozenset()

    def __init__(self, state: SCState):
        super().__init__()
        self.state = state


class LeaderboardGoalControl(Action):
    _trigedit_name = "Leaderboard Goal Control"
    _quoted_fields = frozenset(["title", "unit"])

    def __init__(self, title: str, unit: SCUnit, count: int):
        super().__init__()
        self.title = title
        self.unit = unit
        self.count = count


class LeaderboardGoalControlAtLocation(Action):
    _trigedit_name = "Leaderboard Goal Control At Location"
    _quoted_fields = frozenset(["title", "unit", "location"])

    def __init__(self, title: str, unit: SCUnit, count: int, location: str):
        super().__init__()
        self.title = title
        self.unit = unit
        self.count = count
        self.location = location


class LeaderboardGoalKills(Action):
    _trigedit_name = "Leaderboard Goal Kills"
    _quoted_fields = frozenset(["title", "unit"])

    def __init__(self, title: str, unit: SCUnit, count: int):
        super().__init__()
        self.title = title
        self.unit = unit
        self.count = count


class LeaderboardGoalPoints(Action):
    _trigedit_name = "Leaderboard Goal Points"
    _quoted_fields = frozenset(["title"])

    def __init__(self, title: str, score: SCScore, amount: int):
        super().__init__()
        self.title = title
        self.score = score
        self.amount = amount


class LeaderboardGoalResources(Action):
    _trigedit_name = "Leaderboard Goal Resources"
    _quoted_fields = frozenset(["title"])

    def __init__(self, title: str, amount: int, resource: SCResource):
        super().__init__()
        self.title = title
        self.amount = amount
        self.resource = resource


class MinimapPing(Action):
    _trigedit_name = "Minimap Ping"
    _quoted_fields = frozenset(["location"])

    def __init__(self, location: str):
        super().__init__()
        self.location = location


class ModifyUnitEnergy(Action):
    _trigedit_name = "Modify Unit Energy"
    _quoted_fields = frozenset(["player", "unit", "location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, percent: int, count: typing.Union[int, SCCount],
                 location: str):
        super().__init__()
        self.player = player
        self.unit = unit
        self.percent = percent
        self.count = count
        self.location = location


class ModifyUnitHangerCount(Action):
    _trigedit_name = "Modify Unit Hanger Count"
    _quoted_fields = frozenset(["player", "unit", "location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, hangar_count: int, unit_count: typing.Union[int, SCCount],
                 location: str):
        super().__init__()
        self.player = player
        self.unit = unit
        self.hangar_count = hangar_count
        self.unit_count = unit_count
        self.location = location


class ModifyUnitHitPoints(Action):
    _trigedit_name = "Modify Unit Hit Points"
    _quoted_fields = frozenset(["player", "unit", "location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, percent: int, count: typing.Union[int, SCCount],
                 location: str):
        super().__init__()
        self.player = player
        self.unit = unit
        self.percent = percent
        self.count = count
        self.location = location


class ModifyUnitResourceAmount(Action):
    _trigedit_name = "Modify Unit Resource Amount"
    _quoted_fields = frozenset(["player", "location"])

    def __init__(self, player: SCPlayer, amount: int, unit_count: typing.Union[int, SCCount], location: str):
        super().__init__()
        self.player = player
        self.amount = amount
        self.unit_count = unit_count
        self.location = location


class ModifyUnitShieldPoints(Action):
    _trigedit_name = "Modify Unit Shield Points"
    _quoted_fields = frozenset(["player", "unit", "location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, percent: int, count: typing.Union[int, SCCount],
                 location: str):
        super().__init__()
        self.player = player
        self.unit = unit
        self.percent = percent
        self.count = count
        self.location = location


class MoveLocation(Action):
    _trigedit_name = "Move Location"
    _quoted_fields = frozenset(["player", "unit", "unit_location", "location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, unit_location: str, location: str):
        super().__init__()
        self.player = player
        self.unit = unit
        self.unit_location = unit_location
        self.location = location


class MoveUnit(Action):
    _trigedit_name = "Move Unit"
    _quoted_fields = frozenset(["player", "unit", "from_location", "to_location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, count: typing.Union[int, SCCount], from_location: str,
                 to_location: str):
        super().__init__()
        self.player = player
        self.unit = unit
        self.count = count
        self.from_location = from_location
        self.to_location = to_location


class MuteUnitSpeech(Action):
    _trigedit_name = "Mute Unit Speech"
    _quoted_fields = frozenset()

    def __init__(self):
        super().__init__()


class Order(Action):
    _trigedit_name = "Order"
    _quoted_fields = frozenset(["player", "unit", "location", "destination"])

    def __init__(self, player: SCPlayer, unit: SCUnit, location: str, destination: str, order: SCOrder):
        super().__init__()
        self.player = player
        self.unit = unit
        self.location = location
        self.destination = destination
        self.order = order


class PauseGame(Action):
    _trigedit_name = "Pause Game"
    _quoted_fields = frozenset()

    def __init__(self):
        super().__init__()


class PauseTimer(Action):
    _trigedit_name = "Pause Timer"
    _quoted_fields = frozenset()

    def __init__(self):
        super().__init__()


class PlayWav(Action):
    _trigedit_name = "Play WAV"
    _quoted_fields = frozenset(["wav"])

    def __init__(self, wav: str):
        super().__init__()
        self.wav = wav

    def _get_values(self, pretty=False):
        """ Override the method to fill in the unused parameter. """
        args = super()._get_values(pretty)
        return args + ['0']


class PreserveTrigger(Action):
    _trigedit_name = "Preserve Trigger"
    _quoted_fields = frozenset()

    def __init__(self):
        super().__init__()


class RemoveUnit(Action):
    _trigedit_name = "Remove Unit"
    _quoted_fields = frozenset(["player", "unit"])

    def __init__(self, player: SCPlayer, unit: SCUnit):
        super().__init__()
        self.player = player
        self.unit = unit


class RemoveUnitAtLocation(Action):
    _trigedit_name = "Remove Unit At Location"
    _quoted_fields = frozenset(["player", "unit", "location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, count: typing.Union[int, SCCount], location: str):
        super().__init__()
        self.player = player
        self.unit = unit
        self.count = count
        self.location = location


class RunAiScript(Action):
    _trigedit_name = "Run AI Script"
    _quoted_fields = frozenset(["script"])

    def __init__(self, script: SCScript):
        super().__init__()
        self.script = script


class RunAiScriptAtLocation(Action):
    _trigedit_name = "Run AI Script At Location"
    _quoted_fields = frozenset(["script", "location"])

    def __init__(self, script: SCScript, location: str):
        super().__init__()
        self.script = script
        self.location = location


class SetAllianceStatus(Action):
    _trigedit_name = "Set Alliance Status"
    _quoted_fields = frozenset(["player"])

    def __init__(self, player: SCPlayer, alliance: SCAlliance):
        super().__init__()
        self.player = player
        self.alliance = alliance


class SetCountdownTimer(Action):
    _trigedit_name = "Set Countdown Timer"
    _quoted_fields = frozenset()

    def __init__(self, operation: SCOperation, seconds: int):
        super().__init__()
        self.operation = operation
        self.seconds = seconds


class SetDeaths(Action):
    _trigedit_name = "Set Deaths"
    _quoted_fields = frozenset(["player", "unit"])

    def __init__(self, player: SCPlayer, unit: SCUnit, operation: SCOperation, count: int):
        super().__init__()
        self.player = player
        self.unit = unit
        self.operation = operation
        self.count = count


class SetDoodadState(Action):
    _trigedit_name = "Set Doodad State"
    _quoted_fields = frozenset(["player", "unit", "location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, location: str, state: SCState):
        super().__init__()
        self.player = player
        self.unit = unit
        self.location = location
        self.state = state


class SetInvincibility(Action):
    _trigedit_name = "Set Invincibility"
    _quoted_fields = frozenset(["player", "unit", "location"])

    def __init__(self, player: SCPlayer, unit: SCUnit, location: str, state: SCState):
        super().__init__()
        self.player = player
        self.unit = unit
        self.location = location
        self.state = state


class SetMissionObjectives(Action):
    _trigedit_name = "Set Mission Objectives"
    _quoted_fields = frozenset(["text"])

    def __init__(self, text: str):
        super().__init__()
        self.text = text


class SetNextScenario(Action):
    _trigedit_name = "Set Next Scenario"
    _quoted_fields = frozenset(["scenario"])

    def __init__(self, scenario: str):
        super().__init__()
        self.scenario = scenario


class SetResources(Action):
    _trigedit_name = "Set Resources"
    _quoted_fields = frozenset(["player"])

    def __init__(self, player: SCPlayer, operation: SCOperation, amount: int, resource: SCResource):
        super().__init__()
        self.player = player
        self.operation = operation
        self.amount = amount
        self.resource = resource


class SetScore(Action):
    _trigedit_name = "Set Score"
    _quoted_fields = frozenset(["player"])

    def __init__(self, player: SCPlayer, operation: SCOperation, amount: int, score: SCScore):
        super().__init__()
        self.player = player
        self.operation = operation
        self.amount = amount
        self.score = score


class SetSwitch(Action):
    _trigedit_name = "Set Switch"
    _quoted_fields = frozenset(["switch"])

    def __init__(self, switch: str, action: SCSwitchAction):
        super().__init__()
        self.switch = switch
        self.action = action


class TalkingPortrait(Action):
    _trigedit_name = "Talking Portrait"
    _quoted_fields = frozenset(["unit"])

    def __init__(self, unit: SCUnit, milliseconds: int):
        super().__init__()
        self.unit = unit
        self.milliseconds = milliseconds


class Transmission(Action):
    _trigedit_name = "Transmission"
    _quoted_fields = frozenset(["text", "unit", "location", "wav"])

    def __init__(self, text: str, unit: SCUnit, location: str, operation: SCOperation, milliseconds: int, wav: str):
        super().__init__()
        self.text = text
        self.unit = unit
        self.location = location
        self.operation = operation
        self.milliseconds = milliseconds
        self.wav = wav

    def _get_values(self, pretty=False):
        """ Override the method to fill in the unused parameter. """
        args = super()._get_values(pretty)
        return [str(ALWAYS_DISPLAY)] + args + ['0']


class UnmuteUnitSpeech(Action):
    _trigedit_name = "Unmute Unit Speech"
    _quoted_fields = frozenset()

    def __init__(self):
        super().__init__()


class UnpauseGame(Action):
    _trigedit_name = "Unpause Game"
    _quoted_fields = frozenset()

    def __init__(self):
        super().__init__()


class UnpauseTimer(Action):
    _trigedit_name = "Unpause Timer"
    _quoted_fields = frozenset()

    def __init__(self):
        super().__init__()


class Victory(Action):
    _trigedit_name = "Victory"
    _quoted_fields = frozenset()

    def __init__(self):
        super().__init__()


class Wait(Action):
    _trigedit_name = "Wait"
    _quoted_fields = frozenset()

    def __init__(self, milliseconds: int):
        super().__init__()
        self.milliseconds = milliseconds


if __name__ == '__main__':
    pass
