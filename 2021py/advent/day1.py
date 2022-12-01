from utils.utils import CalcInArray, InputReader


def read_input_file():
    return InputReader.read_file("day_1.txt")


def exec_1(file):
    return CalcInArray.get_increased_count(file)

def exec_2(file):
    group = CalcInArray.create_group_by_three(file)
    return CalcInArray.get_increased_count(group)

file = read_input_file()
result_1 = exec_1(file)
print("exo_1:", result_1)
result_2 = exec_2(file)
print("exo_1:", result_2)
