import unittest
from hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.test_hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=5)

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

    def test_known_as(self):
        expected = "Bron the Dragonslayer"
        self.assertEqual(self.test_hero.known_as(), expected)

    def test_is_alive(self):
        self.assertTrue(self.test_hero.is_alive() is True)

    def test_can_cast(self):
        self.assertTrue(self.test_hero.can_cast() is True)

    def test_get_health(self):
        self.assertEqual(self.test_hero.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.test_hero.get_mana(), 100)


if __name__ == "__main__":
    unittest.main()
