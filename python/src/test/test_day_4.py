from ..day_main.day_4 import main
from ..day_main.utils.utils import read_file, make_int

day = 4
in_memory_path = f'/in_memory/test_day_{day}.txt'


def test_main_result_with_test():
    result = main(in_memory_path)
    assert result == 1
