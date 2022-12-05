from .InputReader import InputReader
from .CalcInArray import CalcInArray
import numpy as np
class CraneCrate:

    def extract_crate(inputs,col_nb):
        index_of_crate = CraneCrate.get_index_of_char_in_string(inputs[len(inputs)-1])
        crates = []
        inputs = inputs[:len(inputs)-1]
        for j in index_of_crate:
            col =  [line[j] for line in inputs if line[j] != ' ']
            crates.append(col)
        return crates
    
    def get_number_of_column(input)->  int:
        columns = InputReader.split_string_with_char(input,' ')
        return int(CalcInArray.get_highter_of_array(columns))
    
    def get_index_of_char_in_string(input)-> list[int]:
        index = []
        for i in range(len(input)):
            if input[i] != ' ':
                index.append(i)
        return index
    
    def get_commands(commands):
        full_commands = [InputReader.split_string_with_char(command,' ') for command in commands]
        command_in_int = []
        words = ['move','from','to']
        for command in full_commands:
            int_command = [int(com) for com in command if com not in words]
            command_in_int.append(int_command)
        return command_in_int
    
    def move_a_crate(commands,crates):
        for i in range(int(commands[0])):
            crate_to_move = crates[commands[1]-1].pop(0)
            crates[commands[2]-1].insert(0,crate_to_move)
        return crates

    def get_first_crates_after_move(inputs):
        [inputs,commands] = InputReader.split_inputs_with_n(inputs)
        number_of_columns = CraneCrate.get_number_of_column(inputs[len(inputs)-1])
        crates = CraneCrate.extract_crate(inputs,number_of_columns)
        commands = CraneCrate.get_commands(commands)
        for command in commands:
            crates = CraneCrate.move_a_crate(command,crates)
        result = [col[0] for col in crates]
        return ''.join(result)
    
    def move_crate_with_crate_mover_9001(command,crates):
        print(command)
        crates_to_move = crates[command[1]-1][:command[0]]
        print(crates[command[1]-1])
        for i in range(command[0]):
            crates[command[1]-1].pop(0)
        new_array = crates_to_move + crates[command[2]-1]
        crates[command[2]-1].clear()
        crates[command[2]-1] = new_array
        return crates

    def get_first_crates_after_move_9001(inputs):
        [inputs,commands] = InputReader.split_inputs_with_n(inputs)
        number_of_columns = CraneCrate.get_number_of_column(inputs[len(inputs)-1])
        crates = CraneCrate.extract_crate(inputs,number_of_columns)
        commands = CraneCrate.get_commands(commands)
        for command in commands:
            crates = CraneCrate.move_crate_with_crate_mover_9001(command,crates)
        result = [col[0] for col in crates]
        return ''.join(result)