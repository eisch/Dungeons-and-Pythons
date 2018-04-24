import unittest
from dungeon import Dungeon
from hero import Hero


class DungeonTests(unittest.TestCase):
    def setUp(self):
        self.d = Dungeon('level1.txt')
        self.test_hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=5)

    def test_init_name_type(self):
        with self.assertRaises(AssertionError):
            Dungeon(5)

    def test_spawn_type(self):
        with self.assertRaises(AssertionError):
            self.d.spawn(5)

    def test_spawn_first_occurence(self):
        self.assertTrue(self.d.spawn(self.test_hero))

    def test_spawn_no_spawns(self):
        self.d.spawn(self.test_hero)
        self.assertFalse(self.d.spawn(self.test_hero))

    def test_move_direction_type(self):
        with self.assertRaises(AssertionError):
            self.d.move(5)


if __name__ == "__main__":
    unittest.main()
