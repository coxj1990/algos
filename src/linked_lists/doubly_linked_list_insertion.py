from src.linked_lists.types.doubly_linked_list_node import DoublyLinkedListNode

def insert_before(after_node, val):
    node = DoublyLinkedListNode(val)
    node.prev = after_node.prev
    node.next = after_node
    if after_node.prev:
        after_node.prev.next = node
    after_node.prev = node

def insert_after(before_node, val):
    node = DoublyLinkedListNode(val)
    node.prev = before_node
    node.next = before_node.next
    if before_node.next:
        before_node.next.prev = node
    before_node.next = node
