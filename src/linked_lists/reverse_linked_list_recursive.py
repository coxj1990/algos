def reverse(head, before=None):
    if head is None:
        return before
    nxt = head.next
    head.next = before
    return reverse(nxt, head)
