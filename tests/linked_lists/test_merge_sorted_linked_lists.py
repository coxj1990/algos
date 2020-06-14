from src.linked_lists.types.linked_list_node import LinkedListNode
from src.linked_lists.is_same_linked_list import is_same
from src.linked_lists.merge_sorted_linked_lists import merge

def test_trivial():
    head1 = LinkedListNode(0)
    head2 = LinkedListNode(1)
    merged = merge(head1, head2)
    expected = LinkedListNode(0, LinkedListNode(1))
    assert is_same(merged, expected)

def test_nontrivial():
    head1 = LinkedListNode(1, LinkedListNode(3))
    head2 = LinkedListNode(0, LinkedListNode(2))
    merged = merge(head1, head2)
    expected = LinkedListNode(0, LinkedListNode(1, LinkedListNode(2, LinkedListNode(3))))
    assert is_same(merged, expected)
