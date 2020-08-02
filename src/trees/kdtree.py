from src.trees.types.tree_node import TreeNode

class KdTree:

    def __init__(self, data):
        self.kdtree = self.make_tree(data, depth=0)

    def make_tree(self, data, depth):
        if not data:
            return None
        dim = depth % len(data[0])
        data.sort(key=lambda x: x[dim])
        mid = len(data) / 2
        return TreeNode(data[mid],
                        self.make_tree(data[:mid], depth + 1),
                        self.make_tree(data[mid + 1:], depth + 1))

    def _get_closest(self, node, x, depth):
        if not node:
            return None
        if node.left is None and node.right is None:
            return node.val
        dim = depth % len(node.val)
        if x[dim] < node.val[dim]:
            return self._get_closest(node.left, x, depth + 1)
        elif x[dim] > node.val[dim]:
            return self._get_closest(node.right, x, depth + 1)
        else:
            return node.val

    def get_closest(self, x):
        return self._get_closest(self.kdtree, x, 0)
