from utils.utils import CalcInArray, InputReader


def read_input_file():
    return InputReader.read_file("day_1.txt")


def exec_1():
    all_elf_kcal = read_input_file()
    split_elf_kcal = InputReader.make_group_in_array(all_elf_kcal)
    return CalcInArray.get_highter_of_array(split_elf_kcal)


def exec_2():
    all_elf_kcal = read_input_file()
    split_elf_kcal = InputReader.make_group_in_array(all_elf_kcal)
    return CalcInArray.get_tree_highter_of_array(split_elf_kcal)


result_1 = exec_1()
print("exo_1:", result_1)
result_2 = exec_2()
print("exo_1:", result_2)
