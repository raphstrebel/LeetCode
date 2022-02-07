# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack = []
        seen = []
        curr = root
        while curr or (len(stack) > 0):
            # push all left node path to stack
            while curr:
                stack.append(curr)
                curr = curr.left
            # first node of stack is left-most unseen
            curr = stack.pop()
            seen.append(curr.val)
            curr = curr.right
        return seen
    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        seen = []
        def inorderRec(r):
            if r is not None:
                inorderRec(r.left)
                seen.append(r.val)
                inorderRec(r.right)
                
        inorderRec(root)
        return seen