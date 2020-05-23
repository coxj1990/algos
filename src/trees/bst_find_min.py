def find_min(root):
    while root and root.left:
        root = root.left
    return root.val
