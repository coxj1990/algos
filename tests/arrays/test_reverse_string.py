from src.arrays.reverse_string import reverse

def test_trivial():
    assert reverse('') == ''

def test_nontrivial():
    assert reverse('hello') == 'olleh'
