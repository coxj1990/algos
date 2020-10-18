def is_same_prev(prev1, prev2):
    if prev1 is None and prev2 is None:
        return True
    if prev1 is None or prev2 is None:
        return False
    return prev1.val == prev2.val

def is_same(head1, head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False
        if not is_same_prev(head1.prev, head2.prev):
            return False
        head1, head2 = head1.next, head2.next
    return head1 is None and head2 is None
