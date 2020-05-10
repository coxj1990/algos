def is_same_tree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.val == root2.val and \
        is_same_tree(root1.left, root2.left) and \
        is_same_tree(root1.right, root2.right)
