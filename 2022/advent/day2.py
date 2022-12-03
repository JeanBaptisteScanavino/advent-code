from utils.InputReader import InputReader
from utils.ElfGame import ElfGame


def read_input_file():
    return InputReader.read_file("day_2.txt")


def exec_1(file):
    game = InputReader.return_splited_with_space(file)
    return ElfGame.make_game(game)


def exec_2(file):
    game = InputReader.return_splited_with_space(file)
    return ElfGame.make_real_game(game)


file = read_input_file()
result_1 = exec_1(file)
print("exo_1:", result_1)
result_2 = exec_2(file)
print("exo_1:", result_2)
