import unittest
from weapon import Weapon


class WeaponTests(unittest.TestCase):
    def test_init_create_weapon(self):
        Weapon(name="The Axe of Destiny", damage=20)

    def test_init_name_wrong_type(self):
        with self.assertRaises(AssertionError):
            Weapon(name=["The Axe of Destiny"], damage=20)

    def test_init_damage_wrong_type(self):
        with self.assertRaises(AssertionError):
            Weapon(name="The Axe of Destiny", damage="20")

    def test_eq_true(self):
        w1 = Weapon(name="The Axe of Destiny", damage=20)
        w2 = Weapon(name="The Axe of Destiny", damage=20)
        self.assertTrue(w1 == w2)

    def test_eq_false(self):
        w1 = Weapon(name="The Axe of Destiny", damage=20)
        w2 = Weapon(name="The Axe of Destiny", damage=30)
        self.assertFalse(w1 == w2)


if __name__ == "__main__":
    unittest.main()
