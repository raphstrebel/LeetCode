class Solution:
    def minPathSumLinearSpace(self, grid: List[List[int]]) -> int:
        """Assuming we may NOT change the input -> O(N) extra space"""
        
        n = len(grid)
        m = len(grid[0])
        # initialize r to be the last element
        r = [grid[n-1][m-1]] * m
        # iterate from down-right to top-left, keeping the min path sum at each row
        for i in range(n-1, -1, -1):
            # for every line, r contains the min path sum until every column
            # so we need to keep only an array of length M
            # r[j] contains either the sum until r[j+1] (the path sum on the right of j)
            # or the sum until r[j] (the path sum until the element below j, which was computed on the previous row "i-1")
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1:
                    # bottom-right value was initialized
                    continue
                elif i == n - 1 and j != m - 1:
                    # if last row, then consider only the value on the right (next column)  
                    r[j] = grid[i][j] + r[j+1]
                elif i != n - 1 and j == m - 1:
                    # if last column, then consider only the value below (row i-1) 
                    r[j] = grid[i][j] + r[j]
                else:
                    # consider the minimum between the value below and value on the right
                    r[j] = grid[i][j] + min(r[j], r[j+1])
        return r[0]
    def minPathSumChangeInput(self, grid: List[List[int]]) -> int:
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