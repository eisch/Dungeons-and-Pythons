class Weapon:
    def __init__(self, name, damage):
        assert type(name) is str
        assert type(damage) is int or type(damage) is float
        self.name = name
        self.damage = damage

    def __eq__(self, other):
        return self.name == other.name and self.damage == other.damage