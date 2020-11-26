class Characters:
    def __init__(self, _name, _strength):
        self.name = _name
        self.strength = _strength

    def getName(self):
        return self._name

    def setName(self, _name):
        if type(_name) != str:
            print("type ERROR")
        else:
            self._name = _name

    def getStrength(self):
        return self._strength

    def setStrength(self, _strength):
        if type(_strength) != float:
            print("type ERROR")
        elif _strength > 5.0:
            self._strength = 5.0
        elif _strength < 0.0:
            self._strength = 0.0
        else:
            self._strength = _strength

    def fight(self, other):
        if other > self:
            if other._strength <= 4.0:
                other._strength = other._strength + 1
                print(other)
            else:
                other._strength = 5.0
                print(other)
        elif self > other:
            if self._strength <= 4.0:
                self._strength = self._strength + 1
                print(self)
            else:
                self._strength = 5.0
                print(self)
        else:
            if self._strength >= 0.5 and other._strength >= 0.5:
                self._strength = self._strength - 0.5
                other._strength = other._strength - 0.5
            elif self._strength < 0.5:
                self._strength = 0.0
            elif other._strength < 0.5:
                self._strength = 0.0

    def __gt__(self, other):
        if self._strength > other.strength:
            return True
        return False

    def __str__(self):
        return "%s %.1f" % (self._name, self._strength)

    name = property(getName, setName)
    strength = property(getStrength, setStrength)


class Orc(Characters):
    def __init__(self, _name, _strength, _weapon):
        super().__init__(_name, _strength)
        self.weapon = _weapon

    def getWeapon(self):
        return self._weapon

    def setWeapon(self, _weapon):
        if type(_weapon) != bool:
            print("type ERROR")
        else:
            self._weapon = _weapon

    def __gt__(self, other):
        if isinstance(self, Orc) and isinstance(other, Orc):
            if self._weapon == True and other.weapon == False:
                return True
            elif self._weapon == False and other.weapon == True:
                return False
            else:
                return super(Orc, self).__gt__(other)
        else:
            return super(Orc, self).__gt__(other)

    def __str__(self):
        return super(Orc, self).__str__() + " %s" % self._weapon

    weapon = property(getWeapon, setWeapon)


class Humans(Characters):
    def __init__(self, _name, _strength, _kingdom):
        super().__init__(_name, _strength)
        self.kingdom = _kingdom

    def getKingdom(self):
        return self._kingdom

    def setKingdom(self, _kingdom):
        if type(_kingdom) != str:
            print("type ERROR")
        else:
            self._kingdom = _kingdom

    def fight(self, other):
        if isinstance(self, Humans) and isinstance(other, Humans):
            print("Fight ERROR")
        else:
            super(Humans, self).fight(other)

    def __str__(self):
        return super(Humans, self).__str__() + " %s" % self._kingdom

    kingdom = property(getKingdom, setKingdom)


class Archer(Humans):
    def __init__(self, _name, _strength, _kingdom):
        super().__init__(_name, _strength, _kingdom)


class Knight(Humans):
    def __init__(self, _name, _strength, _kingdom, archers_list):
        super().__init__(_name, _strength, _kingdom)
        if type(archers_list) != list:
            print("archers list ERROR")
        else:
            self.archers_list = archers_list

    def getArcher_list(self):
        return self._archers_list

    def setArcher_list(self, val):
        self._archers_list = []
        for archer in val:
            if not isinstance(archer, Archer):
                print("archers list ERROR")
            elif archer.kingdom == self._kingdom:
                self._archers_list.append(archer)

    def __str__(self):
        string_archer_list = '['
        for item in self._archers_list:
            string_archer_list += item.__str__()
            current_archer = self._archers_list.index(item)
            if current_archer != len(self._archers_list) - 1:
                string_archer_list += ", "
        string_archer_list += ']'
        return super().__str__() + string_archer_list

    archers_list = property(getArcher_list, setArcher_list)
