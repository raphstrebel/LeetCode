"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        """
        Keep track of leftmost.
        Set 2 types of pointers for a node's children:
        - node.left -> node.right
        - node.right -> node.next.left (since node.next is the next node in the bfs queue)
        """
        if root is None:
            return root
        leftmost = root
        while leftmost.left is not None:
            # set all pointers on this level:
            head = leftmost
            while head is not None:
                # set pointer of this node's children
                if head.left is None:
                    return root
                # set pointer of left child
                head.left.next = head.right
                if head.next is not None:
                    # set pointer of right child
                    head.right.next = head.next.left
                # move to next node on same level (next node in bfs queue)
                head = head.next
            # move to next level, starting from the left
            leftmost = leftmost.left
        return root


    def connectNaive(self, root):
        if root is None:
            return root
        new_root = root
        root.next = None
        queue = []
        queue.append(root)
        seen = []
        seen.append(root)
        
        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            if node.left is None:
                continue
            seen.append(node.left)
            seen.append(node.right)
            queue.append(node.left)
            queue.append(node.right)
        for i, n in enumerate(seen):
            if math.log2(i+2).is_integer():
                n.next = None
            else:
                n.next = seen[i+1]
        return root