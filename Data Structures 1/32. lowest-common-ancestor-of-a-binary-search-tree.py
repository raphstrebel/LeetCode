# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == q.val:
            return p
        if p.val > q.val:
            tmp = q
            q = p
            p = tmp
        def commonAncestorRec(r, p, q):
            if p.val <= r.val:
                if r.val <= q.val:
                    return r
                else:
                    return commonAncestorRec(r.left, p, q)
            else:
                return commonAncestorRec(r.right, p, q)
        return commonAncestorRec(root, p, q)