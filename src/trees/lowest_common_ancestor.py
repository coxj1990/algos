def get_lca(root, p, q):
    if root is None:
        return None
    if root.val == p or root.val == q:
        return root
    left = get_lca(root.left, p, q)
    right = get_lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right
