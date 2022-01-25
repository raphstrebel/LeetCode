class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def _search(nums, target, offset):
            len_ = len(nums)
            if len_ == 1:
                if target <= nums[0]:
                    return offset
                else:
                    return offset + 1
            if target < nums[0]:
                return offset
            if target > nums[len_-1]:
                return len_ + offset 
            if target == nums[len_-1]:
                return len_ + offset - 1
             
            
            len_2 = int(len_/2)
            if target == nums[len_2]:
                return len_2 + offset
            if target > nums[len_2]:
                return _search(nums[len_2:], target, offset+len_2)
            return _search(nums[:len_2], target, offset)
        return _search(nums, target, 0)