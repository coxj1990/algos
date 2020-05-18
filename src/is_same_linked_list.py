def is_same(head1, head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1, head2 = head1.next, head2.next
    return head1 is None and head2 is None
