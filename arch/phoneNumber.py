class PhoneNumber(object):
    """docstring for PhoneNumber"""
    def __init__(self, arg):
        super(PhoneNumber, self).__init__()
        self.arg = arg
        self._phoneType = ""
        self._areaCode = ""
        self._exchange = ""
        self._number = ""

