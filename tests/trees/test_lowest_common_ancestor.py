from src.trees.types.tree_node import TreeNode
from src.trees.lowest_common_ancestor import get_lca

def test_trivial():
    tree = TreeNode(0)
    p = TreeNode(1)
    q = TreeNode(2)
    lca = get_lca(tree, p, q)
    assert lca is None

def test_nontrivial():
    #        4
    #      /   \
    #     2     7
    #    / \   / \
    #   1   3 6   9

    tree = TreeNode(4)
    tree.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    tree.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))

    p = tree.left.left
    q = tree.left.right
    lca = get_lca(tree, p, q)
    assert lca.val == 2
