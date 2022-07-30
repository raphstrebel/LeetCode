class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Find the closest integer of the square root of x.
        Runtime: O(log(x))
        """
        if x == 0:
            return 0
        if x <= 3:
            return 1
        # sqrt(x) <= x/2 for x >= 4
        start, stop = 2, x // 2
        
        while start <= stop:
            mid = (start + stop) // 2
            mid_sq = mid * mid
            mid_upper_sq = mid_sq + 2 * mid + 1
            # check if mid^2 or (mid + 1)^2 = x
            if mid_sq == x:
                return mid
            if mid_upper_sq == x:
                return mid + 1
            # if mid^2 < x < (mid + 1)^2 then return mid (the closest int to sqrt(x))
            if mid_sq < x:
                if x < mid_upper_sq:
                    return mid
                # sqrt(x) is > mid
                start = mid + 1
            else:
                # sqrt(x) is < mid
                stop = mid