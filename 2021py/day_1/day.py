# pylint: disable=unused-variable
def read_file(file_to_read):
    reading_file = open(file_to_read, "r")
    readed_file = reading_file.read().split('\n')
    reading_file.close()
    return readed_file

def make_int(data):
    return int(data)

def is_increase(first, second):
    if first - second < 0:
        return True
    return False 

def count_increase(data):
    count = 0
    loop_length = len(data) -1
    for x in range(loop_length):
        if is_increase(data[x], data[x+1]):
            count += 1
    return count

def count_increase_with_windows(data):
    count = 0
    loop_length = len(data) -3
    for x in range(loop_length):
        window_1 = make_windows(data,x)
        window_2 = make_windows(data,x+1)
        if is_increase(window_1, window_2):
            count += 1
    return count

def main():
    input_data = read_file("./day_1/input.txt")
    input_data_int = []
    for data in input_data:
        input_data_int.append(make_int(data))
    result = count_increase(input_data_int)
    print(result)
    second_result = count_increase_with_windows(input_data_int)
    print(second_result)    

def make_windows(data, first_number):
    window = []
    for x in range(first_number, first_number + 3):
        window.append(data[x])
    return sum(window)

main()
