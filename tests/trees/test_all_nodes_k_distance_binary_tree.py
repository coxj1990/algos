from src.trees.types.tree_node import TreeNode
from src.trees.all_nodes_k_distance_binary_tree import all_nodes_k_distance

def test_trivial():
    root = TreeNode(0)
    left = TreeNode(1)
    root.left = left
    res = all_nodes_k_distance(root, left, 1)
    assert res == [0]

def test_nontrivial():
    #       3
    #      / \
    #     5   1
    #    / \   \
    #   6   2   8
    #      / \
    #     7   4
    root = TreeNode(3)
    target = TreeNode(5)
    root.left = target
    target.left = TreeNode(6)
    target.right = TreeNode(2, TreeNode(7), TreeNode(4))
    root.right = TreeNode(1, None, TreeNode(8))
    res = all_nodes_k_distance(root, target, 2)
    assert set([1, 4, 7]) == set(res)
