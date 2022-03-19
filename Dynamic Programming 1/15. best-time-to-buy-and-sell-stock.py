class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        r = [0] * n
        low_left = prices[0]
        for i, p in enumerate(prices[1:]):
            r[i] = max(r[i-1], p - low_left)
            if low_left > p:
                low_left = p
        return r[n-2]