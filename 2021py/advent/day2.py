from utils.utils import CalcInArray, CommandSubmarine, InputReader


def read_input_file():
    return InputReader.read_file("day_2.txt")


def exec_1(file):
    postions = CommandSubmarine.apply_order(file)
    return CommandSubmarine.get_submarine_position(postions)


def exec_2(file):
    postions = CommandSubmarine.apply_real_order(file)
    return CommandSubmarine.get_submarine_position(postions)


file = read_input_file()
result_1 = exec_1(file)
print("exo_1:", result_1)
result_2 = exec_2(file)
print("exo_1:", result_2)
