from src.linked_lists.reverse_linked_list_iterative import reverse
from src.linked_lists.advance_to_linked_list_node import advance
from src.linked_lists.linked_list_size import size

def is_same(head1, head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1, head2 = head1.next, head2.next
    return head1 is None or head2 is None

def is_palindrome(head):
    n = size(head)
    head2 = advance(head, n / 2)
    head2 = reverse(head2)
    return is_same(head, head2)
