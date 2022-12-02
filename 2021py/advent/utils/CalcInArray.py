class CalcInArray:
    def get_highter_of_array(array):
        return max(array)

    def get_tree_highter_of_array(array):
        array.sort(reverse=True)
        return array[0] + array[1] + array[2]

    def get_increased_count(array):
        count = 0
        for i, x in enumerate(array):
            if i < len(array) - 1 and int(x) < int(array[i + 1]):
                count += 1
        return count

    def create_group_by_three(array):
        group = []
        for i, x in enumerate(array):
            if i < len(array) - 2:
                group.append(str(int(x) + int(array[i + 1]) + int(array[i + 2])))
        return group

    def kept_bits_with_x_in_position_y(array, bit, pos):
        result = []
        for i, x in enumerate(array):
            if x[pos] == str(bit):
                result.append(x)
        return result
