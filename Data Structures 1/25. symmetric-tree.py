# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None:
            if root.right is None:
                return True
            else:
                return False
        if root.right is None:
            return False
        
        seen_1 = []
        def bfs_1(n):
            if n is None:
                seen_1.append(None)
                return
            seen_1.append(n.val)
            bfs_1(n.left)
            bfs_1(n.right)
        seen_2 = []
        def bfs_2(n):
            if n is None:
                seen_2.append(None)
                return
            seen_2.append(n.val)
            bfs_2(n.right)
            bfs_2(n.left)
            
        bfs_1(root.left)
        bfs_2(root.right)
        return seen_1 == seen_2