from src.trees.types.tree_node import TreeNode
from src.trees.bst_search import search

def test_trivial_true():
    tree = TreeNode(0)
    assert search(tree, 0)

def test_trivial_false():
    assert not search(None, 0)

def test_nontrivial_true():
    #        5
    #      /   \
    #     3     8
    #    / \
    #   2   4

    tree = TreeNode(4)
    tree.left = TreeNode(3, left=TreeNode(2), right=TreeNode(4))
    tree.right = TreeNode(8)

    assert search(tree, 4)

def test_nontrivial_false():
    #        5
    #      /   \
    #     3     8
    #    / \
    #   2   4

    tree = TreeNode(4)
    tree.left = TreeNode(3, left=TreeNode(2), right=TreeNode(4))
    tree.right = TreeNode(8)

    assert not search(tree, 1)
