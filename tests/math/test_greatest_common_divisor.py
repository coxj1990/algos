from src.math.greatest_common_divisor import get_gcd

def test_trivial():
    gcd = get_gcd(1, 1)
    return gcd == 1

def test_nontrivial():
    gcd = get_gcd(18, 48)
    return gcd == 6
