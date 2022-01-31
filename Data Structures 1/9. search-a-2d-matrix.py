class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        """Transform matrix into list, then binary search result"""
        def find_elem_rec(l, target):
            if len(l) == 1:
                if target == l[0]:
                    return True
                return False
            if len(l) == 2:
                if target == l[0] or target == l[1]:
                    return True
                return False
            mid = int(len(l)/2)
            if target == l[mid]:
                return True
            if target < l[mid]:
                return find_elem_rec(l[:mid], target)
            return find_elem_rec(l[mid+1:], target)
        
        n = len(matrix)
        m = len(matrix[0])
        l = [0]*n*m
        idx = 0
        for i in range(n):
            for j in range(m):
                l[idx] = matrix[i][j]
                idx += 1
        return find_elem_rec(l, target)