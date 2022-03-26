def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # if they are both null then return True
    if not p and not q:
        return True
    # if one of them is null, then they can't be same
    if not p or not q:
        return False
    # if their values are not the same, then they can't be same
    if p.val != q.val:
        return False
    return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    que = deque()
    que.append((p, q))
    while que:
        for x in range(len(que)):
            p_n, q_n = que.popleft()
            if not p_n or not q_n:
                return False
            if p_n.val != q_n.val:
                return False
            
            # if one node is not null but the other one isn't
            if p_n.left and not q_n.left or p_n.right and not q_n.right:
                return False
            if q_n.left and not p_n.left or q_n.right and not p_n.right:
                return False

            if p_n.left and q_n.left:
                que.append((p_n.left, q_n.left))
            if p_n.right and q_n.right:
                que.append((p_n.right, q_n.right))
    return True