# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        seen = []
        def postorderRec(r):
            if r:
                postorderRec(r.left)
                postorderRec(r.right)
                seen.append(r.val)
        postorderRec(root)
        return seen