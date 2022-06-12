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
    def minCostConnectPointsKruskal(self, points: List[List[int]]) -> int:
        """
        Build a complete graph by computing distances between all pairs of points. So E = V^2.
        Runtime: O(E*log(E)) = O(V^2*log(V)) since log(V^2) = 2*log(V)
            - O(V^2) = O(E) to build graph
            - O(E*log(E)) for sorting
            - O(alpha(V)) for Kruskal's algo using UnionFind (alpha is inverse Ackermann's function)
        Space: O(E) = O(N^2)
            - O(E) to store the graph
            - let's assume in-place, or at most O(E) space
            - O(V) = O(sqrt(E)) for UnionFind
        """
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
        total_weight = 0
        total_edges = 0
        for edge in edges:
            i, j, w = edge
            if graph.union(i, j):
                total_weight += w
                total_edges += 1
            if total_edges == n-1:
                return total_weight
        return total_weight

    def minCostConnectPointsPrim(self, points: List[List[int]]) -> int:
        """
        MST using Prim's algorithm.
        Runtime O(N^2):
            Select each node to be added to MST (N nodes). Every time a node
            is added, min distances to every other node are updated -> O(N^2)
        Space O(N):
            Use a set of size N and and array of size N.
        """
        n = len(points)
        if n == 0 or n == 1:
            return 0
        # minimum distances from MST to this each point
        dist = [math.inf] * n
        dist[0] = 0
        
        total = 0
        included = set()
        # MST has n-1 edges        
        num_edges = 0
        while num_edges != n:
            # add minimum edge from MST to non-included node
            min_ = math.inf
            curr = -1
            for i in range(n):
                if not i in included and dist[i] < min_:
                    curr = i
                    min_ = dist[i]
            # update total MST weight and included nodes
            total += min_
            included.add(curr)
            num_edges += 1
            # update min distances with edges from curr to non-included nodes
            for i in range(n):
                if not i in included:
                    x1, y1 = points[curr]
                    x2, y2 = points[i]
                    dist[i] = min(dist[i], abs(x1 - x2) + abs(y1 - y2))
        return total