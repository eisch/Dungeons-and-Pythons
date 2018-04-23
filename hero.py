class Hero:
    def __init__(self, name="Bron",title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2):
        assert type(name) is str
        assert type(title) is str
        assert type(health) is int
        assert type(mana) is int
        assert type(mana_regeneration_rate) is int
        if health < 0 or mana < 0 or mana_regeneration_rate < 0:
            raise ValueError
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
