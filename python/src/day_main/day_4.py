from utils.utils import make_int, read_file
import numpy as np

day = 4
input_path = f"/input/input_day_{day}.txt"

def retrieve_line(input_data):
    line_array =  input_data.split(' ')
    return [int(number.strip(), 10)for number in line_array if number != '']
    
def make_one_grill(big_data):
    return [retrieve_line(line) for line in big_data if line != '']

def retrieve_bingo(data):
    number = data.split(",")
    return [make_int(nb) for nb in number]

def make_grill(data):
    data_array = np.array(data)
    print(np.array_split(data_array,len(data)/5))


def main(input_file):
    input_data = read_file(input_file)
    result = "result"
    return result


main(input_path)
