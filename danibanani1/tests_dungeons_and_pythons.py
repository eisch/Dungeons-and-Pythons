import unittest

from dungeons_and_pythons import *


class TestMusic(unittest.TestCase):
    def setUp(self):
        self.h1 = Hero(name="Bron",
                       title="DragonSlayer",
                       health=100,
                       mana=100,
                       mana_regeneration_rate=2
                       )
        self.h2 = Hero(name="Gencho",
                       title='Banicharq',
                       health=0,
                       mana=30,
                       mana_regeneration_rate=5
                       )

    def test_known_as(self):
        expected_data = 'Bron the DragonSlayer'
        self.assertEqual(self.h1.known_as(), expected_data)

    def test_is_alive(self):
        self.assertTrue(self.h1.is_alive())
        self.assertFalse(self.h2.is_alive())

    def test_get_health(self):
        self.assertEqual(self.h1.get_health(), 100)
        self.assertEqual(self.h2.get_health(), 0)

    def test_get_mana(self):
        self.assertEqual(self.h1.get_mana(), 100)
        self.assertEqual(self.h2.get_mana(), 30)

    def test_can_cast(self):
        pass

    def test_take_damage(self):
        with self.subTest('Damage on hero who is alive'):
            self.h1.take_damage(20)
            self.assertEqual(self.h1.get_health(), 80)
        with self.subTest('Damage on hero who is dead'):
            self.h2.take_damage(20)
            self.assertEqual(self.h2.get_health(), 0)

    def test_take_healing(self):
        with self.subTest('Test if take_healing can exceed 100 health'):
            self.assertTrue(self.h1.take_healing(20))
            self.assertEqual(self.h1.get_health(), 100)
        with self.subTest('Heal hero who is alive and below 100 health'):
            self.h1.take_damage(30)
            self.assertTrue(self.h1.take_healing(20))
            self.assertEqual(self.h1.get_health(), 90)
        with self.subTest('Heal hero who is dead'):
            self.assertFalse(self.h2.take_healing(50))

    def test_take_mana(self):
        self.h2.mana = 0
        self.h2.take_mana(30)
        self.assertEqual(self.h2.get_mana(), 30)


if __name__ == '__main__':
    unittest.main()
