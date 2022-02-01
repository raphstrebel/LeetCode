from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = defaultdict(int)
        t_chars = defaultdict(int)
        for c in s:
            s_chars[c] += 1
        for c in t:
            t_chars[c] += 1
        return s_chars == t_chars