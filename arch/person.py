class Person(object):
    """docstring for Person"""

    def __init__(self, firstName, lastName, gender, dateOfBirth):
        self.set_firstName(firstName)
        self.set_lastName(lastName)
        self.set_compositeName()
        self.set_gender(gender)
        self.set_dateOfBirth(dateOfBirth)
        self.set_age()

    def set_firstName(self, firstName):
        self._firstName = firstName

    def set_lastName(self, lastName):
        self._lastName = lastName

    def set_compositeName(self):
        self._compositeName = self._firstName + ' ' + self._lastName

    def set_gender(self, gender):
        self._gender = gender

    def set_dateOfBirth(self, dateOfBirth):
        self._dateOfBirth = dateOfBirth

    def set_age(self):
        pass
