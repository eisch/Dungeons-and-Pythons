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
            Hero(name="Bron", title="Dragonslayer", health=100.1, mana=100, mana_regeneration_rate=5)

    def test_assert_type_mana(self):
        with self.assertRaises(AssertionError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=10.4, mana_regeneration_rate=5)

    def test_assert_type_mana_regeneration_rate(self):
        with self.assertRaises(AssertionError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=10.4, mana_regeneration_rate=5.1)

    def test_check_health_negative(self):
        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=-100, mana=100, mana_regeneration_rate=5)

    def test_check_mana_negative(self):
        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=-100, mana_regeneration_rate=5)

    def test_check_mana_regeneration_rate_negative(self):
        with self.assertRaises(ValueError):
            Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=-5)

    def test_known_as(self):
        expected = "Bron the Dragonslayer"
        self.assertEqual(self.test_hero.known_as(), expected)


if __name__ == "__main__":
    unittest.main()
