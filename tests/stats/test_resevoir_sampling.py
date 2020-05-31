from src.stats.resevoir_sampling import Resevoir
from collections import Counter

def normalize(counter):
    total = sum(counter.values(), 0.0)
    for key in counter:
        counter[key] /= total

def test_trivial():
    r = Resevoir(1)
    r.add(0)
    assert r.sample() == 0

def test_nontrivial():
    n_sims = 1000
    c = Counter()
    for _ in range(n_sims):
        r = Resevoir(2)
        for num in range(3):
            r.add(num)
        c[r.sample()] += 1
    normalize(c)
    assert abs(c[0] - 0.33) < 0.1
