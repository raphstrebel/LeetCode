class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return mat
        
        n = len(mat)
        m = len(mat[0])
        
        # if k at least max(n, m) then all cells are summed with eachother
        if k >= max(n, m):
            s = sum([sum(row) for row in mat])
            return [[s for _ in range(m)] for _ in range(n)]
        
        
        # r contains the block sum from index (0, 0) to (i, j)
        r = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                # r[i+1][j+1] is the value at (i,j) + the block sum at (i+1, j) and (i, j+1) - intersection
                r[i+1][j+1] += mat[i][j] + r[i][j+1] + r[i+1][j] - r[i][j]
        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                # i and j are in [0, n-1] and [0, m-1] resp
                i_1 = max(0, i - k)
                i_2 = min(i + k, n - 1)
                j_1 = max(0, j - k)
                j_2 = min(j + k, m - 1)
                # at (i,j), block sum around k is:
                # block sum of (0,0) until (i,j) + r(i-k+1, j-k) - r(i-k, j+k+1) - r(i+k+1, j-k)
                res[i][j] = r[i_1][j_1] + r[i_2 + 1][j_2 + 1] - r[i_1][j_2 + 1] - r[i_2 + 1][j_1]
        return res