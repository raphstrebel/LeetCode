# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Using Binary Search:
        Time: O(log(N))
        Space: O(1)
        """
        # Constraint: there is at least one bad version
        if n == 0 or n == 1:
            return n
        start, stop = 1, n
        while start < stop:
            mid = (start + stop) // 2
            bad = isBadVersion(mid)
            if bad:
                stop = mid
            else:
                start = mid + 1
        return start