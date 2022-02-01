from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars_to_freq = defaultdict(int)
        # keep all chars seen in a set for faster access
        chars = set()
        for c in ransomNote:
            # count frequency and add new chars
            chars_to_freq[c] += 1
            chars = chars.union({c})
        for c in magazine:
            # c not in chars, then we don't need the letter
            if c not in chars:
                continue
            chars_to_freq[c] -= 1
            # check if we need more of the same letter, if not remove from chars
            if chars_to_freq[c] <= 0:
                chars = chars - set({c})
                if len(chars) == 0:
                    return True
        return len(chars_to_freq) == 0
