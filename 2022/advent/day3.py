from utils.InputReader import InputReader
from utils.PlayWithString import PlayWithString

def read_input_file():
    return InputReader.read_file("day_3.txt")


def exec_1(file):
    return PlayWithString.calc_priority(file)
    


def exec_2(file):
    return PlayWithString.calc_real_priority(file)

file = read_input_file()
result_1 = exec_1(file)
print("exo_1:", result_1)
result_2 = exec_2(file)
print("exo_1:", result_2)
