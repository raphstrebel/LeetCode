# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        leaf_values = []
        def dfsSum(n, s):
            if n is None:
                return
            s += n.val
            if n.left is None and n.right is None:
                leaf_values.append(s)
            if n.left:
                dfsSum(n.left, s)
            if n.right:
                dfsSum(n.right, s)
        dfsSum(root, 0)
        if targetSum in leaf_values:
            return True
        else:
            return False
            
            
