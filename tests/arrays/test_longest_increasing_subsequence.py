from src.arrays.longest_increasing_subsequence import lis

def test_trivial():
    L = []
    assert lis(L) == 0

def test_nontrivial():
    L = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert lis(L) == 6
