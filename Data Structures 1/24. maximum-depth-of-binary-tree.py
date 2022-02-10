# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepthRec(n):
            if not n:
                return 0
            depth_left, depth_right = 0, 0
            if n.left:
                depth_left = maxDepthRec(n.left) + 1
            if n.right:
                depth_right = maxDepthRec(n.right) + 1
            return max(depth_left, depth_right, 1)
        return maxDepthRec(root)