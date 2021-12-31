from os import path

from ..day_main.day_2 import (
    apply_instruction,
    apply_instruction_with_aim,
    apply_instructions,
    main,
    read_instruction,
)
from ..day_main.utils.utils import read_file

path = "/in_memory/test_day_2.txt"


def test_read_instruction():
    instruction_1 = "forward 5"
    instruction_2 = "down 3"
    result_1 = read_instruction(instruction_1)
    result_2 = read_instruction(instruction_2)
    assert result_1 == ["forward", "5"]
    assert result_2 == ["down", "3"]


def test_forward_instruction():
    instruction = ["forward", "5"]
    position = {"horizontal": 3, "depth": 0}
    new_position = apply_instruction(instruction, position)
    assert new_position == {"horizontal": 8, "depth": 0}


def test_down_instruction():
    instruction = ["down", "5"]
    position = {"horizontal": 0, "depth": 4}
    new_position = apply_instruction(instruction, position)
    assert new_position == {"horizontal": 0, "depth": 9}


def test_up_instruction():
    instruction = ["up", "5"]
    position = {"horizontal": 0, "depth": 10}
    new_position = apply_instruction(instruction, position)
    assert new_position == {"horizontal": 0, "depth": 5}


def test_with_test_instruction_have_result():
    input = read_file(path)
    instructions = [read_instruction(instruction) for instruction in input]
    result = apply_instructions(instructions)
    assert result == {"horizontal": 15, "depth": 10}


def test_main_result_with_test():
    result = main(path)
    assert result == 150


def test_forward_instruction_with_aim():
    instruction = ["forward", "5"]
    position = {"horizontal": 3, "depth": 0, "aim": 5}
    new_position = apply_instruction_with_aim(instruction, position)
    assert new_position == {"horizontal": 8, "depth": 25, "aim": 5}


def test_down_instruction_with_aim():
    instruction = ["down", "5"]
    position = {"horizontal": 0, "depth": 4, "aim": 5}
    new_position = apply_instruction_with_aim(instruction, position)
    assert new_position == {"horizontal": 0, "depth": 4, "aim": 10}


def test_up_instruction_with_aim():
    instruction = ["up", "5"]
    position = {"horizontal": 0, "depth": 10, "aim": 10}
    new_position = apply_instruction_with_aim(instruction, position)
    assert new_position == {"horizontal": 0, "depth": 10, "aim": 5}


def test_main_result_with_test():
    result = main(path)
    assert result["result"] == 150
    assert result["result_with_aim"] == 900
