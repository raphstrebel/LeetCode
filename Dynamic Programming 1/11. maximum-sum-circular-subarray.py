class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            m = -math.inf
            prev = m
            for num in arr:
                prev = max(prev + num, num)
                m = max(prev, m)
            return m
        
        # case where max subarray is not in circle
        max_sub = kadane(nums)
        print(max_sub)
        
        # invert signs in nums and compute max
        inv = [ -x for x in nums]
        max_inv = kadane(inv)
        # case max sum in circle:
        # max is sum of inverted array - max inverted (inverted)
        rest = -(sum(inv)-max_inv)
        
        # max of circular sum and normal sum
        max_all = max(rest, max_sub)
        # return max of normal sum since max might be negative,
        # if all nums are negative, only one is required (so only subarray can be max)
        if max_all == 0:
            return max_sub
        return max_all