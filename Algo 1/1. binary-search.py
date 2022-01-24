class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _search(self, nums, target, offset):
            if len(nums) == 0 or (len(nums) == 1 and nums[0] != target):
                return -1
            mid_idx = int(len(nums)/2)
            mid = nums[mid_idx]
            if target == mid:
                return mid_idx + offset
            if target < mid:
                return _search(self, nums[:mid_idx], target, offset)
            return _search(self, nums[mid_idx:], target, offset + mid_idx)
        return _search(self, nums, target, 0)
