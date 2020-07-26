from src.linked_lists.types.linked_list_node import LinkedListNode
from src.linked_lists.reorder_linked_list import reorder
from src.linked_lists.is_same_linked_list import is_same

def test_trivial():
    head = LinkedListNode(0)
    reorder(head)
    expected = LinkedListNode(0)
    assert is_same(head, expected)

def test_nontrivial():
    head = LinkedListNode(0, LinkedListNode(1, LinkedListNode(2, LinkedListNode(3))))
    expected = LinkedListNode(0, LinkedListNode(3, LinkedListNode(1, LinkedListNode(2))))
    reorder(head)
    assert is_same(head, expected)
