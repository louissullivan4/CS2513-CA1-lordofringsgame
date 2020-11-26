class Orc:
    def __init__(self, _name, _strength, _weapon):
        self._name = _name
        self._strength = _strength
        self._weapon = _weapon

    def getName(self):
        return self._name

    def setName(self, _name):
        if type(_name) != str:
            print("Type ERROR")
        else:
            self._name = _name

    def getStrength(self):
        return self._strength

    def setStrength(self, _strength):
        if type(_strength) != float:
            print("Type ERROR")
        elif _strength > 5:
            self._strength = 5.0
        elif _strength < 0:
            self._strength = 0.0
        else:
            self._strength = self._strength

    def getWeapon(self):
        return self._weapon

    def setWeapon(self, _weapon):
        if type(_weapon) != bool:
            print("Type ERROR")
        else:
            self._weapon = _weapon

    def fight(self, other):
        if other > self:
            other._strength = other._strength + 1
            print(other)
        elif self > other:
            self._strength = self._strength + 1
            print(self)
        else:
            self._strength = self._strength - 0.5
            other._strength = other._strength - 0.5

    def __gt__(self, other):
        if self._weapon == True and other.weapon == False:
            return True
        elif self._weapon == False and other.weapon == True:
            return False
        else:
            if self._strength > other.strength:
                return True
            return False

    def __str__(self):
        return "%s %.1f %s" % (self._name, self._strength, self._weapon)

    name = property(getName, setName)
    strength = property(getStrength, setStrength)
    weapon = property(getWeapon, setWeapon)
