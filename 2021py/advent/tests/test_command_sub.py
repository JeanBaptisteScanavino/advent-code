from ..utils.CommandSubmarine import CommandSubmarine


def test_get_submarine_order():
    test = CommandSubmarine.get_order("forward 2")
    expect = ["forward", "2"]
    assert test == expect


def test_forward_increase_x():
    test = CommandSubmarine.apply_order(["forward 2"])
    expect = [2, 0]
    assert test == expect


def test_down_increase_depht():
    test = CommandSubmarine.apply_order(["down 5"])
    expect = [0, 5]
    assert test == expect


def test_up_decrease_depht():
    test = CommandSubmarine.apply_order(["up 5"])
    expect = [0, -5]
    assert test == expect


def test_get_submarine_position():
    test = CommandSubmarine.get_submarine_position([10, 15])
    expect = 150
    assert test == expect


def test_forward_increase_x():
    test = CommandSubmarine.apply_real_order(["down 5", "forward 2"])
    expect = [2, 10, 5]
    assert test == expect


def test_down_increase_aim():
    test = CommandSubmarine.apply_real_order(["down 5"])
    expect = [0, 0, 5]
    assert test == expect


def test_up_decrease_aim():
    test = CommandSubmarine.apply_real_order(["up 5"])
    expect = [0, 0, -5]
    assert test == expect
