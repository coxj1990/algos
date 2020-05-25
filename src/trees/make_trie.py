def make_trie(words):
    trie = {}
    for word in words:
        curr = trie
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['end'] = 'end'
    return trie
