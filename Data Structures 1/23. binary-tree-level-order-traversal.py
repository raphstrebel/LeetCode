# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # keep track of nodes on each level
        nodes = []
        # keep track of values of nodes on each level
        levels = []
        nodes.append([root])
        levels.append([root.val])
        i = 0
        while True:
            nodes_on_level = nodes[i]
            next_level = []
            next_level_nodes = []
            # for every nodes on a level (from left to right)
            for n in nodes_on_level:
                # append left then right child to next_level_nodes, and their values to next_lebel
                if n.left:
                    next_level_nodes.append(n.left)
                    next_level.append(n.left.val)
                if n.right:
                    next_level_nodes.append(n.right)
                    next_level.append(n.right.val)
            # no more children after this level
            if next_level == []:
                return levels
            levels.append(next_level)
            nodes.append(next_level_nodes)
            i += 1
