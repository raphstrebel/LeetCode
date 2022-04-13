class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """Keeping O(N*M) additional space, runtime is O(N*M)"""
        n = len(matrix)
        m = len(matrix[0])
        if n == 0 or m == 0:
            return 0
        
        # r[i,j] keeps the max square length from (0,0) to (i-1,j-1)
        r = [[0 for j in range(m+1)] for i in range(n+1)]
        max_ = 0  # keep track of previous max
        for i in range(1, n+1):
            for j in range(1, m+1):
                # if not '1' then r[i,j] is 0 by default
                if matrix[i-1][j-1] == '1':
                    # if one of the lines right before (i,j) is 0
                    # then r[i,j] is 1, otherwise prev square size + 1
                    r[i][j] = 1 + min(r[i-1][j-1], r[i-1][j], r[i][j-1])
                    max_ = max(r[i][j], max_)
        # max_ keeps length of square, not number of elements
        return max_**2