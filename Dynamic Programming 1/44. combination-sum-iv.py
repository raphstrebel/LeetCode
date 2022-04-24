class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """Time O(N*target), Space O(target)"""
        n = len(nums)
        if n == 0 or target == 0:
            return 1
        
        r = [0] * (target + 1)
        r[0] = 1
        
        for sub_target in range(target+1):
            for num in nums:
                # if num is not greater than sub-target, then increment nb of combinations until sub-target by nb of combinations until sub-target - num (since sub-target can be reached from num)
                if sub_target >= num:
                    r[sub_target] = r[sub_target] + r[sub_target-num]
        return r[target]