import os

my_path = os.path.abspath(os.path.dirname(__file__))


class InputReader:
    def myutils():
        return "utils"

    def read_file(file_to_read):

        path = f"{my_path}/../input/{file_to_read}"
        reading_file = open(path, "r")
        readed_file = reading_file.read().split("\n")
        reading_file.close()
        return readed_file

    def make_group_in_array(file):
        elf_kcal = 0
        result = []
        for i, x in enumerate(file):
            if x == "":
                result.append(elf_kcal)
                elf_kcal = 0
            elif i == len(file) - 1:
                elf_kcal += int(x)
                result.append(elf_kcal)
            else:
                elf_kcal += int(x)
        return result

class CalcInArray():
    def get_highter_of_array(array):
        return max(array)

    def get_tree_highter_of_array(array):
        array.sort(reverse=True)
        return array[0] + array[1] + array[2]

    def get_increased_count(array):
        count =0
        for i,x in enumerate(array):
            if i < len(array)-1 and int(x) < int(array[i+1]):
                count +=1
        return count
    
    def create_group_by_three(array):
        group = []
        for i,x in enumerate(array):
            if i < len(array)-2:
                group.append(str(int(x) + int(array[i+1]) + int(array[i+2])))
        return group
    
    def kept_bits_with_x_in_position_y(array, bit, pos):
        result = []
        for i,x in enumerate(array):
            if  x[pos] == bit:
                result.append(x)
        return result

class CommandSubmarine:

    def get_order(order):
        return order.split(" ")
    
    def apply_order(orders):
        x = 0
        depth = 0
        for order in orders:
            real_order = CommandSubmarine.get_order(order)
            if real_order[0] == "forward":
                x += int(real_order[1])
            elif real_order[0] == "down":
                depth += int(real_order[1])
            elif real_order[0] == "up":
                depth -= int(real_order[1])
        return [x, depth]

    def apply_real_order(orders):
        x = 0
        depth = 0
        aim = 0
        for order in orders:
            real_order = CommandSubmarine.get_order(order)
            if real_order[0] == "forward":
                x += int(real_order[1])
                depth += int(real_order[1]) * aim
            elif real_order[0] == "down":
                aim += int(real_order[1])
            elif real_order[0] == "up":
                aim -= int(real_order[1])
        return [x, depth, aim]
    
    def get_submarine_position(postion):
        return postion[0] * postion[1]

class Diagnostic:
    def get_gamma_bit(bits):
        lenght = len(bits)
        z = bits.count("0")
        if z > lenght /2:
            return "0"
        return "1"
    
    def get_epsilon_bits(gamma):
        epsilon  = []
        for b in gamma:
            if b == "0":
                epsilon.append('1')
            else:
                epsilon.append('0')
        return ''.join(epsilon)
    
    def get_gamma_bits(seq):
        gamma =[]
        for i in range(len(seq[0])):
            to_send=[]
            for s in seq:
                to_send.append(s[i])
            gamma.append(Diagnostic.get_gamma_bit(to_send))
        return ''.join(gamma)
            
    def get_oxygen_bits(seq,gamma):
        oxy = []
        new_seq = seq
        for i in range(len(gamma)):
            if len(new_seq) > 1:
                new_seq = CalcInArray.kept_bits_with_x_in_position_y(new_seq, gamma[i],i)
        return new_seq


class ClassicCalc:

    def get_decimal_from_bin(bina):
        return int(bina,2)