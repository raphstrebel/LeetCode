class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        offset = 0
        words_rev = []
        for word in s.split(' '):
            words_rev.append(''.join(self.reverseString(list(word))))
            offset += len(word)
        return ' '.join(words_rev)
    
    def reverseString(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        for i in range(len(s)):
            if left >= right:
                return s
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            
            left += 1
            right -= 1