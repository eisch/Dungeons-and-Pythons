from hero import Hero
from enemy import Enemy
from weapon_and_spell import Weapon, Spell


class Fight:
    def __init__(self, hero, enemy):
        if type(hero) is not Hero:
            raise TypeError
        if type(enemy) is not Enemy:
            raise TypeError
        self.hero = hero
        self.enemy = enemy

    def fight(self):
        while self.hero.is_alive() and self.enemy.is_alive():
            if self.hero.is_alive():
                hero_weapon = self.hero.get_most_powerfull_weapon()
                self.enemy.take_damage(hero_weapon.get_damage())
                print(f"Hero casts a {hero_weapon.get_name()}, hits enemy for {hero_weapon.get_damage()} dmg. Enemy health is {self.enemy.get_health()}")

            if self.enemy.is_alive():
                self.hero.take_damage(self.enemy.attack())
                print(f"Enemy hits hero for {self.enemy.attack()} dmg. Hero health is {self.hero.get_health()}.")

        if not self.hero.is_alive():
            print()
            return False

        print("Enemy is dead!")
        return True 
