def size(head):
    n = 0
    while head:
        n += 1
        head = head.next
    return n
