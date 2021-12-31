from ..day_main.day_4 import main, make_one_grill, retrieve_bingo, retrieve_line, make_grill
from ..day_main.utils.utils import make_int, read_file

day = 4
in_memory_path = f'/in_memory/test_day_{day}.txt'

def test_retrieve_bingo_number_in_an_array():
    input_data = read_file(in_memory_path)
    bingo_number = retrieve_bingo(input_data[0])
    assert bingo_number == [7, 4, 9, 5, 11, 17, 23 ,2 ,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

def test_restrieve_grill_line_by_colum():
    input_data = '22 13 17 11  0'
    line = retrieve_line(input_data)
    assert line == [22, 13, 17, 11, 0]

def test_make_a_bingo_grill():
    input_data = read_file(in_memory_path)
    grill = make_one_grill(input_data[2:8])
    assert grill == [[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]]

def test_make_grill_separation():
    input_data = read_file(in_memory_path)
    line_data = retrieve_line(input_data)
    grill = make_grill(input_data[2:len(line_data)])
    assert grill ==[[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]]

def test_main_result_with_test():
    result = main(in_memory_path)
    assert result == 1
