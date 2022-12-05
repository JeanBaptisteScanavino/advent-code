from ..utils.InputReader import InputReader
from .fixture import cleanup_test
from ..utils.Cleanup import Cleanup

def test_get_group_with_range():
    test = Cleanup.get_group_with_range(cleanup_test)
    result = [[['2', '4'], ['6', '8']], [['2', '3'], ['4', '5']], [['5', '7'], ['7', '9']], [['2', '8'], ['3', '7']], [['6', '6'], ['4', '6']], [['2', '6'], ['4', '8']]]
    assert test == result


def test_one_is_totaly_in_range():
    groups=Cleanup.get_group_with_range(cleanup_test)
    test_0 = Cleanup.one_is_totaly_in_range(groups[0])
    result_0 = False
    test_3 = Cleanup.one_is_totaly_in_range(groups[3])
    result_3 = True
    test_4 = Cleanup.one_is_totaly_in_range(groups[4])
    result_4 = True
    test_strange = Cleanup.one_is_totaly_in_range([['4', '5'], ['5', '15']])
    result_strange = False
    assert test_0 == result_0
    assert test_3 == result_3
    assert test_4 == result_4
    assert test_strange == result_strange
def test_how_many_totaly_in_range():
    test = Cleanup.how_many_totaly_in_range(cleanup_test)
    result = 2
    assert test == result

def test_one_is_overlaping():
    groups=Cleanup.get_group_with_range(cleanup_test)
    test_0 = Cleanup.one_is_overlapping(groups[0])
    result_0 = False
    test_3 = Cleanup.one_is_overlapping(groups[3])
    result_3 = True
    test_4 = Cleanup.one_is_overlapping(groups[4])
    result_4 = True
    test_strange = Cleanup.one_is_overlapping([['4', '5'], ['5', '15']])
    result_strange = True
    assert test_0 == result_0
    assert test_3 == result_3
    assert test_4 == result_4
    assert test_strange == result_strange

def test_how_many_overlap():
    test = Cleanup.how_many_overlap(cleanup_test)
    result = 4
    assert test == result

