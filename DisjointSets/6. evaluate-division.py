class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        # contains value of each index i found
        self.values = {}
        
    def find(self, x):
        # If no value was assigned to x, assign 1
        if not self.values.get(x):
            self.values[x] = 1
        
        if self.root[x] != x:
            # update root and value of x using find() on root
            newRootX, newValX = self.find(self.root[x])
            self.root[x] = newRootX
            self.values[x] = self.values[x] * newValX
        return self.root[x], self.values[x]
    
    def union(self, x, y, val):
        rootX, valX = self.find(x)
        rootY, valY = self.find(y)
        
        if rootX != rootY:
            # x/y = val, so update x = prevY * val / prevX
            self.root[rootX] = rootY
            self.values[rootX] = valY * val / valX

    def getVal(self):
        return self.values
            

class Solution:
    def calcEquation(self, equations, values, queries):
        # initialize UnionFind with all elements in equations
        elems = set()
        for x, y in equations:
            elems.add(x)
            elems.add(y)
        elems_to_idx = {e: i for i, e in enumerate(elems)}
        graph = UnionFind(len(elems))
        
        # inside any component (elements sharing the same root), we know all divisions
        for i, equ in enumerate(equations):
            x, y = equ
            graph.union(elems_to_idx[x], elems_to_idx[y], values[i])
        
        # res contains the weight of each element
        res = graph.getVal()
        
        results = []
        for x, y in queries:
            if x not in elems or y not in elems:
                results.append(-1)
            else:
                rootX, valX = graph.find(elems_to_idx[x])
                rootY, valY = graph.find(elems_to_idx[y])
                if rootX == rootY:
                    results.append(valX/valY)
                else:
                    # not part of same comp -> don't have link between x and y
                    results.append(-1)
        return results
