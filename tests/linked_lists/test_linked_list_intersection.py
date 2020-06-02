from src.linked_lists.types.linked_list_node import LinkedListNode
from src.linked_lists.linked_list_intersection import get_intersection

def test_trivial():
    # 1-2
    #  /
    # 1

    head1 = LinkedListNode(1)
    node1 = LinkedListNode(2)
    head1.next = node1

    head2 = LinkedListNode(1)
    head2.next = node1

    intersection_node = get_intersection(head1, head2)
    assert intersection_node.val == 2

def test_nontrivial():
    # 1-2-3-4
    #    /
    # 1-2

    head1 = LinkedListNode(1)
    node1 = LinkedListNode(2)
    node2 = LinkedListNode(3)
    node3 = LinkedListNode(4)
    head1.next = node1
    node1.next = node2
    node2.next = node3

    head2 = LinkedListNode(1)
    node4 = LinkedListNode(2)
    head2.next = node4
    node4.next = node2

    intersection_node = get_intersection(head1, head2)
    assert intersection_node.val == 3
