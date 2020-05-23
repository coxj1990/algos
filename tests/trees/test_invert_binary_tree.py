from src.trees.types.tree_node import TreeNode
from src.trees.is_same_tree import is_same_tree
from src.trees.invert_binary_tree import invert

def test_trivial():
    tree = TreeNode(0)
    tree_inv = invert(tree)
    assert is_same_tree(tree_inv, TreeNode(0))

def test_nontrivial():
    #        4               4
    #      /   \           /   \
    #     2     7   ->    7     2
    #    / \   / \       / \   / \
    #   1   3 6   9     9   6 3   1

    tree = TreeNode(4)
    tree.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    tree.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))

    tree_inv = TreeNode(4)
    tree_inv.left = TreeNode(7, left=TreeNode(9), right=TreeNode(6))
    tree_inv.right = TreeNode(2, left=TreeNode(3), right=TreeNode(1))

    assert is_same_tree(invert(tree), tree_inv)
