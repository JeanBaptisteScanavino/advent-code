from utils.InputReader import InputReader
from utils.Cleanup import Cleanup

def read_input_file():
    return InputReader.read_file("day_4.txt")


def exec_1(file):
    return Cleanup.how_many_totaly_in_range(file)
    


def exec_2(file):
    return Cleanup.how_many_overlap(file)

file = read_input_file()
result_1 = exec_1(file)
print("exo_1:", result_1)
result_2 = exec_2(file)
print("exo_1:", result_2)
