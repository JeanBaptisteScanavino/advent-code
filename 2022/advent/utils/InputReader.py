import os
import numpy as np
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

    def return_splited_with_space(file):
        result = []
        for i in file:
            result.append(i.split(" "))
        return result

    def split_string_with_char(s,c):
        return s.split(c)

    def split_inputs_with_n(file):
        print(file.index(''))
        arr = np.array(file)
        separator = np.where(arr == '')[0]
        inputs=arr[0:separator[0]].tolist()
        commands=arr[separator[0]+1:len(arr)].tolist()
        print(commands)
        return [inputs,commands]


