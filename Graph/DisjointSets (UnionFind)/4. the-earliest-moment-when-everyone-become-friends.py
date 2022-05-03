class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.num_comps = n
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
            self.num_comps -= 1
    
    def num_comps(self):
        return self.num_comps

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # sort logs by timestamp
        logs.sort(key = lambda x: x[0])
        
        graph = UnionFind(n)
        for t, x, y in logs:
            graph.union(x, y)
            if graph.num_comps == 1:
                return t
        return -1