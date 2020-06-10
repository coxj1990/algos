from src.linked_lists.types.linked_list_node import LinkedListNode

def insert_after(before_node, val):
    node = LinkedListNode(val)
    node.next = before_node.next
    before_node.next = node
