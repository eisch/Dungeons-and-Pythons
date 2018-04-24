import unittest
from dungeon import Dungeon


class DungeonTests(unittest.TestCase):
    def setUp(self):
        self.d = Dungeon('level1.txt')

    def test_init_name_type(self):
        with self.assertRaises(AssertionError):
            Dungeon(5)

    def test_print(self):
        self.d.print_map()


if __name__ == "__main__":
    unittest.main()
