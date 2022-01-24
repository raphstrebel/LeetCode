class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        last_good = 1
        first_bad = n
        while(last_good < first_bad):
            mid = last_good + int((first_bad-last_good)/2)
            if isBadVersion(mid):
                first_bad = mid
            else:
                last_good = mid + 1
        return last_good