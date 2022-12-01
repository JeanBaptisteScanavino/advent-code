from utils import Utils


def exec():
    return ["Je suis le fichier day1.py", Utils.myutils()]


def read_input_file():
    return Utils.read_file("/input/test_day_1.txt")


result = read_input_file()
print(result)
