import os

my_path = os.path.abspath(os.path.dirname(__file__))

def read_file(file_to_read):
    path = f'{my_path}{file_to_read}'
    reading_file = open(path, "r")
    readed_file = reading_file.read().split("\n")
    reading_file.close()
    return readed_file

def make_int(data):
    return int(data)
