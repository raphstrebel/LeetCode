# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestorIt(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Iterative approach:
        - if p and q are in different subtrees, return root
        - if p and q are in same subtree, loop over common subtree
        """
        if p.val == q.val:
            return p
        # set p < q (to simplify)
        if p.val > q.val:
            tmp = q
            q = p
            p = tmp
        node = root
        while node is not None:
            if p.val <= node.val:
                if node.val <= q.val:
                    return node
                else:
                    node = node.left
            else:
                node = node.right
            
        return node
    def lowestCommonAncestorRec(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Recursive approach: 
        - if p and q are in left and right subtrees of root (resp.), return root
        - otherwise set root = root.left (if p,q < root) or root.right (if p,q > root)
        """
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