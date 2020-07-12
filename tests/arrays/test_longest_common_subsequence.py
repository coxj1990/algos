from src.arrays.longest_common_subsequence import lcs

def test_trivial():
    assert lcs('a', 'a') == 1

def test_nontrivial():
    assert lcs('abcd', 'acbad') == 3
