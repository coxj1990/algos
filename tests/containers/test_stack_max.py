from src.containers.stack_max import Stack

def test_trivial():
    s = Stack()
    s.push(1)
    print(type(s))
    assert s.max() == 1

def test_nontrivial():
    s = Stack()
    s.push(2)
    s.push(1)
    s.push(3)
    s.pop()
    assert s.max() == 2
