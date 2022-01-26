class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[last_non_zero] = n
                last_non_zero += 1
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0