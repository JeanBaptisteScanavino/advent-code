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
    test = PlayWithString.is_in_two_string(PlayWithString.split_in_two(day_3_readed[1]))
    result = "L"
    assert test == result

def test_calc_priority():
    test = PlayWithString.calc_priority(day_3_readed)
    result = 157
    assert test == result
    
def test_calc_char_priority():
    test_a = PlayWithString.calc_char_priority('a')
    test_z = PlayWithString.calc_char_priority('z')
    test_A = PlayWithString.calc_char_priority('A')
    test_Z = PlayWithString.calc_char_priority('Z')
    result_a = 1
    result_z = 26
    result_A = 27
    result_Z = 52
    assert test_a == result_a
    assert test_z == result_z
    assert test_A == result_A
    assert test_Z == result_Z

def test_is_in_three_string():
    test = PlayWithString.is_in_three_string(day_3_readed[:3])
    result = "r"
    assert test == result
    test = PlayWithString.is_in_three_string(day_3_readed[3:])
    result = "Z"
    assert test == result

def test_calc_real_priority():
    test = PlayWithString.calc_real_priority(day_3_readed)
    result = 70
    assert test == result
