from src.arrays.longest_consecutive_subsequence import lcs

def test_trivial():
    L = []
    assert lcs(L) == 0

def test_nontrivial():
    L = [100, 4, 200, 1, 3, 2]
    assert lcs(L) == 4
