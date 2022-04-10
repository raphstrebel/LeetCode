class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # assuming we can change the input (otherwise create copy of triangle)
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        if n == 2:
            return triangle[0][0] + min(triangle[1][0], triangle[1][1])
        for i in range(1, n):
            m = len(triangle[i])
            for j in range(1, m-1):
                # at each row i column j, sum value with minimum path between j and j-1 of previous row
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
            # handle first and last elements (sum values right above)
            triangle[i][0] += triangle[i-1][0]
            triangle[i][m-1] += triangle[i-1][m-2]
        return min(triangle[n-1])