from src.trees.make_trie import make_trie

def test_make_one_word_trie():
    words = ['test']
    trie = {'t': {'e': {'s': {'t': {'end': 'end'}}}}}
    assert make_trie(words) == trie

def test_make_multiple_word_trie():
    words = ['bar', 'baz']
    trie = {'b': {'a': {'z': {'end': 'end'}, 'r': {'end': 'end'}}}}
    assert make_trie(words) == trie
