class Dungeon:
    def __init__(self, file_name):
        assert type(file_name) is str
        self.file_name = file_name

    def read_from_file(self):
        result = []
        with open(self.file_name) as f:
            for line in f.readlines():
                result.append([letter for letter in line][:len(line) - 1])
        return result

    def print_map(self):
        for line in self.read_from_file():
            print("".join(line))
