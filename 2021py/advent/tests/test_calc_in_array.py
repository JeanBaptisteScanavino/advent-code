from ..utils.CalcInArray import CalcInArray
from .fixture import bit_example_diag


def test_get_highter_of_array():
    test = CalcInArray.get_highter_of_array([6000, 4000, 11000, 24000, 10000])
    result = 24000
    assert test == result


def test_get_tree_highter_of_array():
    test = CalcInArray.get_tree_highter_of_array([6000, 4000, 11000, 24000, 10000])
    result = 45000
    assert test == result


def test_get_increased_count():
    test = CalcInArray.get_increased_count(
        [
            "199",
            "200",
            "208",
            "210",
            "200",
            "207",
            "240",
            "269",
            "260",
            "263",
        ]
    )
    expect = 7
    assert test == expect


def test_create_group_by_three():
    test = CalcInArray.create_group_by_three(
        [
            "199",
            "200",
            "208",
            "210",
            "200",
            "207",
            "240",
            "269",
            "260",
            "263",
        ]
    )
    expect = [
        "607",
        "618",
        "618",
        "617",
        "647",
        "716",
        "769",
        "792",
    ]
    assert test == expect


def test_get_only_some_result():
    test = CalcInArray.kept_bits_with_x_in_position_y(bit_example_diag, "1", 0)
    expect = ["11110", "10110", "10111", "10101", "11100", "10000", "11001"]
    assert test == expect
