class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        """
        DP approach: 
        - keep r, a boolean array of length s
        - for every index i in length of s, r[i] is True if:
        -     s[:i] is a word or
        -     there aree valid words until j and s[i:j] is a word
        - s can be broken into words of the dictionary iff r[len(s)-1] is True
        """
        len_s = len(s)
        r = [False] * len_s
        for i, c in enumerate(s):
            if s[:i+1] in wordDict:
                r[i] = True
            else:
                for j in range(i):
                    if r[j] and (s[j+1:i+1] in wordDict):
                        r[i] = True
                        break
        return r[len_s-1]
        