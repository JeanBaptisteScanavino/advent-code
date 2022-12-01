import pytest

from .dayX import exec
from .utils import Utils


def test_day_send_me_a_message():
    test = exec()
    assert test


def test_read_input_file():
    test = Utils.read_file("/input/test_day_1.txt")
    result = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    assert test == result


def test_make_group_in_array():
    test = Utils.make_group_in_array(Utils.read_file("/input/test_day_1.txt"))
    result = [6000, 4000, 11000, 24000]
    assert test == result
