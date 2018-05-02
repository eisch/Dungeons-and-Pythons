import unittest
from dungeons_and_pythons import Dungeon
from hero import Hero


class DungeonTests(unittest.TestCase):
    def setUp(self):
        self.d = Dungeon('dungeon1.txt')
        self.test_hero = Hero(
            name="Bron", title="Dragonslayer", health=100,
            mana=100, mana_regeneration_rate=5)

    def test_init_name_type(self):
        self.assertFalse(self.d.spawn(5))

    def test_spawn_type(self):
        self.assertFalse(self.d.spawn(5))
    def test_spawn_first_occurence(self):
        self.assertTrue(self.d.spawn(self.test_hero))

    def test_spawn_no_spawns(self):
        self.d.spawn(self.test_hero)
        self.assertFalse(self.d.spawn(self.test_hero))

    def test_move_direction_type(self):
        self.d.spawn(self.test_hero)
        self.assertFalse(self.d.move_hero(5))

    def test_hero_coordinates(self):
        self.d.spawn(self.test_hero)
        expected = (0, 0)
        self.assertEqual(self.d.hero_position, expected)

    def test_check_valid_move_left(self):
        self.d.spawn(self.test_hero)
        self.assertFalse(self.d.move_hero("left"))

    def test_check_valid_move_right(self):
        self.d.spawn(self.test_hero)
        self.assertTrue(self.d.move_hero("right"))

    def test_check_valid_move_up(self):
        self.d.spawn(self.test_hero)
        self.assertFalse(self.d.move_hero("up"))

    def test_check_valid_move_down(self):
        self.d.spawn(self.test_hero)
        self.assertFalse(self.d.move_hero("down"))

    def test_move_false(self):
        self.d.spawn(self.test_hero)
        self.assertFalse(self.d.move_hero("up"))

    def test_move_obstacle(self):
        self.d.spawn(self.test_hero)
        self.assertFalse(self.d.move_hero("down"))

    def test_move_path(self):
        self.d.spawn(self.test_hero)
        self.assertTrue(self.d.move_hero("right"))


if __name__ == "__main__":
    unittest.main()
