from utils.linked_list_node import LinkedListNode

def remove(head, val):
    before = LinkedListNode(0)
    before.next = head
    curr = before
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return before.next
