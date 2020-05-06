def is_bst(root, lower=-float('inf'), upper=float('inf')):
    if not root:
        return True
    if root.data < lower or root.data > upper:
        return False
    return is_bst(root.left, lower, root.data) and is_bst(root.right, root.data, upper)
