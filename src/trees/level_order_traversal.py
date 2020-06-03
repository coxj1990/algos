def level_order_traversal(root):
    traversal = []
    q = [root]
    while q:
        curr = q.pop(0)
        traversal.append(curr.val)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return traversal
