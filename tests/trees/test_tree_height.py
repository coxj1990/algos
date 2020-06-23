from src.trees.types.tree_node import TreeNode
from src.trees.tree_height import get_height

def test_trivial():
    root = TreeNode(0)
    assert get_height(root) == 1

def test_nontrivial():
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    root.right = TreeNode(5)
    assert get_height(root) == 3
