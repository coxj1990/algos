from src.arrays.fibonacci import fib_recursive, fib_memo, fib_dp

def test_trivial_recursive():
    assert fib_recursive(1) == 0

def test_nontrivial_recursive():
    assert fib_recursive(7) == 8

def test_trivial_memo():
    assert fib_memo(1) == 0

def test_nontrivial_memo():
    assert fib_memo(7) == 8

def test_trivial_dp():
    assert fib_dp(1) == 0

def test_nontrivial_dp():
    assert fib_dp(7) == 8
