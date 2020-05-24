from src.arrays.first_nonrepeated_character import get_first_nonrepeated

def test_trivial():
    assert get_first_nonrepeated('x') == 'x'

def test_nontrivial():
    assert get_first_nonrepeated('level') == 'v'
