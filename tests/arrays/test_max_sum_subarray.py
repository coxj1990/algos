from src.arrays.max_sum_subarray import get_max_sum

def test_trivial():
    L = []
    assert get_max_sum(L) == 0

def test_nontrivial():
    L = [-2, -3, 4, -1, -2, 1, 5, -3]
    assert get_max_sum(L) == 7
