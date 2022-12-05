from ..utils.InputReader import InputReader
from ..utils.CraneCrate import CraneCrate 
from .fixture import day_5_readed


def test_separate_input_command():
    [inputs,commands] = InputReader.split_inputs_with_n(day_5_readed)
    expected_inputs = ['    [D]    ', '[N] [C]    ', '[Z] [M] [P]', ' 1   2   3 ']
    expected_commands = ['move 1 from 2 to 1','move 3 from 1 to 3','move 2 from 2 to 1','move 1 from 1 to 2']
    assert inputs == expected_inputs
    assert commands == expected_commands

test_inputs = InputReader.split_inputs_with_n(day_5_readed)[0]
test_commands = InputReader.split_inputs_with_n(day_5_readed)[1]
number_of_columns = CraneCrate.get_number_of_column(test_inputs[len(test_inputs)-1])

def test_extract_crate():
    crates = CraneCrate.extract_crate(test_inputs,number_of_columns)
    expected_crates = [['N','Z'],['D','C','M'],['P']]
    assert crates == expected_crates

def test_get_number_of_columns():
    crates = CraneCrate.get_number_of_column(test_inputs[len(test_inputs)-1])
    expected_columns = 3
    assert crates == expected_columns

def test_get_index_of_char_in_string():
    index = CraneCrate.get_index_of_char_in_string(test_inputs[3])
    expected_index =[1, 5, 9]
    assert index == expected_index

def test_get_commands():
    commands = CraneCrate.get_commands(test_commands)
    expected_commands = [[1,2,1], [3,1,3], [2,2,1], [1,1,2]]
    assert commands == expected_commands

commands_int = CraneCrate.get_commands(test_commands)

def test_move_a_crate():
    crates = CraneCrate.extract_crate(test_inputs,number_of_columns)
    result = CraneCrate.move_a_crate(commands_int[0],crates)
    expected_crates = [['D','N','Z'],['C','M'],['P']]
    assert result == expected_crates

def test_move_get_first_crates_after_move():
    result = CraneCrate.get_first_crates_after_move(day_5_readed)
    expect = 'CMZ'
    assert result == expect

def test_move_with_crate_mover_9001():
    result = CraneCrate.move_crate_with_crate_mover_9001(commands_int[1],[['D','N','Z'],['C','M'],['P']])
    expected_crates = [[],['C','M'],['D','N','Z','P']]
    assert result == expected_crates
