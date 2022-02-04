class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # char to last index of char (plus one)
        chars_to_idx = {}
        max_ = 0
        sub_start = 0
        for i, c in enumerate(s):
            if c in chars_to_idx:
                # char is duplicate, move start to new position of char (if greater than previous substring start)
                sub_start = max(sub_start, chars_to_idx[c])
            # update new max if substring is bigger than previous
            max_ = max(max_, i - sub_start + 1)
            chars_to_idx[c] = i + 1
        return max_
                
