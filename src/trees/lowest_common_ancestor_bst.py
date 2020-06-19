def get_lca(root, p, q):
    if root is None:
        return None
    if p > root.val and q > root.val:
        return get_lca(root.right, p, q)
    if p < root.val and q < root.val:
        return get_lca(root.left, p, q)
    return root
