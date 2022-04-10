class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # constraint says matrix is square
        # assuming we can change the input (otherwise create copy of matrix)
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return min(matrix[0][0], matrix[0][1]) + min(matrix[1][0], matrix[1][1])
        for i in range(1, n):
            for j in range(1, n-1):
                # in row i column j, min path sum is min path sum from previous row at indices j-1, j or j+1 (when not on first or last column)
                matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
            # handle column 0 and n-1
            matrix[i][0] += min(matrix[i-1][0], matrix[i-1][1])
            matrix[i][n-1] += min(matrix[i-1][n-2], matrix[i-1][n-1])
        return min(matrix[n-1])