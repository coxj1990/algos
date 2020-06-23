def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1
