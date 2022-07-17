class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Iterative search for target insert index in sorted nums:
        Time: O(log(n))
        Space: O(1)
        """
        start, stop = 0, len(nums)-1
        while start <= stop:
            mid = (start + stop) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                stop = mid - 1
            else:
                start = mid + 1
        # target was not found, must be inserted in last "mid + 1" value
        return start