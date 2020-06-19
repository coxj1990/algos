from src.trees.types.tree_node import TreeNode
from src.trees.lowest_common_ancestor_bst import get_lca

def test_trivial():
    tree = TreeNode(0)
    lca = get_lca(tree, 1, 2)
    assert lca is None

def test_nontrivial():
    #        5
    #      /   \
    #     3     8
    #    / \
    #   2   4

    tree = TreeNode(5)
    tree.left = TreeNode(3, left=TreeNode(2), right=TreeNode(4))
    tree.right = TreeNode(8)

    lca = get_lca(tree, 2, 4)
    assert lca.val == 3
