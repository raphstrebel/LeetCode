class Solution:
    def firstUniqChar(self, s: str) -> int:
        # array of unique chars in order of appearence
        chars = []
        # hashmap of char to idx of first appearence
        char_to_idx = {}
        for i, c in enumerate(s):
            # c is in chars, so add it to char_to_idx and remove it from chars
            if c in chars:
                if c not in char_to_idx:
                    char_to_idx[c] = i
                chars.remove(c)
            else:
                # character was never seen, so append it to chars and keep first idx
                if c not in char_to_idx:
                    chars.append(c)
                    char_to_idx[c] = i
                
        if len(chars) == 0:
            return -1
        else:
            return char_to_idx[chars[0]]