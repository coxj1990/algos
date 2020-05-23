def is_bst(root, lower=-float('inf'), upper=float('inf')):
    if not root:
        return True
    if root.val < lower or root.val > upper:
        return False
    return is_bst(root.left, lower, root.val) and is_bst(root.right, root.val, upper)
