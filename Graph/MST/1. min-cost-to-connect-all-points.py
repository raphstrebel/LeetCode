class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x] 

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootX]:
                self.root[rootY] = self.root[rootX]
            elif self.rank[rootX] < self.rank[y]:
                self.root[rootX] = self.root[y]
            else:
                self.root[rootY] = self.root[rootX]
                self.rank[rootX] += 1
            return True
        return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # build edges as (p_i_index, p_j_index, dist(p_i, p_j))
        edges = []
        for i, p1 in enumerate(points):
            x1, y1 = p1
            for j, p2 in enumerate(points[:i]):
                x2, y2 = p2
                edges.append((i, j, abs(x1-x2) + abs(y1-y2)))
        # sort by ascending order of weights
        edges = sorted(edges, key=lambda x: x[2])
        graph = UnionFind(n)
        total = 0
        for edge in edges:
            i, j, w = edge
            if graph.union(i, j):
                total += w
        return total