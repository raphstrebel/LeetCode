class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        def robArray(nums: List[int]) -> int:
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums[0], nums[1])
            r = [0] * n
            r[0] = nums[0]
            r[1] = max(nums[0], nums[1])

            for i in range(2, n):
                r[i] = max(r[i-1], r[i-2] + nums[i])

            return r[n-1]
        return max(robArray(nums[:len(nums)-1]), robArray(nums[1:]))
