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

    def can_cast(self):
        return self.mana > 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_damage(self, damage):
        self.health -= damage

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        else:
            if self.health + healing_points > 100:
                self.health = 100
            else:
                self.health += healing_points
            return True

    def take_mana(self, mana_points):
        if self.mana + mana_points > 100:
            self.mana = 100
        else:
            self.mana += mana_points

    def attack(self):
        return self.damage
