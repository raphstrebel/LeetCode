class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        tmp = nums[len(nums)-k:]
        tmp += nums[:len(nums)-k]
        nums.clear()
        nums.extend(tmp)
