class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """Greedy: Time O(N), Space O(1)"""
        n = len(nums)
        
        # base cases
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1 if nums[0] == nums[1] else 2
        
        # prev_pos: diff between elements at i-2 and i-1 was positive
        # prev_neg: diff between elements at i-2 and i-1 was negative
        # (ignoring consecutive same elements in the array)
        if nums[0] == nums[1]:
            prev_pos = True
            prev_neg = True
            max_ = 1
        else:
            prev_pos = nums[0] < nums[1]
            prev_neg = nums[0] > nums[1]
            max_ = 2
        for i in range(2, n):
            # is diff between elements at i-1 and i pos or neg?
            if nums[i-1] < nums[i]:
                # if positive and previous was negative, increment and switch prev_pos/neg
                if prev_neg:
                    max_ += 1
                    prev_pos = True
                    prev_neg = False
            elif nums[i-1] > nums[i]:
                # if neg and previous was pos, increment and switch prev_pos/neg
                if prev_pos:
                    max_ += 1
                    prev_pos = False
                    prev_neg = True
        return max_
    def wiggleMaxLengthDP(self, nums: List[int]) -> int:
        """Dynamic Prog: Time O(N^2) Space O(N)"""
        n = len(nums)
        
        # base cases
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1 if nums[0] == nums[1] else 2
        
        # pos/neg at i contains len of longest wiggle subseq. where i is
        # last element of subseq. with pos/neg diff w.r.t previous element
        pos = [1] * n
        neg = [1] * n
        prev_pos = False
        for i in range(1, n):
            # update pos[i] and neg[i] as:
            # 1 + max of prev subseq. where diff between last and curr elements is pos/neg
            for j in range(0, i):
                if nums[j] < nums[i]:
                    pos[i] = max(pos[i], neg[j] + 1)
                elif nums[j] != nums[i]:
                    neg[i] = max(neg[i], pos[j] + 1)
        return max(neg[n-1], pos[n-1])