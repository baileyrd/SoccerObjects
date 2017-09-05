from logAttribute import LogAttribute
from logType import LogType
from game import Game
from side import Side
from teamPlayer import TeamPlayer


class GameLog(object):
    """docstring for GameLog"""
    def __init__(self, arg):
        super(GameLog, self).__init__()
        self.arg = arg
        self._logAttributes = LogAttribute()
        self._logEmpty
        self._logType = LogType()
        self._game = Game()
        self._side = Side()
        self._teamPlayer = TeamPlayer()
        self._logDate
        self._logMinutes
