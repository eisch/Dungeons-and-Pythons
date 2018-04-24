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

    def move(self, direction):
        assert type(direction) is str

