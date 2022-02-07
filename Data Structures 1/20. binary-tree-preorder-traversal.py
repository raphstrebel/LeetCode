# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Iterative approach using a stack"""
        if root is None:
            return []
        stack = []
        seen = []
        stack.append(root)
        while len(stack) > 0:
            curr = stack.pop()
            seen.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return seen
    def preorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        def preorderRec(root):
            if root:
                queue.append(root.val)
                preorderRec(root.left)
                preorderRec(root.right)
        preorderRec(root)
        return queue