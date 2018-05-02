# TODO: Learn how to use motherf*cking Git
# TODO: Decide what happens after S is encountered
# TODO: hero_attack method
# TODO: Custom features?

import sys

from random import randint
from weapon_and_spell import Weapon, Spell
from fight import Fight


def help():
    with open('help.txt') as help:
        print(help.read())


class Dungeon:
    def __init__(self, dungeon_file, enemy):
        self.dungeon_filename = dungeon_file
        with open(dungeon_file) as file:
            self.dungeon = file.read().splitlines()
            for i in range(len(self.dungeon)):
                self.dungeon[i] = list(self.dungeon[i])
        self.save_respawn_points = []
        self.enemy = enemy
        self.hero = None

    def print_map(self):
        for line in self.dungeon:
            print("".join(line))
        print()

    def spawn(self, hero):
        for i in range(len(self.dungeon)):
            try:
                line_index = self.dungeon[i].index('S')
                self.dungeon[i][line_index] = 'H'
                self.hero_position = (i, line_index)
                self.hero = hero
                if (i, line_index) in self.save_respawn_points:
                    self.save_respawn_points.remove((i, line_index))
                return True
            except ValueError:
                print('Game over')
                sys.exit()

    def move_hero(self, direction):
        try:
            i, j = self.hero_position
            if direction == 'up' and self.dungeon[i - 1][j] != '#' and i > 0:
                    self.handle_encounters(i - 1, j)
                    self.dungeon[i - 1][j] = 'H'
                    self.dungeon[i][j] = '.'
                    self.hero_position = (i - 1, j)
            elif (direction == 'down' and
                  self.dungeon[i + 1][j] != '#'):
                    self.handle_encounters(i + 1, j)
                    self.dungeon[i + 1][j] = 'H'
                    self.dungeon[i][j] = '.'
                    self.hero_position = (i + 1, j)
            elif (direction == 'left' and
                  self.dungeon[i][j - 1] != '#' and
                  j > 0):
                    self.handle_encounters(i, j - 1)
                    self.dungeon[i][j - 1] = 'H'
                    self.dungeon[i][j] = '.'
                    self.hero_position = (i, j - 1)
            elif (direction == 'right' and
                  self.dungeon[i][j + 1] != '#'):
                    self.handle_encounters(i, j + 1)
                    self.dungeon[i][j + 1] = 'H'
                    self.dungeon[i][j] = '.'
                    self.hero_position = (i, j + 1)
            else:
                return False
            self.hero.mana = min(
                self.hero.mana + self.hero.mana_regeneration_rate,
                self.hero.mana_save)
            self.hero.mana = min(
                self.hero.mana + self.hero.mana_regeneration_rate,
                self.hero.mana_save)
            return True
        except IndexError:
            return False

    def handle_encounters(self, row, col):
        for respawn_tuple in self.save_respawn_points:
            self.dungeon[respawn_tuple[0]][respawn_tuple[1]] = 'S'
        if self.dungeon[row][col] == 'E':
            if self.hero is not None:
                Fight(self.hero, self.enemy)
        elif self.dungeon[row][col] == 'T':
            self.get_treasure()
        elif self.dungeon[row][col] == 'G':
            print('Level complete!')
        elif self.dungeon[row][col] == 'S':
            self.save_respawn_points.append((row, col))
        elif self.dungeon[row][col] == '.':
            pass
        else:
            print('WTF have you encountered?')

    def hero_attack(by):
        pass

    def get_treasure(self):
        with open("treasures_{}".format(self.dungeon_filename)) as file:
            lines = file.read().splitlines()
            found = lines[randint(0, len(lines) - 1)]
            if found == 'mana potion':
                self.hero.mana = self.hero.mana_save
                print("You've found a mana potion. Your mana is now max!")
            elif found == 'health potion':
                print("You've found a health potion. Your health is now 100!")
                self.hero.health = 100
            elif found.startswith('W'):
                found = found.split()
                print('You found the weapon {}. \
It deals {} damage!'.format(found[1], found[2]))
                self.hero.weapon_inventory.append(Weapon(found[1], found[2]))
            elif found.startswith('S'):
                found = found.split()
                print('You found a scroll! \
Now you can learn the spell {}. \
It deals {} damage for the cost of {} mana in range of {}!'.format(found[1],
                                                                   found[2],
                                                                   found[3],
                                                                   found[4]))
                self.hero.spell_inventory.append(Spell(found[1],
                                                       found[2],
                                                       found[3],
                                                       found[4]))
            else:
                print("You found a bag of potatoes!")
