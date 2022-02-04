class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}',
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if mapping[c] != last:
                    return False
        return len(stack) == 0