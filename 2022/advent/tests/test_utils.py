from ..utils.utils import InputReader,CalcInArray


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


def test_get_highter_of_array():
    test = CalcInArray.get_highter_of_array([6000, 4000, 11000, 24000, 10000])
    result = 24000
    assert test == result


def test_get_tree_highter_of_array():
    test = CalcInArray.get_tree_highter_of_array([6000, 4000, 11000, 24000, 10000])
    result = 45000
    assert test == result
