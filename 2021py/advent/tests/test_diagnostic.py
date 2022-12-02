from ..utils.ClassicCalc import ClassicCalc
from ..utils.Diagnostic import Diagnostic
from .fixture import bit_example_diag


def test_get_gamma_bit():
    test_1 = Diagnostic.get_gamma_bit(["0", "0", "0", "1", "1", "1", "1"])
    test_0 = Diagnostic.get_gamma_bit(["0", "0", "0", "0", "1", "1", "1"])
    expect_1 = "1"
    expect_0 = "0"
    assert test_1 == expect_1
    assert test_0 == expect_0


def test_get_epsilon_bits():
    test = Diagnostic.get_epsilon_bits("11110000")
    expect = "00001111"
    assert test == expect


def test_get_decimal_from_bin():
    test_1 = ClassicCalc.get_decimal_from_bin("10110")
    test_2 = ClassicCalc.get_decimal_from_bin("01001")
    expect_1 = 22
    expect_2 = 9
    assert test_1 == expect_1
    assert test_2 == expect_2


def test_get_gamma_bits():
    test = Diagnostic.get_gamma_bits(
        [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
    )
    expect = "10110"
    assert test == expect


def test_get_oxygen():
    test = Diagnostic.get_oxygen_bits(bit_example_diag)
    expect = ["10111"]
    assert test == expect


def test_get_CO2():
    test = Diagnostic.get_CO2_bits(bit_example_diag)
    expect = ["01010"]
    assert test == expect
