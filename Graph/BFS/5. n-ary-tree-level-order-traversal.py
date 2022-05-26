"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None or root.val is None:
            return []
        
        levels = [[]]
        num_levels = 0
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if level > num_levels:
                num_levels += 1
                levels.append([])
            levels[level].append(node.val)
            for child in node.children:
                queue.append((child, level+1))
        return levels