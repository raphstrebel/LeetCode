class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """Binary search for valid perfect square in O(log(N)) time, O(1) space."""
        # sqrt(num) <= num/2 when num >= 2 -> no need to square farther than num/2
        start, stop = 2, num // 2
        if num < 2:
            return True
        while start <= stop:
            mid = (start + stop) // 2
            mid_sq = mid ** 2
            if mid_sq == num:
                return True
            if mid_sq > num:
                stop = mid - 1
            else:
                start = mid + 1
        return False