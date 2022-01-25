class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], nums[i] + curr)
            max_ = max(max_, curr)
        return max_