class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])
        r = [0] * (n+1)
        for i in range(2, n+1):
            r[i] = min(r[i-1] + cost[i-1], r[i-2] + cost[i-2])
        return r[n]