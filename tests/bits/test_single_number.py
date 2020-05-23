from src.bits.single_number import get_single

def test_trivial():
    L = [1]
    assert get_single(L) == 1

def test_nontrivial():
    L = [1, 3, 3, 4, 1]
    assert get_single(L) == 4
