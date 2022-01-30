class Solution:
    def generate(self, numRows: int):
        r = [[1]]
        if numRows == 1:
            return r
        for i in range(1, numRows):
            r.append([])
            r[i].append(1)
            for j in range(1,i):
                r[i].append(r[i-1][j-1] + r[i-1][j])
            r[i].append(1)
        return r