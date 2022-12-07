import numpy as np
class Transmission:

    def is_there_identics_char(string):
        for char in string:
            if string.count(char) > 1:
                return True
        return False
    
    def get_index_first_marker(string, nb_of_char=4):
        arr = np.array(string)
        for i, char in enumerate(string):
            if not Transmission.is_there_identics_char(string[i:i+nb_of_char]):
                return i + nb_of_char 
        return -1