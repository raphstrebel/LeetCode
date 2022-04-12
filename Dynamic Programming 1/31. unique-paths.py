class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # r[i][j] contains the number of paths until (i,j)
        # initialized at 1 since only one path for borders
        r = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                # number of paths until (i,j) is number of paths until (i, j-1)
                # plus number of paths until (i-1, j)
                r[i][j] = r[i][j-1] + r[i-1][j]
        return r[n-1][m-1]