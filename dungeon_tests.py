import unittest
from dungeon import Dungeon


class DungeonTests(unittest.TestCase):
    def test_init_name_type(self):
        with self.assertRaises(AssertionError):
            Dungeon(5)


if __name__ == "__main__":
    unittest.main()
