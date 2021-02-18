def get_parents(root, parents, parent=None):
    if root is None:
        return
    parents[root] = parent
    get_parents(root.left, parents, root)
    get_parents(root.right, parents, root)

def get_nodes_k_distance(target, k, parents, res, visited):
    if target is None or target.val in visited:
        return
    visited.add(target.val)
    if k == 0:
        res.append(target.val)
        return
    get_nodes_k_distance(target.left, k-1, parents, res, visited)
    get_nodes_k_distance(target.right, k-1, parents, res, visited)
    get_nodes_k_distance(parents[target], k-1, parents, res, visited)

def all_nodes_k_distance(root, target, k):
    parents = {}
    get_parents(root, parents)
    res = []
    visited = set()
    get_nodes_k_distance(target, k, parents, res, visited)
    return res
