from src.linked_lists.types.linked_list_node import LinkedListNode
from src.linked_lists.linked_list_size import size

def test_trivial():
    head = LinkedListNode(0)
    return size(head) == 1

def test_nontrivial():
    head = LinkedListNode(0, LinkedListNode(1, LinkedListNode(2)))
    return size(head) == 3
