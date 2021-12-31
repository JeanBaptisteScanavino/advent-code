from ..day_main.day_1 import (
    count_increase,
    count_increase_with_windows,
    is_increase,
    make_windows,
)
from ..day_main.utils.utils import make_int, read_file

path = "/in_memory/test_day_1.txt"


def test_is_increase():
    first = 2
    second = 10
    passed = is_increase(first, second)
    failed = is_increase(second, first)
    assert failed == False
    assert passed == True


def test_count_increase():
    data = read_file(path)
    result_data = []
    for dat in data:
        result_data.append(make_int(dat))
    result = count_increase(result_data)
    assert result == 7


def test_count_increase_with_windows():
    data = read_file(path)
    result_data = []
    for dat in data:
        result_data.append(make_int(dat))
    result = count_increase_with_windows(result_data)
    assert result == 5


def test_make_windows():
    data = read_file(path)
    result_data = []
    for dat in data:
        result_data.append(make_int(dat))
    windows_1 = make_windows(result_data, 0)
    windows_2 = make_windows(result_data, 1)
    assert windows_1 == 199 + 200 + 208
    assert windows_2 == 200 + 208 + 210
