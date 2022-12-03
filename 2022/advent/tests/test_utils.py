from ..utils.InputReader import InputReader
from ..utils.CalcInArray import CalcInArray
from ..utils.ElfGame import ElfGame


def test_read_input_file():
    test = InputReader.read_file("/test_day_1.txt")
    result = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    assert test == result


def test_make_group_in_array():
    test = InputReader.make_group_in_array(InputReader.read_file("test_day_1.txt"))
    result = [6000, 4000, 11000, 24000, 10000]
    assert test == result


def test_get_highter_of_array():
    test = CalcInArray.get_highter_of_array([6000, 4000, 11000, 24000, 10000])
    result = 24000
    assert test == result


def test_get_tree_highter_of_array():
    test = CalcInArray.get_tree_highter_of_array([6000, 4000, 11000, 24000, 10000])
    result = 45000
    assert test == result


def test_is_win_loose_draw():
    test_win_1 = ElfGame.win_or_loose(["A", "Y"])
    test_loose = ElfGame.win_or_loose(["B", "X"])
    test_draw = ElfGame.win_or_loose(["C", "Z"])
    result_win = "win"
    result_loose = "loose"
    result_draw = "draw"
    assert test_win_1 == result_win
    assert test_loose == result_loose
    assert test_draw == result_draw


def test_how_many_points_with_result():
    test_win = ElfGame.how_many_points_with_result("win")
    test_loose = ElfGame.how_many_points_with_result("loose")
    test_draw = ElfGame.how_many_points_with_result("draw")
    result_win = 6
    result_loose = 0
    result_draw = 3
    assert test_win == result_win
    assert test_loose == result_loose
    assert test_draw == result_draw


def test_how_many_points_with_RPS():
    test_rock = ElfGame.how_many_points_with_RPS("X")
    test_paper = ElfGame.how_many_points_with_RPS("Y")
    test_scissors = ElfGame.how_many_points_with_RPS("Z")
    result_rock = 1
    result_paper = 2
    result_scissors = 3
    assert test_rock == result_rock
    assert test_paper == result_paper
    assert test_scissors == result_scissors


def test_return_splited_with_space():
    test = InputReader.return_splited_with_space(["A B", "C D", "E F"])
    result = [["A", "B"], ["C", "D"], ["E", "F"]]
    assert test == result


def test_make_game():
    test = ElfGame.make_game([["A", "Y"], ["B", "X"], ["C", "Z"]])
    result = 15
    assert test == result


def test_real_second_column_result():
    test = ElfGame.real_second_column_result([["A", "Y"], ["B", "X"], ["C", "Z"]])
    result = 9
    assert test == result


def test_what_did_i_play():
    test = ElfGame.what_did_i_play([["A", "Y"], ["B", "X"], ["C", "Z"]])
    result = [["A", "X"], ["B", "X"], ["C", "X"]]
    assert test == result
