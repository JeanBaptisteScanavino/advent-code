import os

my_path = os.path.abspath(os.path.dirname(__file__))


class InputReader:
    def myutils():
        return "utils"

    def read_file(file_to_read):

        path = f"{my_path}/../input/{file_to_read}"
        reading_file = open(path, "r")
        readed_file = reading_file.read().split("\n")
        reading_file.close()
        return readed_file

    def make_group_in_array(file):
        elf_kcal = 0
        result = []
        for i, x in enumerate(file):
            if x == "":
                result.append(elf_kcal)
                elf_kcal = 0
            elif i == len(file) - 1:
                elf_kcal += int(x)
                result.append(elf_kcal)
            else:
                elf_kcal += int(x)
        return result

    def get_first_line(file):
        print(file[0])
        return InputReader.split_string_with_char(file[0],',')

    def split_string_with_char(s,c):
        return s.split(c)

