from src.arrays.num_subarrays_with_odd_sum import num_subarrays_with_odd_sum as f

def test_all_odds():
    L = [1, 3, 5]
    assert f(L) == 4

def test_mix():
    L = range(1, 8)
    assert f(L) == 16
