from ..day_main.day_3 import main, get_bits
from ..day_main.utils.utils import read_file, make_int

day = 3
in_memory_path = f"/in_memory/test_day_{day}.txt"


def test_get_bits():
    initial_table = "00101"
    result = get_bits(initial_table)
    assert result == ["0", "0", "1", "0", "1"]


def test_main_result_with_test():
    result = main(in_memory_path)
    assert result == 198
