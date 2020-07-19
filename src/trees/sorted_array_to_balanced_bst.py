from src.trees.types.tree_node import TreeNode

def _array_to_bst(L, first, last):
    if first > last:
        return None
    mid = (first + last) // 2
    node = TreeNode(L[mid])
    node.left = _array_to_bst(L, first, mid - 1)
    node.right = _array_to_bst(L, mid + 1, last)
    return node

def array_to_bst(L):
    return _array_to_bst(L, 0, len(L) - 1)
