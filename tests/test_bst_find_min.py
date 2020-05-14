from utils.tree_node import TreeNode
from src.bst_find_min import find_min

def test_trivial():
    tree = TreeNode(0)
    assert find_min(tree) == 0

def test_nontrivial():
    #        5
    #      /   \
    #     3     8
    #    / \
    #   2   4

    tree = TreeNode(4)
    tree.left = TreeNode(3, left=TreeNode(2), right=TreeNode(4))
    tree.right = TreeNode(8)

    assert find_min(tree) == 2
