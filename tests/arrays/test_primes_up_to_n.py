from src.arrays.primes_up_to_n import get_primes

def test_trivial():
    res = get_primes(1)
    assert res == []

def test_nontrivial():
    res = get_primes(10)
    print(res)
    assert res == [2, 3, 5, 7]
