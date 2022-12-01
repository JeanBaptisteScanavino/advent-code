from ..utils.utils import *


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

def test_get_increased_count():
    test = CalcInArray.get_increased_count(["199","200","208","210","200","207","240","269","260","263",])
    expect = 7
    assert test == expect

def test_create_group_by_three():
    test = CalcInArray.create_group_by_three(["199","200","208","210","200","207","240","269","260","263",])
    expect = ["607","618","618","617","647","716","769","792",]
    assert test == expect

def test_get_submarine_order():
    test = CommandSubmarine.get_order("forward 2")
    expect = ["forward", "2"]
    assert test == expect

def test_forward_increase_x():
    test = CommandSubmarine.apply_order(["forward 2"])
    expect = [2,0]
    assert test == expect

def test_down_increase_depht():
    test = CommandSubmarine.apply_order(["down 5"])
    expect = [0,5]
    assert test == expect
def test_up_decrease_depht():
    test = CommandSubmarine.apply_order(["up 5"])
    expect = [0,-5]
    assert test == expect

def test_get_submarine_position():
    test= CommandSubmarine.get_submarine_position([10, 15])
    expect = 150
    assert test == expect

def test_forward_increase_x():
    test = CommandSubmarine.apply_real_order(["down 5","forward 2"])
    expect = [2,10,5]
    assert test == expect

def test_down_increase_aim():
    test = CommandSubmarine.apply_real_order(["down 5"])
    expect = [0,0,5]
    assert test == expect
def test_up_decrease_aim():
    test = CommandSubmarine.apply_real_order(["up 5"])
    expect = [0,0,-5]
    assert test == expect

def test_get_gamma_bit():
    test_1 = Diagnostic.get_gamma_bit(['0','0','0','1','1','1','1'])
    test_0 = Diagnostic.get_gamma_bit(['0','0','0','0','1','1','1'])
    expect_1 = '1'
    expect_0 = '0'
    assert test_1 == expect_1
    assert test_0 == expect_0

def test_get_epsilon_bits():
    test = Diagnostic.get_epsilon_bits('11110000')
    expect = '00001111'
    assert test == expect

def test_get_decimal_from_bin():
    test_1 = ClassicCalc.get_decimal_from_bin('10110')
    test_2 = ClassicCalc.get_decimal_from_bin('01001')
    expect_1 = 22
    expect_2 = 9
    assert test_1 == expect_1
    assert test_2 == expect_2

bit_example =["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010",]
def test_get_gamma_bits():
    test = Diagnostic.get_gamma_bits(["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010",])
    expect = '10110'
    assert test == expect
    
def test_get_only_some_result():
    test = CalcInArray.kept_bits_with_x_in_position_y(bit_example,'1',0)
    expect = ['11110', '10110', '10111', '10101', '11100', '10000', '11001']
    assert test == expect

def test_get_oxygen_from_gamma():
    test = Diagnostic.get_oxygen_bits(bit_example,'10110')
    expect = ['10111']
    assert test == expect
