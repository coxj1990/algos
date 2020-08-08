from src.arrays.powerset_iterative import powerset_iterative

def test_trivial():
    L = []
    res = powerset_iterative(L)
    assert res == set([()])

def test_nontrivial():
    L = [1, 2, 3]
    res = powerset_iterative(L)
    expected = set([(), (3,), (2,), (2, 3), (1,), (1, 3), (1, 2), (1, 2, 3)])
    assert res == expected
