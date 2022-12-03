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
