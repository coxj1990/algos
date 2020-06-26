from src.arrays.is_rotation import is_rotation

def test_false():
    assert not is_rotation('abc', 'bac')

def test_true():
    assert is_rotation('abc', 'cab')
