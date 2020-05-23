from src.linked_lists.types.linked_list_node import LinkedListNode
from src.linked_lists.is_same_linked_list import is_same

def test_trivial():
    assert is_same(None, None)

def test_trivial_true():
    head1 = LinkedListNode(0)
    head2 = LinkedListNode(0)
    assert is_same(head1, head2)

def test_trivial_false():
    head1 = LinkedListNode(0)
    head2 = LinkedListNode(1)
    assert not is_same(head1, head2)

def test_nontrivial_true():
    head1 = LinkedListNode(0, LinkedListNode(1, LinkedListNode(2)))
    head2 = LinkedListNode(0, LinkedListNode(1, LinkedListNode(2)))
    assert is_same(head1, head2)

def test_nontrivial_false():
    head1 = LinkedListNode(0, LinkedListNode(1, LinkedListNode(2)))
    head2 = LinkedListNode(0, LinkedListNode(1))
    assert not is_same(head1, head2)
