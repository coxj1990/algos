from src.trees.types.tree_node import TreeNode
from src.trees.tree_traversal import inorder, preorder, postorder

def test_inorder():
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    root.right = TreeNode(5)
    assert inorder(root) == [1, 2, 3, 4, 5]

def test_preorder():
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    root.right = TreeNode(5)
    assert preorder(root) == [4, 2, 1, 3, 5]

def test_postorder():
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    root.right = TreeNode(5)
    assert postorder(root) == [1, 3, 2, 5, 4]
