class Solution:
    def uniquePathsComb(self, m: int, n: int) -> int:
        """
        Using combinatorics:
        we can choose n-1 paths from (m-1) + (n-1) total cells
        -> nCr(n-1,m+n-2) = (m+n-2)! / ((n-1)! (m+n-2-n+1)!)
        = (m+n-2)! / ((n-1)! (m-1)!)
        """
        # or on python >= 3.8: math.comb(m + n - 2, n - 1)
        return factorial(m+n-2)//(factorial(n-1)*factorial(m-1))
    def uniquePathsDP(self, m: int, n: int) -> int:
        """Naive using dynamic programming"""
        # r[i][j] contains the number of paths until (i,j)
        # initialized at 1 since only one path for borders
        r = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                # number of paths until (i,j) is number of paths until (i, j-1)
                # plus number of paths until (i-1, j)
                r[i][j] = r[i][j-1] + r[i-1][j]
        return r[n-1][m-1]