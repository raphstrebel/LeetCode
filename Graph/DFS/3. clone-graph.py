"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        # keep track of visited nodes as keys, their copy as values
        visited = {}
        def rec(node):
            # base cases
            if node is None:
                return None
            if node in visited:
                return visited[node]
            if len(node.neighbors) == 0:
                return Node(val=node.val)
            
            # initialize first node without neighbors
            node_copy = Node(val=node.val)
            visited[node] = node_copy

            # initialize all neighbor nodes with same recursive method
            neighbors = []
            for x in node.neighbors:
                neighbors.append(rec(x))
            # set neighbors (once all nodes have a copy)
            node_copy.neighbors = neighbors
            return node_copy
        return rec(node)
            