class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        max_ = 10**4 + 1
        r = [[max_] * len(i) for i in triangle]
        num_levels = len(triangle)
        if num_levels == 0:
            return 0
        if num_levels == 1:
            return triangle[0][0]
        r[0][0] = triangle[0][0]
        
        def minTotalRec(l, i):
            #print(l, i)
            if r[l][i] < max_:
                # we computed this already
                return r[l][i]
            if i == 0:
                # must take index 0 of above level
                r[l][0] = triangle[l][i] + minTotalRec(l-1, 0)
            elif i == len(triangle[l]) - 1:
                # must take last index of above level
                r[l][i] = triangle[l][i] + minTotalRec(l-1, i-1)
            else:
                # take min path of above level
                r[l][i] = triangle[l][i] + min(minTotalRec(l-1, i),
                                               minTotalRec(l-1, i-1))
            return r[l][i]
        min_ = max_
        # in last level, compute all paths leading to each element, keeping min
        for j in range(len(triangle[num_levels-1])):
            path = minTotalRec(num_levels-1, j)
            min_ = min(min_, path)
        return min_