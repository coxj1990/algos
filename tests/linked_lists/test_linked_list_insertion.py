from src.linked_lists.types.linked_list_node import LinkedListNode
from src.linked_lists.is_same_linked_list import is_same
from src.linked_lists.linked_list_insertion import insert_after

def test_trivial():
    head1 = LinkedListNode(0)
    insert_after(head1, 1)
    head2 = LinkedListNode(0, LinkedListNode(1))
    assert is_same(head1, head2)

def test_nontrivial():
    head1 = LinkedListNode(1, LinkedListNode(3))
    head2 = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3)))
    insert_after(head1, 2)
    assert is_same(head1, head2)
