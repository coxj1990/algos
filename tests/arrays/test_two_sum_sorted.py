from src.arrays.two_sum_sorted import two_sum_sorted

def test_trivial_found():
    L = [1, 2]
    assert two_sum_sorted(L, 3) == (0, 1)

def test_trivial_not_found():
    L = [1, 2]
    assert two_sum_sorted(L, 1) == -1

def test_nontrivial():
    L = [2, 7, 11, 15]
    assert two_sum_sorted(L, 18) == (1, 2)
