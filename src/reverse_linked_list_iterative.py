def reverse(head):
    before = None
    while head:
        nxt = head.next
        head.next = before
        before, head = head, nxt
    return before
