class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Runtime O(N^2), Space O(1)"""
        n = len(s)
        # base cases
        if s == '' or n == 1:
            return s
        if n == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        def compare_left_right(left, right):
            """compare left and right of middle char while they are equal"""
            while left >= 0 and right <= n-1 and s[left] == s[right]:
                left -= 1
                right += 1
            # the left/right indices were shifted once after the condition was last met
            return left+1, right-1
        # indices and len of maximum palindrome
        start, end = 0, 0
        len_max = 0
        # set each i as center and compare left and right from there
        for i in range(n-1):
            # try palindrome with no midde char (e.g. "abba")
            start_1, end_1 = compare_left_right(i, i)
            len_1 = end_1 - start_1
            # try palindrome with middle char (e.g. "abcba")
            start_2, end_2 = compare_left_right(i, i+1)
            len_2 = end_2 - start_2
            
            # update longest palindrome start/stop indices
            if len_1 > len_2:
                if len_1 > len_max:
                    len_max = len_1
                    start = start_1
                    end = end_1
            else:
                if len_2 > len_max:
                    len_max = len_2
                    start = start_2
                    end = end_2
        return s[start:end+1]