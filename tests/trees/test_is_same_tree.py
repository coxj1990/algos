from src.trees.types.tree_node import TreeNode
from src.trees.is_same_tree import is_same_tree

def test_trivial_true():
    tree1 = TreeNode(0)
    tree2 = TreeNode(0)
    assert is_same_tree(tree1, tree2)

def test_trivial_false():
    tree1 = TreeNode(0)
    tree2 = TreeNode(1)
    assert not is_same_tree(tree1, tree2)

def test_nontrivial_true():
    #        4               4
    #      /   \           /   \
    #     2     7   ==    2     7
    #    / \   / \       / \   / \
    #   1   3 6   9     1   3 6   9

    tree1 = TreeNode(4)
    tree1.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    tree1.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))

    tree2 = TreeNode(4)
    tree2.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    tree2.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))

    assert is_same_tree(tree1, tree2)

def test_nontrivial_false():
    #        4               4
    #      /   \           /   \
    #     2     7   !=    7     2
    #    /     / \       / \   / \
    #   1     6   9     9   6 3   1

    tree1 = TreeNode(4)
    tree1.left = TreeNode(2, left=TreeNode(1))
    tree1.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))

    tree2 = TreeNode(4)
    tree2.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    tree2.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))

    assert not is_same_tree(tree1, tree2)
