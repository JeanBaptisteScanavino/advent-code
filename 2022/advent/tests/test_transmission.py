from ..utils.Transmission import Transmission



def test_there_identics_char():
    test_one = Transmission.is_there_identics_char('abca')
    test_two = Transmission.is_there_identics_char('abcb')
    test_three = Transmission.is_there_identics_char('abcc')
    test_four = Transmission.is_there_identics_char('abcd')
    assert test_one == True
    assert test_two == True
    assert test_three == True
    assert test_four == False

input_test_one ='bvwbjplbgvbhsrlpgdmjqwftvncz'
input_test_two ='nppdvjthqldpwncqszvftbrmjlhg'
input_test_three ='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
input_test_four ='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

def test_get_index_first_marker():
    test_one = Transmission.get_index_first_marker(input_test_one)
    test_two = Transmission.get_index_first_marker(input_test_two)
    test_three = Transmission.get_index_first_marker(input_test_three)
    test_four = Transmission.get_index_first_marker(input_test_four)
    assert test_one == 5
    assert test_two == 6
    assert test_three == 10
    assert test_four == 11

