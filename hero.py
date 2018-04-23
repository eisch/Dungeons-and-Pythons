from weapon import Weapon


class Hero:
    def __init__(self, name="Bron",\
                 title="Dragonslayer", health=100,\
                 mana=100, mana_regeneration_rate=2):
        assert type(name) is str
        assert type(title) is str
        assert type(health) is float or type(health) is int
        assert type(mana) is float or type(mana) is int
        assert type(mana_regeneration_rate) is float or\
               type(mana_regeneration_rate) is int
        if health < 0 or mana < 0 or mana_regeneration_rate < 0:
            raise ValueError
        if health > 100 or mana > 100:
            raise ValueError
        self.name = name
        self.title = title
        self._health = health
        self._mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self._weapon = None
        self._spell = None

    def known_as(self):
        return f"{self.name} the {self.title}"

    def is_alive(self):
        return self._health > 0

    def can_cast(self):
        return self._mana > 0

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        if self.get_health() + healing_points > 100:
            return False
        self._health += healing_points
        return True

    def take_mana(self, mana_points):
        if self.get_mana() + self.mana_regeneration_rate + mana_points < 100:
            self._mana = self.get_mana() + self.mana_regeneration_rate + mana_points

    def attack(self, by):
        if self._weapon is None and self._spell is None:
            return 0
        if by == "weapon":
            return self._weapon.damage
        # if by == "magic":
        #     return self._spell.damage

    def equip(self, weapon):
        assert type(weapon) is Weapon
        self._weapon = weapon

    def learn(self, spell):
        #assert type(spell) is Spell
        self._spell = spell

    def take_damage(self, damage_points):
        if self.get_health() - damage_points < 0:
            self._health = 0
        else:
            self._health -= damage_points

