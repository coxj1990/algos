from collections import Counter

def all_counts_unique(L):
    counts = Counter(L)
    return len(counts) == len(set(counts.values()))
