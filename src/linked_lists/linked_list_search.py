def search(node, val):
    while node and node.val != val:
        node = node.next
    return True if node else False
