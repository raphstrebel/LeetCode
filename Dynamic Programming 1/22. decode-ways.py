class Solution:
    def numDecodings(self, s: str) -> int:
        
        last_idx = len(s) - 1
        valid_first = set([str(i) for i in range(1, 10)])
        valid_pair = set([str(i) for i in range(10, 27)])
        r = [-1] * (len(s)+1)
        if s == "" or s[0] not in valid_first:
            return 0
        def numDecRec(i):
            if r[i] >= 0:
                return r[i]
            if i == last_idx+1:
                r[i] = 1
                return 1
            if not s[i] in valid_first:
                r[i] = 0
                return 0
            if i == last_idx:
                r[i] = 1
                return 1
            num = numDecRec(i+1)
            if s[i:i+2] in valid_pair:
                num += numDecRec(i+2)
            r[i] = num
            return num
        return numDecRec(0)