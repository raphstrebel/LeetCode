class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        """Space and Time complexities: O(N*M)"""
        # r[i][j] contains the number of paths until (i,j)
        # first row and column initialized at 1 until first obstacle
        n = len(grid)
        m = len(grid[0])
        r = [[0 for _ in range(m)] for _ in range(n)]
        val = 1
        for i in range(n):
            if grid[i][0] == 1:
                val = 0
            r[i][0] = val
        val = 1
        for j in range(m):
            if grid[0][j] == 1:
                val = 0
            r[0][j] = val
            
        for i in range(1, n):
            for j in range(1, m):
                # number of paths until (i,j) is number of paths until (i, j-1)
                # plus number of paths until (i-1, j)
                # except if (i,j) is an obstacle, then set r(i,j) to 0
                if grid[i][j] == 1:
                    r[i][j] = 0
                else:
                    r[i][j] = r[i][j-1] + r[i-1][j]
        return r[n-1][m-1]