import unittest
from enemy import Enemy


class EnemiesTests(unittest.TestCase):
    def setUp(self):
        self.enemy_one = Enemy(health=100, mana=100, damage=20)
        self.enemy_two = Enemy(health=0, mana=0, damage=0)
        self.enemy_three = Enemy(health=15, mana=25)

    def test_init_enemy_with_negative_values(self):
        with self.subTest("test with negative health"):
            with self.assertRaises(ValueError):
                Enemy(health=-5, mana=5, damage=15)

        with self.subTest("test with negative mana"):
            with self.assertRaises(ValueError):
                Enemy(health=5, mana=-5, damage=15)

        with self.subTest("test with negative damage"):
            with self.assertRaises(ValueError):
                Enemy(health=5, mana=5, damage=-15)

    def test_init_enemy_with_values_greater_then_100(self):
        with self.subTest("test with negative health"):
            with self.assertRaises(ValueError):
                Enemy(health=105, mana=5, damage=15)

        with self.subTest("test with negative mana"):
            with self.assertRaises(ValueError):
                Enemy(health=5, mana=105, damage=15)

        with self.subTest("test with negative damage"):
            with self.assertRaises(ValueError):
                Enemy(health=5, mana=5, damage=105)

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

    def test_is_alive(self):
        with self.subTest("Is alive enemy one"):
            self.assertTrue(self.enemy_one.is_alive())

        with self.subTest("Is alive enemy two"):
            self.assertFalse(self.enemy_two.is_alive())

    def test_can_cast(self):
        with self.subTest("Can cast enemy one"):
            self.assertTrue(self.enemy_one.can_cast())

        with self.subTest("Can cast enemy two"):
            self.assertFalse(self.enemy_two.can_cast())

    def test_get_health(self):
        expected = 100
        actual = self.enemy_one.get_health()
        self.assertEqual(expected, actual)

    def test_get_mana(self):
        expected = 100
        actual = self.enemy_one.get_mana()
        self.assertEqual(expected, actual)

    def test_taka_damage(self):
        damage = 20
        expected = self.enemy_one.get_health() - damage
        self.enemy_one.take_damage(damage)
        actual = self.enemy_one.get_health()
        self.assertEqual(expected, actual)

    def test_take_healing(self):
        with self.subTest("Enemy one take 0 healing"):
            healing_points = 20
            self.assertTrue(self.enemy_one.take_healing(healing_points))
            expected = 100
            actual = self.enemy_one.get_health()
            self.assertEqual(expected, actual)

        with self.subTest("Enemy two cannot take healing, it is dead"):
            healing_points = 20
            self.assertFalse(self.enemy_two.take_healing(healing_points))
            expected = 0
            actual = self.enemy_two.get_health()
            self.assertEqual(expected, actual)

        with self.subTest("Enemy three can take 20 points healing"):
            healing_points = 20
            self.assertTrue(self.enemy_three.take_healing(healing_points))
            expected = 35
            actual = self.enemy_three.get_health()
            self.assertEqual(expected, actual)

    def test_take_mana(self):
        with self.subTest("Enemy one take 0 mana"):
            mana_points = 20
            expected = 100
            self.enemy_one.take_mana(mana_points)
            actual = self.enemy_one.get_mana()
            self.assertEqual(expected, actual)

        with self.subTest("Enemy three can take 20 points mana"):
            mana_points = 20
            expected = 45
            self.enemy_three.take_mana(mana_points)
            actual = self.enemy_three.get_mana()
            self.assertEqual(expected, actual)

    def test_damage_for_enemy_one(self):
        expected = 20
        actual = self.enemy_one.attack()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
