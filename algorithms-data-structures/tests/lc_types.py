"""LeetCode's node classes and helpers (TreeNode as in LeetCode's Python3 starter comment)."""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(level):
    """Build a tree from LeetCode level-order notation, e.g. [5,1,4,None,None,3,6]."""
    if not level or level[0] is None:
        return None
    it = iter(level)
    root = TreeNode(next(it))
    q = deque([root])
    while q:
        node = q.popleft()
        try:
            v = next(it)
        except StopIteration:
            break
        if v is not None:
            node.left = TreeNode(v)
            q.append(node.left)
        try:
            v = next(it)
        except StopIteration:
            break
        if v is not None:
            node.right = TreeNode(v)
            q.append(node.right)
    return root


def to_level(root):
    """Serialize a tree to LeetCode level-order notation (trailing Nones trimmed)."""
    if root is None:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def bst_insert(root, val):
    if root is None:
        return TreeNode(val)
    node = root
    while True:
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
                return root
            node = node.left
        else:
            if node.right is None:
                node.right = TreeNode(val)
                return root
            node = node.right


def balanced_bst(vals):
    """Balanced BST from sorted vals (iterative to avoid recursion limits)."""
    if not vals:
        return None
    lo, hi = 0, len(vals) - 1
    mid = (lo + hi) // 2
    root = TreeNode(vals[mid])
    stack = [(root, lo, mid - 1, 'L'), (root, mid + 1, hi, 'R')]
    while stack:
        parent, lo, hi, side = stack.pop()
        if lo > hi:
            continue
        mid = (lo + hi) // 2
        node = TreeNode(vals[mid])
        if side == 'L':
            parent.left = node
        else:
            parent.right = node
        stack.append((node, lo, mid - 1, 'L'))
        stack.append((node, mid + 1, hi, 'R'))
    return root


def height(root):
    h, q = 0, deque([root] if root else [])
    while q:
        h += 1
        for _ in range(len(q)):
            n = q.popleft()
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
    return h
