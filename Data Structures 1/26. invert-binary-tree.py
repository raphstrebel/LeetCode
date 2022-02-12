# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if root is None:
            return root
        def bfsRec(n):
            if n is None:
                return
            tmp = n.left
            n.left = n.right
            n.right = tmp
            bfsRec(n.left)
            bfsRec(n.right)
        bfsRec(root)
        return root