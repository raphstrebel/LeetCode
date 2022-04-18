class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """Time O(N^2) Space O(N)"""
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