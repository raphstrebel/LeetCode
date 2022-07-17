class Solution:
    def searchIt(self, nums: List[int], target: int) -> int:
        """
        Iterative search for target in sorted nums:
        Time: O(log(n))
        Space: O(1)
        """
        start, stop = 0, len(nums)-1
        while start <= stop:
            mid = int((start + stop) / 2)
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                stop = mid - 1
            else:
                start = mid + 1
        return -1

    def searchRec(self, nums: List[int], target: int) -> int:
        """
        Recursive search for target in sorted nums:
        Time: O(log(n))
        Space: O(1)
        """
        def rec(target, start, stop):
            if start > stop:
                return -1
            if start == stop:
                return start if target == nums[start] else -1
            mid = int((start + stop)/2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return rec(target, mid + 1, stop)
            return rec(target, start, mid - 1)
        
        return rec(target, 0, len(nums) - 1)