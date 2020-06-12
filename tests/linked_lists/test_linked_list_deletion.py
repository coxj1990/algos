from src.linked_lists.types.linked_list_node import LinkedListNode
from src.linked_lists.is_same_linked_list import is_same
from src.linked_lists.linked_list_deletion import delete_after

def test_trivial():
    head1 = LinkedListNode(0, LinkedListNode(1))
    delete_after(head1)
    head2 = LinkedListNode(0)
    assert is_same(head1, head2)

def test_nontrivial():
    head1 = LinkedListNode(0, LinkedListNode(1, LinkedListNode(2)))
    delete_after(head1)
    head2 = LinkedListNode(0, LinkedListNode(2))
    assert is_same(head1, head2)
