from src.bits.bitwise_and_range import bitwise_and_range

def test_trivial():
    assert bitwise_and_range(0, 1) == 0

def test_nontrivial():
    assert bitwise_and_range(5, 7) == 4
