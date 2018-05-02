from weapon import Weapon, Spell


class Hero:
    def __init__(self, name="Bron", title="Dragonslayer", health=100,
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
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.mana_save = mana
        self.weapon = None
        self.spell = None
        self.weapon_inventory = [Weapon('The Axe Of Destiny', 20)]
        self.spell_inventory = [Spell(name='Fireball',
                                      damage=30,
                                      mana_cost=50,
                                      cast_range=2)]

    def known_as(self):
        return f"{self.name} the {self.title}"

    def is_alive(self):
        return self.health > 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def can_cast(self, spell):
        return spell.mana_cost <= self.mana

    def take_damage(self, damage_points):
        self.health = max(0, self.health - damage_points)

    def take_healing(self, healing_points):
        if self.is_alive():
            self.health = min(100, self.health + healing_points)
            return True
        return False

    def take_mana(self, mana_points):
        self.mana = min(self.mana_save, self.mana + mana_points)

    def equip(self, weapon):
        if weapon in self.weapon_inventory:
            self.weapon = weapon
        else:
            print('You do not have that weapon in your weapon inventory!')

    def learn(self, spell):
        if spell in self.spell_inventory:
            self.spell = spell
        else:
            print("You do not have that spell in your spell inventory! ")

    def attack(self, by):
        if by == 'weapon':
            return self.weapon.damage if self.weapon is not None else 0
        if by == 'spell':
            return self.spell.damage if self.damage is not None else 0

    def get_weapon_inventory(self):
        for weapon in self.weapon_inventory:
            print(weapon)

    def get_spell_inventory(self):
        for spell in self.spell_inventory:
            print(spell)
