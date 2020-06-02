def get_intersection(head1, head2):
    while head1 != head2:
        head1 = head1.next if head1.next else head2
        head2 = head2.next if head2.next else head1
    return head1
