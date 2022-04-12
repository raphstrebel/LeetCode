class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        # r[i+1,j+1] contains block sum of (0,0) to (i,j)
        # (makes it easier to handle the cases row1 = row2 and/or col1 = col2)
        self.r = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                self.r[i+1][j+1] = matrix[i][j] + self.r[i+1][j] + self.r[i][j+1] - self.r[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Return the block sum from 0,0 to i,j minus the blocks (0,0) to (row1, col2) and (0,0) to (row2, col1)
        plus the intersection (which was subtracted twice).
        """
        return self.r[row2+1][col2+1] - self.r[row1][col2+1] - self.r[row2+1][col1] + self.r[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)