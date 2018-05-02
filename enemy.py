class Enemy:
    def __init__(self, health=100, mana=100, damage=20):
        if type(health) is not float and type(health) is not int:
            raise TypeError
        if type(mana) is not float and type(mana) is not int:
            raise TypeError
        if type(damage) is not float and type(damage) is not int:
            raise TypeError
        if ((health < 0 or health > 100) or
            (mana < 0 or mana > 100) or
                (damage < 0 or damage > 100)):
            raise ValueError
        self.health = health
        self.mana = mana
        self.damage = damage

    def is_alive(self):
        return self.health > 0

    def can_cast(self, spell):
        return self.mana >= spell.mana_cost

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_damage(self, damage_points):
        self.health = max(0, self.health - damage_points)

    def take_healing(self, healing_points):
        if self.is_alive():
            self.health = min(100, self.health + healing_points)
            return True
        return False

    def take_mana(self, mana_points):
        self.mana = min(self.mana_save, self.mana + mana_points)

    def attack(self):
        return self.damage
