from src.arrays.is_palindrome import is_palindrome

def test_false():
    assert not is_palindrome('test')

def test_true():
    assert is_palindrome('racecar')
