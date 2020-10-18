from src.linked_lists.types.doubly_linked_list_node import DoublyLinkedListNode
from src.linked_lists.is_same_doubly_linked_list import is_same

def test_trivial():
    assert is_same(None, None)

def test_trivial_true():
    head1 = DoublyLinkedListNode(0)
    head2 = DoublyLinkedListNode(0)
    assert is_same(head1, head2)

def test_trivial_false():
    head1 = DoublyLinkedListNode(0)
    head2 = DoublyLinkedListNode(1)
    assert not is_same(head1, head2)

def test_nontrivial_true():
    head1 = DoublyLinkedListNode(0)
    node11 = DoublyLinkedListNode(1, prev=head1)
    node12 = DoublyLinkedListNode(2, prev=node11)
    head1.next = node11
    node11.next = node12
    head2 = DoublyLinkedListNode(0)
    node21 = DoublyLinkedListNode(1, prev=head1)
    node22 = DoublyLinkedListNode(2, prev=node11)
    head2.next = node21
    node21.next = node22
    assert is_same(head1, head2)

def test_nontrivial_false():
    head1 = DoublyLinkedListNode(0)
    node11 = DoublyLinkedListNode(1, prev=head1)
    node12 = DoublyLinkedListNode(2, prev=node11)
    head1.next = node11
    node11.next = node12
    head2 = DoublyLinkedListNode(0)
    node21 = DoublyLinkedListNode(1, prev=head1)
    node22 = DoublyLinkedListNode(2, prev=head1)  # wrong prev
    head2.next = node21
    node21.next = node22
    assert not is_same(head1, head2)
