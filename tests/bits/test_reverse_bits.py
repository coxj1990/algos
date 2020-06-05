from src.bits.reverse_bits import reverse

def test_trivial():
    assert reverse(1) == 1

def test_nontrivial():
    assert reverse(22) == 13
