from src.linked_lists.types.doubly_linked_list_node import DoublyLinkedListNode
from src.linked_lists.is_same_doubly_linked_list import is_same
from src.linked_lists.doubly_linked_list_deletion import delete_before, delete_after

def test_delete_before():
    head1 = DoublyLinkedListNode(0)
    node11 = DoublyLinkedListNode(1, prev=head1)
    node12 = DoublyLinkedListNode(2, prev=node11)
    head1.next = node11
    node11.next = node12
    head2 = DoublyLinkedListNode(0)
    node21 = DoublyLinkedListNode(2, prev=head2)
    head2.next = node21
    assert not is_same(head1, head2)
    delete_before(node12)
    assert is_same(head1, head2)

def test_nontrivial_insert_after():
    head1 = DoublyLinkedListNode(0)
    node11 = DoublyLinkedListNode(1, prev=head1)
    node12 = DoublyLinkedListNode(2, prev=node11)
    head1.next = node11
    node11.next = node12
    head2 = DoublyLinkedListNode(0)
    node21 = DoublyLinkedListNode(2, prev=head2)
    head2.next = node21
    assert not is_same(head1, head2)
    delete_after(head1)
    assert is_same(head1, head2)
