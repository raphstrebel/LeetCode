class UnionFind:
    def __init__(self, n):
        """n is the number of nodes"""
        self.root = [i for i in range(n)]
        self.num_roots = n
        
    def find(self, x):
        """Use path compression to update the root of x"""
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def unionIsValid(self, x, y):
        """
        Create union between roots of x and y. 
        Returns True iff the union does not create a cycle (x and y have different roots)
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x
            self.num_roots -= 1
            return True
        else:
            # x and y have the same root, so the edge (x,y) creates a cycle
            return False
    
    def isValid(self):
        """A tree is not valid if it is not connected"""
        return self.num_roots == 1

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # initialize graph
        graph = UnionFind(n)
        
        # add all edges, if an edge creates a cycle return False
        for edge in edges:
            print(edge)
            is_valid = graph.unionIsValid(edge[0], edge[1])
            if not is_valid:
                return False
        # there are no cycles, it remains to verify whether the graph is connected (has exactly one root)
        return graph.isValid()