from ..utils.InputReader import InputReader
from .fixture import bingo_test


def test_read_input_file():
    test = InputReader.read_file("/test_day_1.txt")
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
    test = InputReader.make_group_in_array(InputReader.read_file("test_day_1.txt"))
    result = [6000, 4000, 11000, 24000, 10000]
    assert test == result


def test_get_bingo_nb():
    test = InputReader.get_first_line(bingo_test)
    result = [
        "7",
        "4",
        "9",
        "5",
        "11",
        "17",
        "23",
        "2",
        "0",
        "14",
        "21",
        "24",
        "10",
        "16",
        "13",
        "6",
        "15",
        "25",
        "12",
        "22",
        "18",
        "20",
        "8",
        "19",
        "3",
        "26",
        "1",
    ]
    assert test == result
