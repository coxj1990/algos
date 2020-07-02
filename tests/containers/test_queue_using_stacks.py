from src.containers.queue_using_stacks import Queue

def test_trivial():
    q = Queue()
    q.push(1)
    assert q.pop() == 1

def test_nontrivial():
    q = Queue()
    n = 3
    nums = list(range(n))
    for e in nums:
        q.push(e)
    popped = []
    for _ in range(n):
        popped.append(q.pop())
    assert popped == nums
