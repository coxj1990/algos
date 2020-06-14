from src.arrays.permutations import get_perms

def test_trivial():
    perms = get_perms('')
    assert perms == []

def test_nontrivial():
    perms = get_perms('abc')
    res = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert set(perms) == set(res)
