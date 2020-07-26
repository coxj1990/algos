from src.linked_lists.reverse_linked_list_iterative import reverse
from src.linked_lists.advance_to_linked_list_node import advance
from src.linked_lists.linked_list_size import size

# Reorder from 1 -> 2 -> ... -> N -> N-1 to
#              1 -> N -> ... -> N-1 -> 2

def reorder(head):
    n = size(head)
    head2 = advance(head, n / 2)
    head2 = reverse(head2)
    curr = head
    while curr:
        nxt = curr.next
        curr.next = head2
        curr, head2 = head2, nxt
