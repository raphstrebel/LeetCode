class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """Assuming we may change the input"""
        
        n = len(grid)
        m = len(grid[0])
        
        # set first line and first column to sum of prev line/col
        for i in range(1, n):
            grid[i][0] += grid[i-1][0]
        for j in range(1, m):
            grid[0][j] += grid[0][j-1]
        
        # the min path to any index (i,j) is the min between
        # 1. the path until cell above
        # 2. the path until cell on the left
        # plus value (i,j)
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        return grid[n-1][m-1]