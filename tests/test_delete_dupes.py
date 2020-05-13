from src.delete_dupes import delete_dupes, delete_dupes_maintain_order

def test_trivial():
    L = []
    assert delete_dupes(L) == L

def test_nontrivial():
    L = [1, 2, 2, 3, 4, 4]
    expected = [1, 2, 3, 4]
    assert delete_dupes(L) == expected

def test_trivial_maintain_order():
    L = []
    assert delete_dupes_maintain_order(L) == L

def test_nontrivial_maintain_order():
    L = [1, 2, 2, 3, 4, 4]
    expected = [1, 2, 3, 4]
    assert delete_dupes_maintain_order(L) == expected
