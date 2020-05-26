from src.arrays.string_matching import search

def test_trivial():
    assert not search('', 'x')

def test_nontrivial_true():
    assert search('test', 'est')

def test_nontrivial_false():
    assert not search('test', 'se')
