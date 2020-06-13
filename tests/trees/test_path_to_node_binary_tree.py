from src.trees.types.tree_node import TreeNode
from src.trees.path_to_node_binary_tree import get_path

def test_trivial():
    root = TreeNode(0)
    assert get_path(root, 1) == []

def test_nontrivial():
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    root.right = TreeNode(5)
    assert get_path(root, 3) == [4, 2, 3]
