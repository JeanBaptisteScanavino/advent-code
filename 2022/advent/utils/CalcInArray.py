class CalcInArray:
    def get_highter_of_array(array):
        return max(array)

    def get_tree_highter_of_array(array):
        array.sort(reverse=True)
        return array[0] + array[1] + array[2]
