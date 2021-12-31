from .day_main.utils.utils import read_file, make_int

path = '/main.txt'

def test_main_file_should_respond_this():
    assert read_file(path) == ["coucou", "le test", "en python"]


def test_tranform_string_to_int():
    string = "201"
    result = make_int(int(string))
    assert result == 201


def test_main():
    assert True == True
