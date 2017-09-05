from person import Person


class Player(Person):
    """docstring for Player"""
    def __init__(self, arg):
        super(Player, self).__init__()
        self.arg = arg
        self._jersyNumber = ""

