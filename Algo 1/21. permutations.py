class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [nums]
        if n == 2:
            return [nums, [nums[1], nums[0]]]
        def permuteRec(first):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # swap indices "first" and "i"
                nums[first], nums[i] = nums[i], nums[first]
                permuteRec(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        res = []
        permuteRec(0)
        return res