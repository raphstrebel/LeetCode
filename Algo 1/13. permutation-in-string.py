from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        
        # set char frequency of s1
        for c in s1:
            s1_freq[ord(c) - 97] += 1
        
        for i, c in enumerate(s2):
            # increase frequency of current character
            s2_freq[ord(c) - 97] += 1
            
            if i >= l1:
                # chars frequency before start of window must be decreased
                s2_freq[ord(s2[i - l1]) - 97] -= 1
            
            # frequency of all characters is equal -> substring exists
            if s1_freq == s2_freq:
                return True
        return False