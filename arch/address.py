class Address(object):
    """docstring for Address"""
    def __init__(self, arg):
        super(Address, self).__init__()
        self.arg = arg
        self._streetNumber = ""
        self._streetAddress = ""
        self._city = ""
        self._state = ""
        self._zip = ""
