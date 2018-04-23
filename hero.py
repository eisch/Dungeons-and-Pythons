class Hero:
    def __init__(self, name="Bron",\
                 title="Dragonslayer", health=100,\
                 mana=100, mana_regeneration_rate=2):
        assert type(name) is str
        assert type(title) is str
        assert type(health) is float or type(health) is int
        assert type(mana) is float or type(mana) is int
        assert type(mana_regeneration_rate) is float or type(mana_regeneration_rate) is int
        if health < 0 or mana < 0 or mana_regeneration_rate < 0:
            raise ValueError
        if health > 100 or mana > 100:
            raise ValueError
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return f"{self.name} the {self.title}"

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        return self.mana > 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing():
        pass

    def take_mana():
        pass

    def attack():
        pass

    def take_damage(damage):
        pass

