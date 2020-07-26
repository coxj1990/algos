from src.linked_lists.types.linked_list_node import LinkedListNode
from src.linked_lists.advance_to_linked_list_node import advance

def test_trivial():
    head = LinkedListNode(0)
    head2 = advance(head, 0)
    return head2.val == 0

def test_nontrivial():
    head = LinkedListNode(0, LinkedListNode(1, LinkedListNode(2)))
    head2 = advance(head, 1)
    return head2.val == 1
