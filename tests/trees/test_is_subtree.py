from src.trees.types.tree_node import TreeNode
from src.trees.is_subtree import is_subtree

def test_trivial_true():
    assert is_subtree(None, None)

def test_trivial_false():
    tree1 = TreeNode(0)
    assert not is_subtree(tree1, None)

def test_nontrivial_true():
    #                            4
    #                          /   \
    #     2   is subtree of   2     7
    #    / \                 / \   / \
    #   1   3               1   3 6   9

    tree1 = TreeNode(2)
    tree1.left = TreeNode(1)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(4)
    tree2.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    tree2.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))

    assert is_subtree(tree1, tree2)

def test_nontrivial_false():
    #                            4
    #                          /   \
    #     2   is subtree of   2     7
    #    / \                 / \   / \
    #   1   3               1   3 6   9
    #        \
    #         4

    tree1 = TreeNode(2)
    tree1.left = TreeNode(1)
    tree1.right = TreeNode(3, right=TreeNode(4))

    tree2 = TreeNode(4)
    tree2.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    tree2.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))

    assert not is_subtree(tree1, tree2)
