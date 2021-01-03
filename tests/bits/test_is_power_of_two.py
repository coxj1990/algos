from src.bits.is_power_of_two import is_power_of_two

def test_zero():
    assert not is_power_of_two(0)

def test_one():
    assert not is_power_of_two(1)

def test_true():
    assert is_power_of_two(16)

def test_false():
    assert not is_power_of_two(15)
