class DrinkListFileManager:

    def __init__(self, file_path_and_name):
        self.file = open(file_path_and_name)

    # private file managers for the class
    def _open_file(self, file_option):
        try:
            return open(self.file, file_option)
        except FileNotFoundError as file_location_error:
            print("There is an issue with the file location, see the below error")
            print(file_location_error)

    # File actions

    def print_file(self):
        print(self.file.read())

    def line_count(self):
        return len(self._open_file('r').readlines())

    def write_to_file(self, item):
        file = self._open_file('w')
        file.write(item + '\n')
        file.close()


x = DrinkListFileManager("dink.txt")
x.write_to_file("Dr")
print(x.line_count())
