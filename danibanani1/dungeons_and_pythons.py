# TODO: FIX WHAT HAPPENS WHEN YOU FIND AN S, INSTEAD OF E, T or whatever shit you may find

import sys

from random import randint


def help():
    with open('help.txt') as help:
        print(help.read())


class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.mana_save = mana
        self.weapon = None
        self.spell = None
        self.weapon_inventory = [Weapon('The Axe Of Destiny', 20)]
        self.spell_inventory = [Spell(name="Fireball",
                                      damage=30,
                                      mana_cost=50,
                                      cast_range=2)]

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def is_alive(self):
        return self.health > 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def can_cast(self, spell):
        return spell.mana_cost <= self.mana

    def take_damage(self, damage_points):
        self.health = max(0, self.health - damage_points)

    def take_healing(self, healing_points):
        if self.health > 0:
            self.health = min(100, self.health + healing_points)
            return True
        return False

    def take_mana(self, mana_points):
        self.mana = min(self.mana_save, self.mana + mana_points)

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by):
        if by == 'weapon':
            return self.weapon.damage if self.weapon is not None else 0
        if by == 'spell':
            return self.spell.damage if self.damage is not None else 0

    def get_weapon_inventory(self):
        for weapon in self.weapon_inventory:
            print(weapon)

    def get_spell_inventory(self):
        for spell in self.spell_inventory:
            print(spell)


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return '{} with damage of {}'.format(self.name, self.damage)


class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __str__(self):
        return '{} with damage of {} \
for the cost of {} mana in range of {}'.format(self.name,
                                               self.damage,
                                               self.mana_cost,
                                               self.cast_range)


class Enemy:
    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage

    def is_alive(self):
        return self.health > 0

    def can_cast(self, spell):
        return self.mana >= spell.mana_cost

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_damage(self, damage_points):
        self.health = max(0, self.health - damage_points)

    def take_healing(self, healing_points):
        if self.health > 0:
            self.health = min(100, self.health + healing_points)
            return True
        return False

    def take_mana(self, mana_points):
        self.mana = min(self.mana_save, self.mana + mana_points)

    def attack(self):
        return self.damage


class Dungeon:
    def __init__(self, dungeon_file):
        self.dungeon_filename = dungeon_file
        with open(dungeon_file) as file:
            self.dungeon = file.read().splitlines()
            for i in range(len(self.dungeon)):
                self.dungeon[i] = list(self.dungeon[i])

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
                return True
            except ValueError:
                print('Game over')
                sys.exit()

    def move_hero(self, direction):
        # TODO: Cases when the position we're moving to is T or E
        # TODO: FIX IT AS THAT HERO MOTHERFUCKER TELEPORTS ACROSS THE MAP!
        try:
            i, j = self.hero_position
            if direction == 'up' and self.dungeon[i - 1][j] != '#' and i > 0:
                    self.handle_encounters(self.dungeon[i - 1][j])
                    self.dungeon[i - 1][j] = 'H'
                    self.dungeon[i][j] = '.'
                    self.hero_position = (i - 1, j)
            elif (direction == 'down' and
                  self.dungeon[i + 1][j] != '#'):
                    self.handle_encounters(self.dungeon[i + 1][j])
                    self.dungeon[i + 1][j] = 'H'
                    self.dungeon[i][j] = '.'
                    self.hero_position = (i + 1, j)
            elif (direction == 'left' and
                  self.dungeon[i][j - 1] != '#' and
                  j > 0):
                    self.handle_encounters(self.dungeon[i][j - 1])
                    self.dungeon[i][j - 1] = 'H'
                    self.dungeon[i][j] = '.'
                    self.hero_position = (i, j - 1)
            elif (direction == 'right' and
                  self.dungeon[i][j + 1] != '#'):
                    self.handle_encounters(self.dungeon[i][j + 1])
                    self.dungeon[i][j + 1] = 'H'
                    self.dungeon[i][j] = '.'
                    self.hero_position = (i, j + 1)
            else:
                return False
            self.hero.mana = min(self.hero.mana + self.hero.mana_regeneration_rate, self.hero.mana_save)
            return True
        except IndexError:
            return False

    def handle_encounters(self, encountered):
        if encountered == 'E':
            Fight('Hero', 'Enemy')
        if encountered == 'T':
            self.get_treasure()
        if encountered == 'F':
            print('Level complete!')

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


class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy


h = Hero(name="Bron",
         title="Dragonslayer",
         health=100, mana=100,
         mana_regeneration_rate=2)
a = Dungeon('dungeon1.txt')
a.spawn(h)
