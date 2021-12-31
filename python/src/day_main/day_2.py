# pylint: disable=unused-variable
from .utils.utils import make_int, read_file


def read_instruction(instruction):
    return instruction.split(" ")


def apply_instruction(instruction, position):
    if instruction[0] == "forward":
        position["horizontal"] += make_int(instruction[1])
    elif instruction[0] == "down":
        position["depth"] += make_int(instruction[1])
    elif instruction[0] == "up":
        position["depth"] -= make_int(instruction[1])
    return position


def apply_instructions(instructions):
    position = {"horizontal": 0, "depth": 0}
    for instruction in instructions:
        position = apply_instruction(instruction, position)
    return position


def main(input_file):
    input = read_file(input_file)
    instructions = [read_instruction(instruction) for instruction in input]
    final_position = apply_instructions(instructions)
    return final_position["horizontal"] * final_position["depth"]



if __name__ == "__main__":
    result = main("./input/input_day_2.txt")
    print(result)

