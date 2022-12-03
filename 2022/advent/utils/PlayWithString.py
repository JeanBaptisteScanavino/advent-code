from textwrap import wrap
import string
import numpy

class PlayWithString:
    def split_in_two(s):
        wrap_count = len(s) / 2
        return wrap(s, int(wrap_count))

    def count_char(s, c):
        return s.count(c)

    def is_in_two_string(line):
        com_char = []
        pos = 0
        while len(com_char) == 0:
            if PlayWithString.count_char(
                line[0], line[0][pos]
            ) > 0 and PlayWithString.count_char(line[1], line[0][pos] )> 0:
                com_char.append(line[0][pos])
            pos += 1
        return com_char[0]

    def is_in_three_string(line):
        com_char = []
        pos = 0
        while len(com_char) == 0:
            if PlayWithString.count_char(
                line[0], line[0][pos]
            ) > 0 and PlayWithString.count_char(line[1], line[0][pos] )> 0 and PlayWithString.count_char(line[2], line[0][pos] )> 0 :
                com_char.append(line[0][pos])
            pos += 1
        return com_char[0]
  
    def calc_char_priority(char):
        return string.ascii_letters.index(char) +1
    
    def calc_priority(file):
        all_line = []
        for line in file:
            all_line.append(PlayWithString.split_in_two(line))
        charact = []
        for line in all_line:
            charact.append(PlayWithString.is_in_two_string(line))
        result = 0
        for char in charact:
            result += PlayWithString.calc_char_priority(char)
        return result

    def calc_real_priority(file):
        charact = []
        arr = numpy.array(file)
        for x in range(0, len(file), 3):
            charact.append(PlayWithString.is_in_three_string(arr[x:x+3]))
        result = 0
        for char in charact:
            result += PlayWithString.calc_char_priority(char)
        return result
    