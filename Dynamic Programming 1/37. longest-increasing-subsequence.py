class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n
        # r(i) contains the length of the max increasing subsequence between 0 and i
        r = [1 for _ in range(n)]
        max_ = 1
        for i in range(1, n):
            for j in range(i):
                # if elem before index i is smaller
                if nums[j] < nums[i]:
                    # update r(i) if 1 + max subsequence until j was creater
                    r[i] = max(r[i], 1 + r[j])
                    if max_ < r[i]:
                        max_ = r[i]
        return max_