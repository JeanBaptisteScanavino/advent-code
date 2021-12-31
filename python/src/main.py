import os

from day_main.utils.utils import read_file

my_path = os.path.abspath(os.path.dirname(__file__))
path = f"{my_path}/day_main/utils/main.txt"


def main():
    return read_file("/main.txt")


main()
