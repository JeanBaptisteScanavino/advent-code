def read_file(file_to_read):
    reading_file = open(file_to_read, "r")
    readed_file = reading_file.read().split('\n')
    reading_file.close()
    return readed_file


def main():
    return read_file("main.txt")
     
