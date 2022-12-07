from utils.InputReader import InputReader
from utils.Transmission import Transmission

def read_input_file():
    return InputReader.read_file("day_6.txt")


def exec_1(file):
    return Transmission.get_index_first_marker(file)
    


def exec_2(file):
    return Transmission.get_index_first_marker(file,14)

file = read_input_file()
result_1 = exec_1(file[0])
print("exo_1:", result_1)
result_2 = exec_2(file[0])
print("exo_1:", result_2)
