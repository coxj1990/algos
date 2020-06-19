def _is_symmetric(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    return node1.val == node2.val and \
        _is_symmetric(node1.left, node2.right) and \
        _is_symmetric(node1.right, node2.left)

def is_symmetric(root):
    return _is_symmetric(root, root)
