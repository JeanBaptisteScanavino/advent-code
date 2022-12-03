from .fixture import day_3_readed
from ..utils.PlayWithString import PlayWithString


def test_split_string_in_two():
    test = PlayWithString.split_in_two("AAAAAAAABBBBBBBB")
    result = ["AAAAAAAA", "BBBBBBBB"]
    assert test == result


def test_count_char_in_string():
    test_a = PlayWithString.count_char("AAAAAAAaAAAAAA", "a")
    test_A = PlayWithString.count_char("AAAAAAAaAAAAAA", "A")
    count_a = 1
    count_A = 13
    assert test_a == count_a
    assert test_A == count_A


def test_is_in_two_string():
    test = PlayWithString.is_in_two_string(PlayWithString.split_in_two(day_3_readed[0]))
    result = "p"
    assert test == result

def test_calc_priority():
    test = PlayWithString.calc_priority(day_3_readed)
    result = 157
    assert test == result
    