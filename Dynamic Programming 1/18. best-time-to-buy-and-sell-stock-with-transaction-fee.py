class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        
        profit = 0
        prev_min = prices[0]
        
        for p in prices[1:]:
            # is the gain > 0?
            gain = p - prev_min - fee
            if gain > 0:
                profit += gain
                # previous min is price to pay in the future if we did not buy now but kept our stock until then
                prev_min = p - fee
            else:
                # don't sell, but maybe it's better to buy now than previous
                prev_min = min(prev_min, p)
        return profit