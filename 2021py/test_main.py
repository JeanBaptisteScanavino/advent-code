from main import read_file

def test_read_file_should_respond_this():
    assert read_file("main.txt") == ['coucou', 'le test', 'en python']


