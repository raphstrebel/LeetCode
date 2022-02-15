class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        r = [-1] * n
        r[n-1] = 1
        for i in range(n-2, -1, -1):
            m = min(i + nums[i], n-1)
            for j in range(i+1, m+1):
                if r[j] == 1:
                    r[i] = 1
                    break
        return r[0] == 1

    def canJumpGreedy(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        max_jump = 0
        i = 0
        while i < max_jump + 1:
            max_jump = max(max_jump, nums[i] + i)
            if max_jump >= n:
                return True
            i += 1
        return False