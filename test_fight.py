import unittest
from fight import Fight
from hero import Hero
from enemy import Enemy
from weapon_and_spell import Weapon, Spell


class FightTests(unittest.TestCase):
    def setUp(self):
        self.weapon = Weapon(name="The Axe of Destiny", damage=20)
        self.spell = Spell(name="Fireball", damage=30,
                           mana_cost=50, cast_range=2)
        self.hero = Hero(name="Bron", title="Dragonslayer",
                         health=100, mana=100, mana_regeneration_rate=2)
        self.enemy_to_die = Enemy(health=100, mana=100, damage=20)
        self.enemy_to_win = Enemy(health=100, mana=100, damage=50)
        self.hero.equip(self.weapon)
        self.hero.learn(self.spell)
        self.first_fight = Fight(self.hero, self.enemy_to_die)
        self.second_fight = Fight(self.hero, self.enemy_to_win)

    def test_init_for_type_error_for_hero(self):
        with self.assertRaises(TypeError):
            Fight(self.weapon, self.enemy_to_win)

    def test_init_for_type_error_for_enemy(self):
        with self.assertRaises(TypeError):
            Fight(self.hero, self.spell)

    def test_fight_method_where_hero_wins(self):
        self.assertTrue(self.first_fight.fight())

    def test_fight_method_where_enemy_wins(self):
        self.assertFalse(self.second_fight.fight())


if __name__ == "__main__":
    unittest.main()
