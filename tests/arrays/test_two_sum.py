from src.arrays.two_sum import two_sum

def test_trivial_found():
    L = [1, 2]
    assert two_sum(L, 3) == (0, 1)

def test_trivial_not_found():
    L = [1, 2]
    assert two_sum(L, 1) == -1

def test_nontrivial():
    L = [15, 11, 2, 7]
    assert two_sum(L, 9) == (2, 3)
