def get_path(node, val):
    if not node:
        return []
    if node.val == val:
        return [node.val]
    res = get_path(node.left, val)
    if res:
        return [node.val] + res
    res = get_path(node.right, val)
    if res:
        return [node.val] + res
    return []
