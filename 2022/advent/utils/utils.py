import os

my_path = os.path.abspath(os.path.dirname(__file__))


class InputReader:
    def myutils():
        return "utils"

    def read_file(file_to_read):

        path = f"{my_path}/../input/{file_to_read}"
        reading_file = open(path, "r")
        readed_file = reading_file.read().split("\n")
        reading_file.close()
        return readed_file

    def make_group_in_array(file):
        elf_kcal = 0
        result = []
        for i, x in enumerate(file):
            if x == "":
                result.append(elf_kcal)
                elf_kcal = 0
            elif i == len(file) - 1:
                elf_kcal += int(x)
                result.append(elf_kcal)
            else:
                elf_kcal += int(x)
        return result

    def return_splited_with_space(file):
        result = []
        for i in file:
            result.append(i.split(" "))
        return result


class CalcInArray:
    def get_highter_of_array(array):
        return max(array)

    def get_tree_highter_of_array(array):
        array.sort(reverse=True)
        return array[0] + array[1] + array[2]


class ElfGame:
    def win_or_loose(array):
        if array == ["A", "Y"] or array == ["B", "Z"] or array == ["C", "X"]:
            return "win"
        elif array == ["A", "Z"] or array == ["B", "X"] or array == ["C", "Y"]:
            return "loose"
        elif array == ["A", "X"] or array == ["B", "Y"] or array == ["C", "Z"]:
            return "draw"
        else:
            return "error"

    def how_many_points_with_result(result):
        if result == "win":
            return 6
        elif result == "loose":
            return 0
        elif result == "draw":
            return 3
        else:
            return "error"

    def how_many_points_with_RPS(rps):
        if rps == "X":
            return 1
        elif rps == "Y":
            return 2
        elif rps == "Z":
            return 3

    def make_game(games):
        score = 0
        for game in games:
            result = ElfGame.win_or_loose(game)
            points_game = ElfGame.how_many_points_with_result(result)
            points_rps = ElfGame.how_many_points_with_RPS(game[1])
            score += points_game + points_rps
        return score

    def make_real_game(games):
        score = 0
        points_game = ElfGame.real_second_column_result(games)
        real_game = ElfGame.what_did_i_play(games)
        points_rps = 0
        for game in real_game:
            points_rps += ElfGame.how_many_points_with_RPS(game[1])
        score += points_game + points_rps
        return score

    def real_second_column_result(games):
        score = 0
        for game in games:
            if game[1] == "X":
                score += 0
            elif game[1] == "Y":
                score += 3
            elif game[1] == "Z":
                score += 6
        return score

    def what_did_i_play(games):
        real_game = []
        for game in games:
            if game[0] == "A":
                if game[1] == "X":
                    real_game.append(["A", "Z"])
                elif game[1] == "Y":
                    real_game.append(["A", "X"])
                elif game[1] == "Z":
                    real_game.append(["A", "Y"])
            elif game[0] == "B":
                if game[1] == "X":
                    real_game.append(["B", "X"])
                elif game[1] == "Y":
                    real_game.append(["B", "Y"])
                elif game[1] == "Z":
                    real_game.append(["B", "Z"])
            elif game[0] == "C":
                if game[1] == "X":
                    real_game.append(["C", "Y"])
                elif game[1] == "Y":
                    real_game.append(["C", "Z"])
                elif game[1] == "Z":
                    real_game.append(["C", "X"])
        return real_game
