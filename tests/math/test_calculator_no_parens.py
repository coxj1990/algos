from src.math.calculator_no_parens import calculate

def test_trivial():
    res = calculate('2+2')
    assert res == 4

def test_nontrivial():
    res = calculate('2*4/2+3')
    assert res == 7
