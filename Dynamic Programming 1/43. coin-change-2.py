class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """Buttom-up DP: Time O(N*amount) Space O(amount)"""
        n = len(coins)
        if amount == 0 or n == 0:
            return 1
        
        r = [0] * (amount+1)
        r[0] = 1  # there is one combination to reach amount 0: take 0 coins
        for coin in coins:
            for val in range(coin, amount+1):
                # at any coin: increment amount of coins until any value x (greater than coin value)
                # by the amount of coins until the difference between x and the coin
                r[val] = r[val] + r[val-coin]
        return r[amount]