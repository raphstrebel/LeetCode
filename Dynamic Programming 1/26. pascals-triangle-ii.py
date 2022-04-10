class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """'Naive' solution: generate triangle of length 'rowIndex' and return the last row"""
        def generate(numRows: int) -> List[List[int]]:
            if numRows == 1:
                return [[1]]
            if numRows == 2:
                return [[1], [1,1]]

            t = [[1], [1,1]]
            for i in range(2, numRows):
                row = [1]
                for j in range(1, i):
                    row.append(t[i-1][j-1] + t[i-1][j])
                row.append(1)
                t.append(row)
            return t
        return generate(rowIndex+1)[rowIndex]