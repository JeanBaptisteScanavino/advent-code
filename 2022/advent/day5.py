from utils.InputReader import InputReader
from utils.CraneCrate import CraneCrate

def read_input_file():
    return InputReader.read_file("day_5.txt")


def exec_1(file):
    return CraneCrate.get_first_crates_after_move(file)
    


def exec_2(file):
    return CraneCrate.get_first_crates_after_move_9001(file)

file = read_input_file()
result_1 = exec_1(file)
print("exo_1:", result_1)
result_2 = exec_2(file)
print("exo_1:", result_2)
