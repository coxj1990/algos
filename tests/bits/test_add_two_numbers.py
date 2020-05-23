from src.bits.add_two_numbers import add

def test_trivial():
    assert add(0, 0) == 0

def test_nontrivial():
    assert add(3, 1) == 4
