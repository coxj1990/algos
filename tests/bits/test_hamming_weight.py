from src.bits.hamming_weight import hamming_weight

def test_trivial():
    assert hamming_weight(0) == 0

def test_nontrivial():
    assert hamming_weight(11) == 3
