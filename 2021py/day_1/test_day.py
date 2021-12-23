from day import main, read_file, is_increase


def test_is_increase():
    first = 2
    second = 10
    passed = is_increase(first,second)
    failed = is_increase(second,first)
    assert failed == False
    assert passed == True

def test_count_increase():
    data = read_file('test.txt')
    result = count_increase(data)
    assert result == 7