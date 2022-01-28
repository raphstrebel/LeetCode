class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        for c in s:
            if left >= right:
                return
            s[left] = s[right]
            s[right] = c
            
            left += 1
            right -= 1