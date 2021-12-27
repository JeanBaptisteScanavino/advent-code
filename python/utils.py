def read_file(file_to_read):
    reading_file = open(file_to_read, "r")
    readed_file = reading_file.read().split('\n')
    reading_file.close()
    return readed_file

def make_int(data):
    return int(data)