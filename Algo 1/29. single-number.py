class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        a xor a = 0, so when applying xor to all elements, we keep the 
        only unique.
        """
        res = 0
        for n in nums:
            res = res ^ n
        return res