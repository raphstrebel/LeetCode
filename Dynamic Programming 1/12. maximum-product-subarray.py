class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        max_ = nums[0]
        min_ = nums[0]
        res = nums[0]
        
        # keep min product since next elem could be "-1"
        for num in nums[1:]:
            tmp = max(num, max_*num, min_*num)
            min_ = min(num, max_*num, min_*num)
            max_ = tmp
            
            res = max(max_, res)
        return res