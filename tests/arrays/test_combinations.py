from src.arrays.combinations import get_combs

def test_trivial():
    combs = get_combs(1, 1)
    res = [[1]]
    assert combs == res

def test_nontrivial():
    combs = get_combs(3, 2)
    res = [[1, 2], [1, 3], [2, 3]]
    assert combs == res
