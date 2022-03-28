class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        res = 0
        prev = 1001 # -1000 <= nums <= 1000
        diff = 2001
        # in [1,2,3,4], there are three arithmetic slices:
        # [1,2,3], [2,3,4], [1,2,3,4]
        # and at every new i'th element with same difference, there are i more subarrays
        # so "streak" keeps track of the number of consecutive ar. subarrays we have seen
        streak = 0  
        for num in nums:
            new_diff = num - prev
            if new_diff == diff:
                streak += 1
                res += streak
            else:
                # streak breaks
                streak = 0
            diff = new_diff
            prev = num
        return res