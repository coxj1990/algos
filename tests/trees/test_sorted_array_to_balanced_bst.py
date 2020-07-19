from src.trees.types.tree_node import TreeNode
from src.trees.is_same_tree import is_same_tree
from src.trees.sorted_array_to_balanced_bst import array_to_bst

def test_trivial():
    L = []
    tree = array_to_bst(L)
    assert tree is None

def test_nontrivial_true():
    #        6
    #      /   \
    #     2     8
    #    / \   / \
    #   1   3 7   9
    L = [1, 2, 3, 6, 7, 8, 9]
    tree = array_to_bst(L)
    expected = TreeNode(6)
    expected.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    expected.right = TreeNode(8, left=TreeNode(7), right=TreeNode(9))
    assert is_same_tree(tree, expected)
