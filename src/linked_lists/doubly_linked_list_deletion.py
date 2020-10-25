def delete_before(after_node):
    if after_node.prev.prev:
        after_node.prev.prev.next = after_node
    after_node.prev = after_node.prev.prev

def delete_after(before_node):
    if before_node.next.next:
        before_node.next.next.prev = before_node
    before_node.next = before_node.next.next
