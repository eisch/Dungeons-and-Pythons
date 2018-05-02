import unittest
from hero import Hero
from weapon_and_spell import Weapon, Spell


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.test_hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=5)
        self.test_spell = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)

    # test init
    def test_init_create_hero(self):
        Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=5)

    def test_assert_type_name(self):
        with self.assertRaises(AssertionError):
            Hero(name=5, title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=5)

    def test_assert_type_title(self):
        with self.assertRaises(AssertionError):
            Hero(name="Bron", title=5, health=100, mana=100, mana_regeneration_rate=5)

    def test_assert_type_health(self):
        with self.assertRaises(AssertionError):
            Hero(name="Bron", title="Dragonslayer", health=100.1, mana=[100], mana_regeneration_rate=5)

    def test_assert_type_mana(self):
        with self.assertRaises(AssertionError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=[10.4], mana_regeneration_rate=5)

    def test_assert_type_mana_regeneration_rate(self):
        with self.assertRaises(AssertionError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=[10.4], mana_regeneration_rate=5.1)

    def test_check_health_negative(self):
        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=-100, mana=100, mana_regeneration_rate=5)

    def test_check_health_more_than_100(self):
        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=102, mana=100, mana_regeneration_rate=5)

    def test_check_mana_more_than_100(self):
        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=102, mana_regeneration_rate=5)

    def test_check_mana_negative(self):
        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=-100, mana_regeneration_rate=5)

    def test_check_mana_regeneration_rate_negative(self):
        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=-5)

    # test known_as
    def test_known_as(self):
        expected = "Bron the Dragonslayer"
        self.assertEqual(self.test_hero.known_as(), expected)

    # test is_alive
    def test_is_alive(self):
        self.assertTrue(self.test_hero.is_alive() is True)

    # test get_health
    def test_get_health(self):
        self.assertEqual(self.test_hero.get_health(), 100)

    # test get_mana
    def test_get_mana(self):
        self.assertEqual(self.test_hero.get_mana(), 100)

    # test can_cast
    def test_can_cast(self):
        self.assertTrue(self.test_hero.can_cast(self.test_spell))

    # test take_damage
    def test_take_damage_damage_points_more_than_health(self):
        test = Hero(name="Bron", title="Dragonslayer", health=40, mana=100, mana_regeneration_rate=2)
        test.take_damage(50)
        self.assertEqual(test.get_health(), 0)

    def test_take_damage_correct(self):
        test = Hero(name="Bron", title="Dragonslayer", health=80, mana=100, mana_regeneration_rate=2)
        test.take_damage(50)
        self.assertEqual(test.get_health(), 30)

    # test take_healing
    def test_take_healing_zero_health(self):
        test = Hero(name="Bron", title="Dragonslayer", health=0, mana=100, mana_regeneration_rate=2)
        self.assertFalse(test.take_healing(50))

    def test_take_healing_over_100(self):
        test = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        test.take_healing(50)
        self.assertEqual(test.get_health(), 100)

    def test_take_healing_correct(self):
        test = Hero(name="Bron", title="Dragonslayer", health=40, mana=100, mana_regeneration_rate=2)
        self.assertTrue(test.take_healing(50))

    #test take_mana
    def test_take_mana_zero_points_full_mana(self):
        test = Hero(name="Bron", title="Dragonslayer", health=80, mana=100, mana_regeneration_rate=2)
        test.take_mana(0)
        self.assertEqual(test.get_mana(), 100)

    def test_take_mana_zero_points_not_full_mana(self):
        test = Hero(name="Bron", title="Dragonslayer", health=80, mana=80, mana_regeneration_rate=2)
        test.take_mana(0)
        self.assertEqual(test.get_mana(), 80)

    def test_take_mana_not_zero_points_full_mana(self):
        test = Hero(
        name="Bron", title="Dragonslayer", \
        health=80, mana=100, mana_regeneration_rate=2)
        test.take_mana(2)
        self.assertEqual(test.get_mana(), 100)

    def test_take_mana_not_zero_points_full_mana(self):
        test = Hero(name="Bron", title="Dragonslayer", health=80, mana=100, mana_regeneration_rate=2)
        test.take_mana(2)
        self.assertEqual(test.get_mana(), 100)

    def test_take_mana_not_zero_points_not_full_mana(self):
        test = Hero(name="Bron", title="Dragonslayer", health=80, mana=50, mana_regeneration_rate=2)
        test.take_mana(40)
        self.assertEqual(test.get_mana(), 90)

    # tess equip

    def test_equip_weapon_type(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon(name="The Axe of Destiny", damage=20)
        h.equip(w)
        self.assertEqual(h.weapon, w)

    # test learn
    def test_learn_spell_type(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        h.learn(s)
        self.assertEqual(h.spell, s)

    # test attack
    def test_attack_weapon_none(self):
        self.assertEqual(self.test_hero.attack(by="weapon"), 0)

    def test_attack_spell_none(self):
        self.assertEqual(self.test_hero.attack(by="spell"), 0)

    def test_attack_weapon_damage(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon(name="The Axe of Destiny", damage=20)
        h.equip(w)
        self.assertEqual(h.attack(by="weapon"), 20)

    def test_attack_spell_damage(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        h.learn(s)
        self.assertEqual(h.attack(by="spell"), 30)

    def test_most_powerful_weapon_when_weapon_(self):
        test_s = Spell(name='Fireball', damage=10, mana_cost=50, cast_range=2)
        test_w = Weapon('The Axe Of Destiny', 20)
        self.test_hero.learn(test_s)
        self.test_hero.equip(test_w)
        self.assertEqual(self.test_hero.get_most_powerfull_weapon(), Weapon('The Axe Of Destiny', 20))

    def test_most_powerful_weapon_when_spell_and_can_cast_true(self):
        test_s = Spell(name='Fireball', damage=30, mana_cost=50, cast_range=2)
        test_w = Weapon('The Axe Of Destiny', 20)
        self.test_hero.learn(test_s)
        self.test_hero.equip(test_w)
        self.assertEqual(self.test_hero.get_most_powerfull_weapon(), test_s)

    def test_most_powerful_weapon_when_spell_and_can_cast_false(self):
        hero_t = Hero(name="Bron", title="Dragonslayer", health=100, mana=40, mana_regeneration_rate=5)
        test_s = Spell(name='Fireball', damage=30, mana_cost=50, cast_range=2)
        test_w = Weapon('The Axe Of Destiny', 20)
        hero_t.learn(test_s)
        hero_t.equip(test_w)
        self.assertEqual(hero_t.get_most_powerfull_weapon(), test_w)


if __name__ == "__main__":
    unittest.main()
