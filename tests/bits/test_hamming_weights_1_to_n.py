from src.bits.hamming_weights_1_to_n import hamming_weights

def test_trivial():
    assert hamming_weights(0) == [0]

def test_nontrivial():
    assert hamming_weights(5) == [0, 1, 1, 2, 1, 2]
