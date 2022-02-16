# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Store needed number in `found` set, use depth-first search to try all elements
        """
        if root is None:
            return False
        found = set()
        
        def traverse(node):
            if node is None:
                return False
            if node.val in found:
                return True
            found.add(k-node.val)
            found_left = traverse(node.left)
            if found_left:
                return True
            found_right = traverse(node.right)
            return found_right
        return traverse(root)
    def findTargetNaive(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Transform tree to array, check if left-most + right-most is =, <, > to target:
        - if =, we are done
        - if <, recursively try same array without first element
        - if >, recursively try same array without last element
        """
        if root is None:
            return False

        # BST to array
        sorted_tree = []
        def bstToArray(node):
            if node is not None:
                bstToArray(node.left)
                sorted_tree.append(node.val)
                bstToArray(node.right)
        bstToArray(root)
        print(sorted_tree)
        def findSum(array):
            n = len(array)
            if n <= 1:
                return False
            if array[0] + array[1] == k:
                return True
            elif array[0] + array[1] > k:
                return False
            if array[0] + array[n-1] == k:
                return True
            elif array[0] + array[n-1] < k:
                return findSum(array[1:])
            else:
                return findSum(array[:n-1])
        return findSum(sorted_tree)