from src.linked_lists.types.linked_list_node import LinkedListNode
from src.linked_lists.is_linked_list_palindrome import is_palindrome

def test_trivial_true():
    head = LinkedListNode('a')
    assert is_palindrome(head)

def test_trivial_false():
    head = LinkedListNode('a', LinkedListNode('b'))
    assert not is_palindrome(head)

def test_nontrivial_true():
    head = LinkedListNode('a', LinkedListNode('b', LinkedListNode('a')))
    assert is_palindrome(head)

def test_nontrivial_false():
    head = LinkedListNode('a', LinkedListNode('b', LinkedListNode('c')))
    assert not is_palindrome(head)
