from src.arrays.are_anagrams import are_anagrams

def test_false():
    return not are_anagrams('abc', 'abd')

def test_true():
    return are_anagrams('listen', 'silent')
