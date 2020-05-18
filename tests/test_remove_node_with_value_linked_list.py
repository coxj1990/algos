from utils.linked_list_node import LinkedListNode
from src.is_same_linked_list import is_same
from src.remove_node_with_value_linked_list import remove

def test_trivial():
    head = LinkedListNode(0)
    assert remove(head, 0) is None

def test_nontrivial():
    # 2 -> 0 -> 2 -> 2 -> 1 -> 2 => 0 -> 1

    head1 = LinkedListNode(2)
    node1 = LinkedListNode(0)
    node2 = LinkedListNode(2)
    node3 = LinkedListNode(2)
    node4 = LinkedListNode(1)
    node5 = LinkedListNode(2)
    head1.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    head2 = LinkedListNode(0)
    node6 = LinkedListNode(1)
    head2.next = node6

    assert is_same(remove(head1, 2), head2)
