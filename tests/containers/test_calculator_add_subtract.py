from src.containers.calculator_add_subtract import calculate

def test_trivial():
    res = calculate("1 + 1")
    assert res == 2

def test_nontrivial():
    res = calculate("(1+(4+5+2)-3)+(6+8)")
    assert res == 23
