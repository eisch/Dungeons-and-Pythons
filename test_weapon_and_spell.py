import unittest
from weapon import Weapon, Spell


class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.weapon = Weapon(
            name="The Axe of Destiny",
            damage=20)

    def test_init_weapon_with_wrong_types(self):
        with self.subTest("test with 15 for name"):
            with self.assertRaises(TypeError):
                Weapon(name=15, damage=20)

        with self.subTest("test with {} for damage"):
            with self.assertRaises(TypeError):
                Weapon(name="", damage={})

    def test_init_weapon_with_wrong_values(self):
        with self.subTest("test with -15 for damage"):
            with self.assertRaises(ValueError):
                Weapon(name="", damage=-15)

        with self.subTest("test with 105 for damage"):
            with self.assertRaises(ValueError):
                Weapon(name="", damage=105)

    def test_get_name(self):
        expected = "The Axe of Destiny"
        actual = self.weapon.get_name()
        self.assertEqual(expected, actual)

    def test_get_damage(self):
        expected = 20
        actual = self.weapon.get_damage()
        self.assertEqual(expected, actual)


class TestSpell(unittest.TestCase):
    def setUp(self):
        self.spell = Spell(
            name="Fireball",
            damage=30,
            mana_cost=50,
            cast_range=2)

    def test_init_spell_with_wrong_types(self):
        with self.subTest("test with 15 for name"):
            with self.assertRaises(TypeError):
                Spell(name=15, damage=20, mana_cost=50, cast_range=2)

        with self.subTest("test with str for damage"):
            with self.assertRaises(TypeError):
                Weapon(name="", damage="", mana_cost=50, cast_range=2)

        with self.subTest("test with str for mana"):
            with self.assertRaises(TypeError):
                Weapon(name="", damage=30, mana_cost="", cast_range=2)

        with self.subTest("test with float for cast_range"):
            with self.assertRaises(TypeError):
                Weapon(name="", damage=30, mana_cost=50, cast_range=2.5)

    def test_init_weapon_with_wrong_values(self):
        with self.subTest("test with -15 for damage"):
            with self.assertRaises(ValueError):
                Spell(name="", damage=-15, mana_cost=50, cast_range=2)

        with self.subTest("test with 105 for damage"):
            with self.assertRaises(ValueError):
                Spell(name="", damage=105, mana_cost=50, cast_range=2)

        with self.subTest("test with -15 for mana_cost"):
            with self.assertRaises(ValueError):
                Spell(name="", damage=30, mana_cost=-15, cast_range=2)

        with self.subTest("test with 105 for mana_cost"):
            with self.assertRaises(ValueError):
                Spell(name="", damage=30, mana_cost=-105, cast_range=2)

        with self.subTest("test with -15 for cast_range"):
            with self.assertRaises(ValueError):
                Spell(name="", damage=30, mana_cost=50, cast_range=-15)

    def test_get_name(self):
        expected = "Fireball"
        actual = self.spell.get_name()
        self.assertEqual(expected, actual)

    def test_get_damage(self):
        expected = 30
        actual = self.spell.get_damage()
        self.assertEqual(expected, actual)

    def test_get_mana_cost(self):
        expected = 50
        actual = self.spell.get_mana_cost()
        self.assertEqual(expected, actual)

    def test_get_cast_range(self):
        expected = 2
        actual = self.spell.get_cast_range()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
