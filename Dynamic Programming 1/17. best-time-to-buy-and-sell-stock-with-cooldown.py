class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 1:
            return 0
        # 3-state machine:
        sell = -1001  # sell previously bought stock
        keep = -1001  # keep previously bought stock
        cooldown = 0  # state after 'sell', where we cannot buy
        
        for p in prices:
            sell_prev = sell
            sell = keep + p
            keep = max(keep, cooldown - p)
            cooldown = max(cooldown, sell_prev)
        
        return max(sell, cooldown)