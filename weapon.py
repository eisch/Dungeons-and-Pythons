class Weapon:
    def __init__(self, name="", damage=20):
        if type(name) is not str:
            raise TypeError
        if type(damage) is not float and type(damage) is not int:
            raise TypeError
        if damage < 0 or damage > 100:
            raise ValueError

        self.name = name
        self.damage = damage

    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage


class Spell:
    def __init__(self, name="", damage=30, mana_cost=50, cast_range=2):
        if type(name) is not str:
            raise TypeError
        if type(damage) is not float and type(damage) is not int:
            raise TypeError
        if damage < 0 or damage > 100:
            raise ValueError
        if type(mana_cost) is not float and type(mana_cost) is not int:
            raise TypeError
        if mana_cost < 0 or mana_cost > 100:
            raise ValueError
        if type(cast_range) is not int:
            raise TypeError
        if cast_range < 0:
            raise ValueError
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage

    def get_mana_cost(self):
        return self.mana_cost

    def get_cast_range(self):
        return self.cast_range
