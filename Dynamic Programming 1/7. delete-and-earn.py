class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
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
                r[i] = max(r[i-2] + nums[i], r[i-1])
            return r[n-1]

        nums_len = len(nums)
        if nums_len == 0:
            return 0
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        unique = sorted(count.keys())
        unique_sep = []
        prev = -10
        for n in unique:
            if n - 1 != prev:
                unique_sep.append(0)
            unique_sep.append(n*count[n])
            prev = n
        return robArray(unique_sep)
