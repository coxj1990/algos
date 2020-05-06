from utils.tree_node import TreeNode
from src.is_binary_tree_bst import is_bst

def test_trivial():
    assert is_bst(None)

def test_root_only():
    root = TreeNode(0)
    assert is_bst(root)

def test_nontrivial_true():
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    root.right = TreeNode(5)
    assert is_bst(root)

def test_nontrivial_false():
    #       3
    #      / \
    #     2   5
    #    / \
    #   1   4
    root = TreeNode(3)
    root.left = TreeNode(2, left=TreeNode(1), right=TreeNode(4))
    root.right = TreeNode(5)
    assert not is_bst(root)
