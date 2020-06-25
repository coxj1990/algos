def get_min_height(root):
    if root is None:
        return 0
    if not root.left or not root.right:
        return max(get_min_height(root.left), get_min_height(root.right)) + 1
    return min(get_min_height(root.left), get_min_height(root.right)) + 1
