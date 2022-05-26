class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # base cases: empty grid, one cell, or source/target value is 1
        if n == 0:
            return -1
        if grid[0][0] == 1 or grid[n-1][n-1]:
            return -1
        if n == 1:
            return 1
        
        adj = {}
        # construct graph adj matrix
        for i in range(n):
            for j in range(n):
                adj[(i,j)] = []
                if grid[i][j] == 1:
                    # this node cannot be used
                    continue
                # check if right, bottom, and bottom-right are valid neighbors
                if j < n-1 and grid[i][j+1] == 0:
                    adj[(i,j)].append((i, j+1))
                if i < n-1 and grid[i+1][j] == 0:
                    adj[(i,j)].append((i+1, j))
                if j < n-1 and i < n-1 and grid[i+1][j+1] == 0:
                    adj[(i,j)].append((i+1, j+1))
                # or if top-right or bottom-left are valid
                if 0 < i and j < n-1 and grid[i-1][j+1] == 0:
                    adj[(i,j)].append((i-1, j+1))
                if i < n-1 and 0 < j and grid[i+1][j-1] == 0:
                    adj[(i,j)].append((i+1, j-1))
                # or if left, top, or top-left are valid neighbors
                if 0 < j and grid[i][j-1] == 0:
                    adj[(i,j)].append((i, j-1))
                if 0 < i and grid[i-1][j] == 0:
                    adj[(i,j)].append((i-1, j))
                if 0 < i and 0 < j and grid[i-1][j-1] == 0:
                    adj[(i,j)].append((i-1, j-1))

        source = (0,0)
        target = (n-1, n-1)
        queue = [(source, 1)]
        visited = set()
        # BFS starting at source
        while queue:
            node, path = queue.pop(0)
            if node == target:
                return path
            for neigh in adj[node]:
                if not neigh in visited:
                    queue.append((neigh, path+1))
                    visited.add(neigh)
        return -1
