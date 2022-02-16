from src.arrays.max_sum_subarray import get_max_sum

def test_empty_array_has_zero_sum():
    arr = []
    assert get_max_sum(arr) == 0

def test_computes_max_sum():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    assert get_max_sum(arr) == 7
