import unittest
from dungeons_and_pythons import Dungeon
from hero import Hero


class DungeonTests(unittest.TestCase):
    def setUp(self):
        self.d = Dungeon('level1.txt')
        self.test_hero = Hero(
            name="Bron", title="Dragonslayer", health=100,
            mana=100, mana_regeneration_rate=5)

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

    def test_print_map(self):
        pass

    def test_is_valid_coordinate_true(self):
        self.assertTrue(self.d.is_valid_coordinate(4, 6))

    def test_is_valid_coordinate_false(self):
        self.assertFalse(self.d.is_valid_coordinate(8, 10))

    def test_get_coordinate_true(self):
        expected = (0, 9)
        self.assertEqual(self.d.get_coordinate('T'), expected)

    def test_get_coordinate_false(self):
        self.assertFalse(self.d.get_coordinate('P'))

    def test_hero_coordinates_false(self):
        self.assertFalse(self.d.hero_coordinates())

    def test_hero_coordinates(self):
        self.d.spawn(self.test_hero)
        expected = (0, 0)
        self.assertEqual(self.d.hero_coordinates(), expected)

    def test_check_valid_move_left(self):
        self.d.spawn(self.test_hero)
        self.assertFalse(self.d.check_valid_move("left"))

    def test_check_valid_move_right(self):
        self.d.spawn(self.test_hero)
        self.assertTrue(self.d.check_valid_move("right"))

    def test_check_valid_move_up(self):
        self.d.spawn(self.test_hero)
        self.assertFalse(self.d.check_valid_move("up"))

    def test_check_valid_move_down(self):
        self.d.spawn(self.test_hero)
        self.assertTrue(self.d.check_valid_move("down"))

    def test_get_element_from_coordinates_invalid_coordinates(self):
        self.assertEqual(self.d.get_element_from_coordinates(5, 10), None)

    def test_get_element_from_coodinates_valid_coordinates(self):
        self.assertEqual(self.d.get_element_from_coordinates(2, 5), 'E')

    def test_move_false(self):
        self.d.spawn(self.test_hero)
        self.assertFalse(self.d.move("up"))

    def test_move_obstacle(self):
        self.d.spawn(self.test_hero)
        self.assertFalse(self.d.move("down"))

    def test_move_path(self):
        self.d.spawn(self.test_hero)
        self.assertTrue(self.d.move("right"))
        self.d.print_map()


if __name__ == "__main__":
    unittest.main()
