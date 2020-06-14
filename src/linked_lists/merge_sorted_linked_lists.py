from src.linked_lists.types.linked_list_node import LinkedListNode

def merge(head1, head2):
    dummy = LinkedListNode(-1)
    curr = dummy
    while head1 and head2:
        if head1.val < head2.val:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    if head1:
        curr.next = head1
    if head2:
        curr.next = head2
    return dummy.next
