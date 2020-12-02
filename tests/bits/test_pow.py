from src.bits.pow import pow

def test_zero_exp():
    assert pow(2, 0) == 1

def test_one_exp():
    assert pow(2, 1) == 2

def test_positive_exp():
    assert pow(2, 3) == 8

def test_negative_exp():
    assert abs(pow(2, -3) - 0.125) < 0.01
