class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        Iterative search for target insert index in sorted nums:
        Time: O(log(n))
        Space: O(1)
        """
        start, stop = 0, len(arr) - 1
        while start < stop:
            mid = (start + stop) // 2
            # check if mid is higher than right neighbors
            # set start/stop accordingly
            if arr[mid] < arr[mid + 1]:
                    start = mid + 1
            else:
                stop = mid
        return start
