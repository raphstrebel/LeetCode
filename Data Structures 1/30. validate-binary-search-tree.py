# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidRec(r, left_max, right_min):
            if r is None:
                return True
            if left_max >= r.val or r.val >= right_min:
                return False
            return isValidRec(r.left, left_max, r.val) and isValidRec(r.right, r.val, right_min)
        return isValidRec(root, -math.inf, math.inf)