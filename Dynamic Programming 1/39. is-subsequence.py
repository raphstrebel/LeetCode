class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Greedy: time O(N), space O(1)"""
        if s == '':
            return True
        if t == '':
            return False
        if len(t) < len(s):
            return False
        i = 0
        s_len = len(s)-1
        s_char = s[0]
        # check all chars in t until chars of s are found (in order)
        for t_char in t:
            # if a char of t is found, the next t char is searched in 
            # the remaining chars of t
            if t_char == s_char:
                if i == s_len:
                    return True
                i += 1
                s_char = s[i]
        return False