from hero import Hero


class Dungeon:
    def __init__(self, file_name):
        assert type(file_name) is str
        self.file_name = file_name
        self.map = self.read_from_file_map()

    def read_from_file_map(self):
        result = []
        with open(self.file_name) as f:
            for line in f.readlines():
                result.append([letter for letter in line][:len(line) - 1])
        return result

    def print_map(self):
        for line in self.map:
            print("".join(line))

    def spawn(self, hero):
        assert type(hero) is Hero
        for ind, element in enumerate(self.map):
            if 'S' in element:
                index = element.index('S')
                element[index] = "H"
                return True
        return False

    def is_valid_coordinate(self, x, y):
        return x in range(0, len(self.map)) and y in range(0, len(self.map[0]))

    def get_coordinate(self, element):
        for index, list_elem in enumerate(self.map):
            if element in list_elem:
                ind = list_elem.index(element)
                return (index, ind)
        return False

    def hero_coordinates(self):
        return self.get_coordinate('H')

    def get_element_from_coordinates(self, x, y):
        if self.is_valid_coordinate(x, y):
            return self.map[x][y]
        else:
            return None

    def check_valid_move(self, direction):
        hero_x, hero_y = self.hero_coordinates()
        if direction == "right":
            return self.is_valid_coordinate(hero_x, hero_y + 1)
        elif direction == "left":
            return self.is_valid_coordinate(hero_x, hero_y - 1)
        elif direction == "up":
            return self.is_valid_coordinate(hero_x - 1, hero_y)
        elif direction == "down":
            return self.is_valid_coordinate(hero_x + 1, hero_y)

    def change_coordinates(self, x, y, direction):
        if self.check_valid_move(direction):
            if direction == "right":
                return (x, y + 1)
            elif direction == "left":
                return (x, y - 1)
            elif direction == "up":
                return (x - 1, y)
            elif direction == "down":
                return (x + 1, y)

    def swap_elements(self, x, y, direction, element):
        new_x, new_y = self.change_coordinates(x, y, direction)
        if element == '.':
            self.map[x][y], self.map[new_x][new_y] = self.map[new_x][new_y], self.map[x][y]
        elif element == 'T':
            self.map[x][y], self.map[new_x][new_y] = ".", self.map[x][y]

    def move(self, direction):
        assert type(direction) is str
        if not self.check_valid_move(direction):
            return False
        else:
            hero_x, hero_y = self.hero_coordinates()
            new_x, new_y = self.change_coordinates(hero_x, hero_y, direction)
            if self.get_element_from_coordinates(new_x, new_y) == "#":
                return False
            elif self.get_element_from_coordinates(new_x, new_y) == "E":
                pass
                # TODO: fight
            elif self.get_element_from_coordinates(new_x, new_y) == "T":
                print("Found treasure!")
                # self.swap_elements(hero_x, hero_y, direction, ".")
                # TODO: random treasures
            elif self.get_element_from_coordinates(new_x, new_y) == ".":
                self.swap_elements(hero_x, hero_y, direction, ".")
                return True


