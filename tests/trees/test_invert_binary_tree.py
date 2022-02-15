from src.trees.types.tree_node import TreeNode
from src.trees.is_same_tree import is_same_tree
from src.trees.invert_binary_tree import invert

def test_stump_inverted_equals_itself():
    tree = TreeNode(0)
    tree_inverted = invert(tree)
    assert is_same_tree(tree_inverted, TreeNode(0))

def test_computes_correct_inverted_tree():
    #        4               4
    #      /   \           /   \
    #     2     7   ->    7     2
    #    / \   / \       / \   / \
    #   1   3 6   9     9   6 3   1

    tree = TreeNode(4)
    tree.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    tree.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))

    tree_inverted = TreeNode(4)
    tree_inverted.left = TreeNode(7, left=TreeNode(9), right=TreeNode(6))
    tree_inverted.right = TreeNode(2, left=TreeNode(3), right=TreeNode(1))

    assert tree.val == tree_inverted.val
    assert tree.left.val == tree_inverted.right.val
    assert tree.left.left.val == tree_inverted.right.right.val
    assert tree.right.right.val == tree_inverted.left.left.val
    assert tree.left.right.val == tree_inverted.right.left.val
    assert tree.right.left.val == tree_inverted.left.right.val
