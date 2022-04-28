class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    
    def getRoots(self):
        return self.root
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        graph = UnionFind(n)
        for x, y in pairs:
            graph.union(x, y)
        
        # inside a component (elements with common root), the elements can be
        # order as we want, so for all roots, we order elements from
        # lexicographically lowest to highest
        
        # keep elements of each root
        roots_to_elems = defaultdict(list)
        for x in range(n):
            roots_to_elems[graph.find(x)].append(x)
            
        # sort elements in each root
        s = list(s)  # string does not support item assignment
        for root, elems in roots_to_elems.items():
            # sort chars in root
            chars = sorted([s[x] for x in elems])
            # reorder elements in s
            for i, c in enumerate(chars):
                s[elems[i]] = c
        return ''.join(s)
            