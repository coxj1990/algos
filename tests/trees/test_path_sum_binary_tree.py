from src.trees.types.tree_node import TreeNode
from src.trees.path_sum_binary_tree import has_path_sum

def test_trivial_found():
    root = TreeNode(0)
    assert has_path_sum(root, 0)

def test_trivial_not_found():
    root = TreeNode(0)
    assert not has_path_sum(root, 1)

def test_nontrivial_found():
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    root.right = TreeNode(5)
    assert has_path_sum(root, 7)

def test_nontrivial_not_found():
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    root.right = TreeNode(5)
    assert not has_path_sum(root, 6)
