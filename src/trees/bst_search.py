def search(root, val):
    if not root:
        return False
    if val == root.val:
        return True
    elif val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)
