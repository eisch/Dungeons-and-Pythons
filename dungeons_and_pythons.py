# TODO: Learn how to use motherf*cking Git
# TODO: Decide what happens after S is encountered
# TODO: hero_attack method
# TODO: Custom features?

import sys

from random import randint
from weapon_and_spell import Weapon, Spell
from fight import Fight
from hero import Hero
from enemy import Enemy


def help():
    with open('help.txt') as help:
        print(help.read())


class Dungeon:
    def __init__(self, dungeon_file):
        self.dungeon_filename = dungeon_file
        with open(dungeon_file) as file:
            self.dungeon = file.read().splitlines()
            for i in range(len(self.dungeon)):
                self.dungeon[i] = list(self.dungeon[i])
        self.save_respawn_points = []
        self.enemy = None
        self.hero = None

    def print_map(self):
        for line in self.dungeon:
            print("".join(line))
        print()

    def spawn(self, hero):
        for i in range(len(self.dungeon)):
            try:
                if hero.__class__ != Hero:
                    raise AssertionError
                line_index = self.dungeon[i].index('S')
                self.dungeon[i][line_index] = 'H'
                self.hero_position = (i, line_index)
                self.hero = hero
                if (i, line_index) in self.save_respawn_points:
                    self.save_respawn_points.remove((i, line_index))
                return True
            except AssertionError:
                print("Wrong hero")
                return False
            except ValueError:
                print('Game over')
                return False

    def set_enemy(self, enemy):
        self.enemy = enemy

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
            if self.hero is not None and self.enemy is not None:
                f = Fight(self.hero, self.enemy)
                if not f.fight():
                    self.spawn(self.hero)
        elif self.dungeon[row][col] == 'T':
            self.get_treasure()
        elif self.dungeon[row][col] == 'G':
            return 'Level complete!'
        elif self.dungeon[row][col] == 'S':
            self.save_respawn_points.append((row, col))
        elif self.dungeon[row][col] == '.':
            pass
        else:
            print('WTF have you encountered?')

    def find_closest_enemy_in_range(self, r):
        self.enemy_positon = None
        x_positions = [self.hero_position[0] + i for i in range(-r, r + 1)]
        y_positions = [self.hero_position[1] + i for i in range(-r, r + 1)]
        for i, j in zip(x_positions, y_positions):
            if self.dungeon[i][j] == 'E':
                self.enemy_positon = [i, j]
                break
        self.dungeon[i][j] = '.'

    def hero_attack(self, by):
        if by == 'spell':
            self.find_closest_enemy_in_range(self.hero.spell.get_cast_range())
            fight_range = self.hero.spell.get_cast_range()
            if self.enemy_positon is None:
                print(f"Nothing in casting range {fight_range}")
            else:
                self.temp_enemy = self.enemy
                print(
                    f"A fight is started between our {self.hero} and {self.enemy}")
                while not (self.enemy_positon[0] == self.hero_position[0] and
                           self.enemy_positon[1] == self.hero_position[1]):

                    self.temp_enemy.take_damage(self.hero.attack(by='spell'))
                    print(f"Hero casts a {self.hero.spell.get_name()}, hits enemy for {self.hero.attack(by='spell')} dmg. Enemy health is {self.temp_enemy.get_health()}")

                    if self.enemy_positon[0] < self.hero_position[0]:
                        self.enemy_positon[0] += 1
                        print("Enemy moves one square down in order to get to the hero. This is his move.")
                        continue

                    if self.enemy_positon[0] > self.hero_position[0]:
                        self.enemy_positon[0] -= 1
                        print("Enemy moves one square up in order to get to the hero. This is his move.")
                        continue

                    if self.enemy_positon[1] < self.hero_position[1]:
                        self.enemy_positon[1] += 1
                        print("Enemy moves one square to the right in order to get to the hero. This is his move.")
                        continue

                    if self.enemy_positon[1] > self.hero_position[1]:
                        self.enemy_positon[1] -= 1
                        print("Enemy moves one square to the left in order to get to the hero. This is his move.")
                        continue

                f = Fight(self.hero, self.enemy)
                if not f.fight:
                    self.spawn(self.hero)

        elif by == 'weapon':
            print("Enemy is not close enough!")

        else:
            raise ValueError("There only weapon and spell!")

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
                self.hero.weapon_inventory.append(
                    Weapon(found[1], float(found[2])))
            elif found.startswith('S'):
                found = found.split()
                print('You found a scroll! \
Now you can learn the spell {}. \
It deals {} damage for the cost of {} mana in range of {}!'.format(found[1],
                                                                   found[2],
                                                                   found[3],
                                                                   found[4]))
                self.hero.spell_inventory.append(Spell(found[1],
                                                       float(found[2]),
                                                       float(found[3]),
                                                       int(found[4])))
            else:
                print("You found a bag of potatoes!")


# def main():
#     weapon = Weapon(name="The Axe of Destiny", damage=20)
#     spell = Spell(name="Fireball", damage=30,
#                   mana_cost=50, cast_range=2)
#     one = Dungeon("dungeon1.txt")
#     one.print_map()
#     my_hero = Hero(
#         name="Bron", title="Dragonslayer",
#         health=100, mana=100, mana_regeneration_rate=2)
#     my_hero.equip(weapon)
#     my_hero.learn(spell)
#     my_enemy = Enemy(health=100, mana=100, damage=20)
#     one.spawn(my_hero)
#     one.set_enemy(my_enemy)
#     one.print_map()
#     print(one.move_hero("right"))
#     one.print_map()
#     print(one.move_hero("down"))
#     one.print_map()
#     one.hero_attack(by='spell')
#     print(one.move_hero("down"))
#     one.print_map()
#     one.hero_attack(by='spell')
#     one.print_map()


# if __name__ == '__main__':
#     main()
