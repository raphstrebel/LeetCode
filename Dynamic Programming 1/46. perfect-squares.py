class Solution:
    def numSquares(self, n: int) -> int:
        """Bottom-up DP: Time O(N*sqrt(N)) = O(N^(3/2)), Space O(N)"""
        if n == 1 or n == 2:
            return n

        # initialize all squares until sqrt(n)
        squares = []
        for i in range(1, int(sqrt(n))+1):
            squares.append(i**2)
            
        # the problem is the same as "least sum of values to get n" (coin change)
        max_ = 10**4
        r = [max_] * (n+1)
        r[0] = 0
        r[1] = 1
        r[2] = 2
        for val in range(n+1):
            # squares are ordered, so when val is smaller than squares no need to go on
            for s in squares:
                if val < s:
                    break
                # min sum until val is either current value or min sum until val-s (so r(val-s)) + 1 (the current square s)
                r[val] = min(r[val], r[val-s] + 1)
        return r[n]