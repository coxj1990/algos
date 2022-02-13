from src.trees.is_same_tree import is_same_tree

# O(n*m), where
# n - number of nodes in subroot
# m - number of nodes in roo
def is_subtree(subroot, root):
    if not subroot and not root:
        return True
    if not subroot or not root:
        return False
    return is_same_tree(subroot, root) or \
           is_subtree(subroot, root.left) or \
           is_subtree(subroot, root.right)
