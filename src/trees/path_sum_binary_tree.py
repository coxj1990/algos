def has_path_sum(root, k):
    if not root:
        return False
    total = k - root.val
    if not root.left and not root.right and total == 0:
        return True
    return has_path_sum(root.left, total) or \
        has_path_sum(root.right, total)
