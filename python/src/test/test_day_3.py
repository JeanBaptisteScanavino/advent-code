from ..day_main.day_3 import main, get_bits, most_bit, inverse_table,most_bit_with_count, find_oxygen, find_life_support,find_C02
from ..day_main.utils.utils import read_file, make_int

day = 3
in_memory_path = f"/in_memory/test_day_{day}.txt"


def test_get_bit_in_array_from_a_bytes():
    initial_table = "00101"
    result = get_bits(initial_table)
    assert result == ["0", "0", "1", "0", "1"]

def test_most_bit_in_array():
    input_most_zero = ["0", "0", "1", "0", "1", "1", "0"]
    input_most_one = ["1", "1", "1", "0", "1", "1", "0"]
    result_most_zero = most_bit(input_most_zero)
    result_most_one = most_bit(input_most_one)
    assert result_most_zero == "0"
    assert result_most_one == "1"
    
def test_most_bit__with_count_in_array():
    input_most_zero = ["0", "0", "1", "0", "1", "1", "0"]
    input_most_one = ["1", "1", "1", "0", "1", "1", "0"]
    result_most_zero = most_bit_with_count(input_most_zero)
    result_most_one = most_bit_with_count(input_most_one)
    assert result_most_zero == {"most": "0", "count": 4}
    assert result_most_one == {"most": "1", "count": 5}

def test_inverse_table():
    input = ["0", "0", "1", "0", "1", "1", "0"]
    result = inverse_table(input)
    assert result == ["1", "1", "0", "1", "0", "0", "1"]

def test_find_oxygen_generator():
    input_data = read_file(in_memory_path)
    array_of_data = [get_bits(data) for data in input_data]
    result = find_oxygen(array_of_data)
    assert result == 23

def test_find_C02_rating():
    input_data = read_file(in_memory_path)
    array_of_data = [get_bits(data) for data in input_data]
    result = find_C02(array_of_data)
    assert result == 10


def test_main_result_with_test():
    result = main(in_memory_path)
    assert result["power"] == 198
    assert result["life"] == 230
