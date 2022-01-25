class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negs = []
        pos = []
        if len(nums) == 1:
            return [nums[0]*nums[0]]
        for num in nums:
            if num < 0:
                negs.append(num*num)
            else:
                pos.append(num*num)
        
        if len(negs) == 0:
            return pos
        negs = negs[::-1]
        if len(pos) == 0:
            return negs
        if len(pos) == 1 and len(negs) == 1:
            return [min(pos[0], negs[0]), max(pos[0], negs[0])]
        lowest_negs = 0
        lowest_pos = 0
        pos_len = len(pos) 
        negs_len = len(negs)
        nums = [0] * len(nums)
        for i in range(len(nums)):
            if pos[lowest_pos] < negs[lowest_negs]:
                nums[i] = pos[lowest_pos]
                lowest_pos += 1
                if lowest_pos == pos_len:
                    return nums[:i+1] + negs[lowest_negs:]
            else:
                nums[i] = negs[lowest_negs]
                lowest_negs += 1
                if lowest_negs == negs_len:
                    return nums[:i+1] + pos[lowest_pos:]
        return nums