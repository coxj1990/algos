from src.containers.stack_push_pop import Stack

def test_trivial():
    s = Stack()
    s.push(1)
    assert s.pop() == 1

def test_nontrivial():
    s = Stack()
    n = 3
    nums = list(range(n))
    for e in nums:
        s.push(e)
    popped = []
    for _ in range(n):
        popped.append(s.pop())
    assert popped == nums[::-1]
