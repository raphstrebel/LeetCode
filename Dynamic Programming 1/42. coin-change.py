class Solution:
    def coinChangeRecWithCaching(self, coins: List[int], amount: int) -> int:
        """Recursion with caching: O(total*N) time complexity"""
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        
        # sort coins, discard coins greater than amount
        # if any coin has the required amount, return 1
        coins = sorted(coins, reverse=True)
        for i, c in enumerate(coins):
            if c == amount:
                return 1
            elif c < amount:
                break
        coins = coins[i:]
        # no coins with value less than amount
        if len(coins) == 0:
            return -1
        
        @lru_cache(maxsize=None)
        def coinChangeRec(total):
            if total == 0:
                return 0
            if total < 0:
                # easier to keep track of minimum
                return math.inf
            # compute minimum of "total - any coin", plus one since we use a coin
            return 1 + min([coinChangeRec(total-i) for i in coins])
        res = coinChangeRec(amount)
        if res == math.inf:
            return -1 
        return res

    def coinChangeBottomUp(self, coins: List[int], amount: int) -> int:
        """Bottom-up with Time O(N*amount), Space O(amount)"""
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        
        # keeps number of coins needed for any amount
        r = [math.inf] * (amount+1)
        r[0] = 0  # an amount of 0 needs 0 coins
        for coin in coins:
            for rest in range(coin, amount+1):
                r[rest] = min(r[rest], 1 + r[rest-coin])
        res = -1 if r[amount] == math.inf else r[amount]
        return res