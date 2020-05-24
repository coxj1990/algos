from collections import Counter

def get_first_nonrepeated(s):
    c = Counter(s)
    for e in s:
        if c[e] == 1:
            return e
