class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        Runtime: O(N*log(N)):
        - O(N*log(N)) for sorting, then O(log(N)) for while-loop
        Space: O(N) if sorting is done in-place, otherwise O(N*log(N))
        """
        # e.g. [4,4,3,0,0]
        nums = sorted(nums, reverse=True)
        n = len(nums)
        start, stop = 0, n
        
        while start < stop:
            mid = (start + stop) // 2
            # if index is smaller than number at index, then 
            # the special number is to the right
            # otherwise, to the left
            if mid < nums[mid]:
                start = mid + 1
            else:
                stop = mid
        return -1 if start < n and start == nums[start] else start