from ..utils.utils import Utils


def test_read_input_file():
    test = Utils.read_file("/test_day_1.txt")
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
    test = Utils.make_group_in_array(Utils.read_file("test_day_1.txt"))
    result = [6000, 4000, 11000, 24000, 10000]
    assert test == result


def test_is_higher_elf_kcal():
    test = Utils.is_higher_elf_kcal([6000, 4000, 11000, 24000, 10000])
    result = 24000
    assert test == result


def test_total_of_three_higher_elf_kcal():
    test = Utils.total_of_three_higher_elf_kcal([6000, 4000, 11000, 24000, 10000])
    result = 45000
    assert test == result
