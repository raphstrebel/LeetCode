class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(self.root[x])
        rootY = self.find(self.root[y])
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False
    
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # set new node 0 with edge to all nodes and weight well-cost at each node
        for node, well_cost in enumerate(wells):
            pipes.append([0, node+1, well_cost])
        n += 1
        
        # solve min spanning tree (Kruskal using Union-Find)
        graph = UnionFind(n)
        # sort pipes by ascending order of weight
        pipes = sorted(pipes, key=lambda x: x[2])
        total = 0
        for x, y, w in pipes:
            # if x and y are not connected, add weight of edge
            # it is the smallest edge connecting roots of x and y
            if graph.union(x, y):
                total += w
        return total