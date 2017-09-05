from team import Team
from teamEvent import TeamEvent
from datetime import date

class Communication(object):
    """docstring for Communication"""
    def __init__(self, arg):
        super(Communication, self).__init__()
        self.arg = arg
        self._reason = ""
        self._team = Team()
        self._teamEvent = TeamEvent()
        self._date  = date.today()
        self._text = ""

