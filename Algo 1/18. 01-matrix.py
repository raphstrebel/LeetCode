class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # DP solution
        n = len(mat)
        m = len(mat[0])
        res = [[math.inf]*m for _ in range(n)]
        # top-left to bottom-right
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    # distance is either 0 or min of left/top cell + 1
                    if 0 <= i-1 < n:
                        res[i][j] = min(res[i][j], res[i-1][j]+1)
                    if 0 <= j-1 < m:
                        res[i][j] = min(res[i][j], res[i][j-1]+1)
        # bottom-right to top-left
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if mat[i][j] == 1:
                    # distance is either 0 or min of right/bottom cell + 1
                    if 0 <= i+1 < n:
                        res[i][j] = min(res[i][j], res[i+1][j]+1)
                    if 0 <= j+1 < m:
                        res[i][j] = min(res[i][j], res[i][j+1]+1)
        return res