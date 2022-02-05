class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        flag = set()
        def maxAreaRec(r, c):
            if (r,c) in flag:
                return 0
            flag.add((r,c))
            if grid[r][c] == 0:
                return 0
            count = 1
            if r > 0:
                count += maxAreaRec(r-1, c)
            if r < nrows-1:
                count += maxAreaRec(r+1, c)
            if c > 0:
                count += maxAreaRec(r, c-1)
            if c < ncols-1:
                count += maxAreaRec(r, c+1)
            return count
        max_ = 0
        for i in range(nrows):
            for j in range(ncols):
                area = maxAreaRec(i, j)
                max_ = max(max_, area)
        return max_