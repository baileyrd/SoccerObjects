from communication import Communication

class CommunicationItem(object):
    """docstring for CommunicationItem"""
    def __init__(self, arg):
        super(CommunicationItem, self).__init__()
        self.arg = arg
        self._communicationType = ""
        self._communication = Communication()
        self._contact = ""
