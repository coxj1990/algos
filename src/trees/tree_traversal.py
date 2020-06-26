def _inorder(root, res):
    if root is None:
        return
    _inorder(root.left, res)
    res.append(root.val)
    _inorder(root.right, res)

def inorder(root):
    res = []
    _inorder(root, res)
    return res

def _preorder(root, res):
    if root is None:
        return
    res.append(root.val)
    _preorder(root.left, res)
    _preorder(root.right, res)

def preorder(root):
    res = []
    _preorder(root, res)
    return res

def _postorder(root, res):
    if root is None:
        return
    _postorder(root.left, res)
    _postorder(root.right, res)
    res.append(root.val)

def postorder(root):
    res = []
    _postorder(root, res)
    return res
