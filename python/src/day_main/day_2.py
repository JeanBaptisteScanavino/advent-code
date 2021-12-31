# pylint: disable=unused-variable
from utils.utils import make_int, read_file


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


def apply_instruction_with_aim(instruction, position):
    if instruction[0] == "forward":
        position["horizontal"] += make_int(instruction[1])
        position["depth"] += position["aim"] * make_int(instruction[1])
    elif instruction[0] == "down":
        position["aim"] += make_int(instruction[1])
    elif instruction[0] == "up":
        position["aim"] -= make_int(instruction[1])
    return position


def apply_instructions_with_aim(instructions):
    position = {"horizontal": 0, "depth": 0, "aim": 0}
    for instruction in instructions:
        position = apply_instruction_with_aim(instruction, position)
    return position


def main(input_file):
    input = read_file(input_file)
    instructions = [read_instruction(instruction) for instruction in input]
    final_position = apply_instructions(instructions)
    final_position_with_aim = apply_instructions_with_aim(instructions)
    result = final_position["horizontal"] * final_position["depth"]
    result_with_aim = (
        final_position_with_aim["horizontal"] * final_position_with_aim["depth"]
    )
    return {"result": result, "result_with_aim": result_with_aim}


result = main("/input/input_day_2.txt")
print(result)
