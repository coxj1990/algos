def advance(head, n):
    head2 = head
    for _ in range(n):
        head2 = head2.next
    return head2
