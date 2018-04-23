import unittest
from enemy import Enemy


class EnemiesTests(unittest.TestCase):
    def setUp(self):
        self.enemy_one = Enemy(health=100, mana=100, damage=20)

    def test_init_enemy_for_negative_values(self):
        with self.subTest("test with negative health"):
            with self.assertRaises(ValueError):
                Enemy(health=-5, mana=5, damage=15)
        with self.subTest("test with negative mana"):
            with self.assertRaises(ValueError):
                Enemy(health=5, mana=-5, damage=15)
        with self.subTest("test with negative damage"):
            with self.assertRaises(ValueError):
                Enemy(health=5, mana=5, damage=-15)

    def test_init_enemy_for_wrong_types(self):
        with self.subTest("test with negative health"):
            with self.assertRaises(TypeError):
                Enemy(health="", mana=5, damage=15)
        with self.subTest("test with negative mana"):
            with self.assertRaises(TypeError):
                Enemy(health=5, mana="", damage=15)
        with self.subTest("test with negative damage"):
            with self.assertRaises(TypeError):
                Enemy(health=5, mana=5, damage="")

    def test_get_health(self):
        expected = 100
        actual = self.enemy_one.get_health()
        self.assertEqual(expected, actual)

    def test_get_mana(self):
        expected = 100
        actual = self.enemy_one.get_mana()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
