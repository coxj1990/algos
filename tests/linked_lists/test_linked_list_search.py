from src.linked_lists.types.linked_list_node import LinkedListNode
from src.linked_lists.linked_list_search import search

def test_trivial_found():
    head = LinkedListNode(0)
    assert search(head, 0)

def test_trivial_not_found():
    head = LinkedListNode(0)
    assert not search(head, 1)

def test_nontrivial_found():
    head = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3)))
    assert search(head, 3)

def test_nontrivial_not_found():
    head = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3)))
    assert not search(head, 4)
