from textwrap import wrap


class PlayWithString:
    def split_in_two(s):
        wrap_count = len(s) / 2
        return wrap(s, int(wrap_count))

    def count_char(s, c):
        return s.count(c)

    def is_in_two_string(line):
        com_char = []
        pos = 0
        print(line)
        while len(com_char) == 0:

            if PlayWithString.count_char(
                line[0], line[0][pos]
            ) == 1 and PlayWithString.count_char(line[1], line[0][pos]) == 1:
                com_char.append(line[0][pos])
            pos += 1
        return com_char[0]

    def calc_priority(file):
        all_line = []
        for line in file:
            all_line.append(PlayWithString.split_in_two(line))
        charact = []
        for line in all_line:
            charact.append(PlayWithString.is_in_two_string(line))
        print(charact)
