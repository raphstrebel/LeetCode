class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if n == -1 or n == 0:
            return 0
        jumps = 0
        curr_jump = 0
        m = 0
        for i in range(n):
            # jump as far as possible
            m = max(m, i + nums[i])
            # finished current jump
            if i == curr_jump:
                jumps += 1
                curr_jump = m
        return jumps