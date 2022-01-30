class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        n = len(mat)
        m = len(mat[0])
        if n * m != r * c:
            return mat
        arr = [0]*(n*m)
        idx = 0
        for i in range(n):
            for j in range(m):
                arr[idx] = mat[i][j]
                idx += 1
    
        new_arr = [[0]*c for i in range(r)]
        idx = 0
        for i in range(r):
            for j in range(c):
                new_arr[i][j] = arr[idx]
                idx += 1 
        return new_arr