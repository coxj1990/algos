from src.trees.types.tree_node import TreeNode
from src.trees.level_order_traversal import level_order_traversal

def test_trivial():
    root = TreeNode(0)
    traversal = level_order_traversal(root)
    assert traversal == [0]

def test_nontrivial():
    #       4
    #      / \
    #     2   5
    #    /     \
    #   1       3
    root = TreeNode(4)
    root.left = TreeNode(2, left=TreeNode(1))
    root.right = TreeNode(5, right=TreeNode(3))
    traversal = level_order_traversal(root)
    assert traversal == [4, 2, 5, 1, 3]
