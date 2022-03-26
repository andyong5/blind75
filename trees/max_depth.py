def iter_maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    stk = deque()
    # add root and the current depth
    stk.append((1, root))
    depth = 0
    while stk:
        c_depth, node = stk.pop()
        # pop stack and see if the new depth is biggest
        depth = max(depth, c_depth)
        if node.right:
            # for every node we add, we add 1 to the depth
            stk.append((c_depth + 1, node.right))
        if node.left:
            # for every node we add, we add 1 to the depth
            stk.append((c_depth + 1, node.left))
    return depth

def recurse(self, root, val):
    if not root:
        return val
    return max(self.recurse(root.left, val+1), self.recurse(root.right, val + 1))

def maxDepth(self, root: Optional[TreeNode]) -> int:
    return self.recurse(root, 0)