class Solution:
    def longestPalindromeSubseq_LinearSpace(self, s: str) -> int:
        """Runtime O(N^2), space O(N)"""
        n = len(s)
        if n == 0 or n == 1:
            return n
        # keep 2 array: 
        # curr with longest pal. from i to all j
        # prev with longest pal. from i-1 to all j
        curr = [0 for _ in range(n+1)]
        prev = [0 for _ in range(n+1)]
        s_rev = s[::-1]
        for i in range(1, n+1):
            for j in range(1, n+1):
                # compare rev string at j-1:
                if s[i-1] == s_rev[j-1]:
                    # length at j is 1 + s[i to j-1]
                    curr[j] = 1 + prev[j-1]
                else:
                    # keep max between s[i-1 to j] and s[i to j-1] 
                    curr[j] = max(prev[j], curr[j-1])
            # update prev to curr
            prev = curr[:]
        return prev[n]

    def longestPalindromeSubseq_SquareSpace(self, s: str) -> int:
        """Runtime O(N^2), space O(N^2)"""
        n = len(s)
        if n == 0 or n == 1:
            return n
        # keep the max pal. len for s[i-1] until s[j-1] (1 <= i, j <= n)
        # (first row and col of r is 0)
        r = [[0 for _ in range(n+1)] for _ in range(n+1)]
        s_rev = s[::-1]
        for i in range(1, n+1):
            for j in range(1, n+1):
                # check the reverse string:
                if s[i-1] == s_rev[j-1]:
                    # len = 1 + previous max length
                    r[i][j] = 1 + r[i-1][j-1]
                else:
                    # len = previous max
                    r[i][j] = max(r[i][j-1], r[i-1][j])
        return r[n][n]