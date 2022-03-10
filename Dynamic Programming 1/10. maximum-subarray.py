class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        max_ = nums[0]
        
        # keep prev sum, whenever it becomes negative, start from current number
        for i in range(1, len(nums)):
            # if prev < 0, keep current number
            # otherwise sum current number with prev
            prev = max(0, prev) + nums[i]
            max_ = max(max_, prev)
            
        return max_

    def maxSubArray(self, nums: List[int]) -> int:
        """Returns max sum and best subarray"""
        n = len(nums)
        prev = nums[0]
        max_ = nums[0]
        best_s = []
        s = []
        # keep prev sum, whenever it becomes negative, start from current number
        for i in range(1, len(nums)):
            # if prev < 0, keep current number
            # otherwise sum current number with prev
            if prev < 0:
                prev = nums[i]
                s = [nums[i]]
            else:
                prev += nums[i]
                s.append(nums[i])
            
            if max_ < prev:
                max_ = prev
                best_s = s[:]
        return max_, best_s