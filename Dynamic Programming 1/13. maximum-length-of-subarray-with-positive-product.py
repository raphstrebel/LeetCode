class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """
        1. split array on 0's (since x * 0 is not positive)
        2. assuming no 0's in the array, build list of negative number indices
        3. if there is an even number of negatives, return array length (since 2 negs make a pos)
        4. if there is one negative, output the max of "0 to neg index", "neg index to n-1"
        5. lastly, if there are an odd number of 3 negs or more, consider only the first and last negs,
           since the middle negatives will compensate eachother. The max length of products that remains positive
           is the max of "0 to last neg" or "first neg to n-1"
        """
        def getMaxWithoutZeros(arr):
            """Find max continuous positive product without zeros"""
            # find indices of negative numbers
            neg_indices = []
            for i, num in enumerate(arr):
                if num < 0:
                    neg_indices.append(i)
            n = len(arr)
            nb_negs = len(neg_indices)
            # if even number of negatives, product of all is positive
            if nb_negs % 2 == 0:
                return n
            # otherwise, all pairs of negatives compensate and one negative remains, so keep the negative index closest to 0 or n-1
            return max(n-1-neg_indices[0], neg_indices[nb_negs-1])
        m = 0
        prev_zero = -1
        has_zeros = False
        # split array on zeros and keep max of those non-zero arrays
        for i, num in enumerate(nums):
            if num == 0:
                m = max(m, getMaxWithoutZeros(nums[prev_zero+1:i]))
                prev_zero = i
                has_zeros = True
        if not has_zeros:
            return getMaxWithoutZeros(nums)
        else:
            return max(m, getMaxWithoutZeros(nums[prev_zero+1:]))