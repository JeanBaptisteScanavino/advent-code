from .InputReader import InputReader

class Cleanup:

    def get_group_with_range(list):
        groups = [InputReader.split_string_with_char(g,',') for g in list]
        new_group =  []
        for g in groups:
            new_group.append([ InputReader.split_string_with_char(e,'-') for e in g])
        return new_group 
    
    def one_is_totaly_in_range(g):
        if int(g[0][0]) >= int(g[1][0]) and int(g[0][1]) <= int(g[1][1]):
            return True
        if int(g[1][0]) >= int(g[0][0]) and int(g[1][1]) <= int(g[0][1]):
            return True
        return False
    
    def how_many_totaly_in_range(file):
        groups = Cleanup.get_group_with_range(file)
        count = 0
        for group in groups:
            if Cleanup.one_is_totaly_in_range(group):
                count +=1
        return count
    
    def one_is_overlapping(g):
        e_11 = int(g[0][0])
        e_12 = int(g[0][1])
        e_21 = int(g[1][0])
        e_22 = int(g[1][1])
        if e_11 >= e_21 and e_11 <= e_22 or e_12 <= e_22 and e_12 >= e_21:
            return True
        if e_21 >= e_11 and e_22 <= e_12:
            return True
        return False

    def how_many_overlap(file):
        groups = Cleanup.get_group_with_range(file)
        count = 0
        for group in groups:
            if Cleanup.one_is_overlapping(group):
                count +=1
        return count
