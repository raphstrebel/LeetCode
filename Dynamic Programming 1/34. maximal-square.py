class Solution:
    def maximalSquareWithLinearSpace(self, matrix: List[List[str]]) -> int:
        """Keeping O(M) additional space, runtime is O(N*M)"""
        n = len(matrix)
        m = len(matrix[0])
        if n == 0 or m == 0:
            return 0
        
        # r[j] keeps the max square length until column j
        r = [0]*(m+1)
        max_ = 0  # keep track of previous max
        prev_val = 0 # store prev row and column value
        for i in range(1, n+1):
            for j in range(1, m+1):
                tmp = r[j]
                if matrix[i-1][j-1] == '1':
                    # if any of current, previous column or row is 0, r[j] is one
                    # otherwise add the minimum (since all need entries to be 1)
                    r[j] = 1 + min(r[j-1], r[j], prev_val)
                    max_ = max(r[j], max_)
                else:
                    r[j] = 0
                prev_val = tmp
        # max_ keeps length of square, not number of elements
        return max_**2
    def maximalSquareNaive(self, matrix: List[List[str]]) -> int:
        """Keeping O(N*M) additional space, runtime is O(N*M)"""
        n = len(matrix)
        m = len(matrix[0])
        if n == 0 or m == 0:
            return 0
        
        # r[i,j] keeps the max square length from (0,0) to (i-1,j-1)
        r = a = [[0]*(m+1) for _ in range(n+1)]
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