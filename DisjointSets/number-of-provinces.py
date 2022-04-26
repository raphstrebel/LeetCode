class UnionFind:
    def __init__(self, n):
        """n is the number of nodes"""
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x):
        """Use path compression to update the root of x"""
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        """Use ranks of tree roots to balance trees"""
        # if x and y are connected, nothing to do
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = self.root[root_x]
            elif self.rank[root_y] > self.rank[root_x]:
                self.root[root_x] = self.root[root_y]
            else:
                # both ranks are equal, choose first root and increment rank
                self.root[root_y] = self.root[root_x]
                self.rank[root_x] += 1
    
    def connected(self, x, y):
        """True iff x and y have the same root"""
        return self.find(x) == self.find(y)
    
    def num_roots(self):
        """Number of different roots (of disjoint sets)"""
        roots = set()
        for r in self.root:
            # use find to update roots
            roots.add(self.find(r))
        return len(roots)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """Find the number of disjoint sets by creating UnionFind graph"""
        # initialize graph
        n = len(isConnected)
        graph = UnionFind(n)
        
        # make union of i and j if isConnected[i, j] is 1
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph.union(i, j)
        return graph.num_roots()
