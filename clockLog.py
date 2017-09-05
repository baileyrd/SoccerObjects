from datetime import date
from game import Game

class ClockLog(object):
    """docstring for ClockLog"""
    def __init__(self, arg):
        super(ClockLog, self).__init__()
        self.arg = arg
        self._clockAction = ""
        self._game = Game()
        self._clockDate = date.today()
