from utils import Utils


def read_input_file():
    return Utils.read_file("/input/day_1.txt")


def exec_1():
    all_elf_kcal = read_input_file()
    split_elf_kcal = Utils.make_group_in_array(all_elf_kcal)
    return Utils.is_higher_elf_kcal(split_elf_kcal)


def exec_2():
    all_elf_kcal = read_input_file()
    split_elf_kcal = Utils.make_group_in_array(all_elf_kcal)
    return Utils.total_of_three_higher_elf_kcal(split_elf_kcal)


result_1 = exec_1()
print("exo_1:", result_1)
result_2 = exec_2()
print("exo_1:", result_2)
