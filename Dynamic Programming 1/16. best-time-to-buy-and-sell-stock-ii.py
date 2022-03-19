class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_ = 0
        prev_low = prices[0]
        
        for i, p in enumerate(prices[1:]):
            if prev_low < p:
                # buy previous day and sell now
                max_ += p - prev_low
                prev_low = p
            elif prev_low > p:
                # don't buy on previous day, but update previous lowest
                prev_low = p
        return max_