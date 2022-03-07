class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [[]]
        
        for c in s:
            n = len(res)
            if c.isdigit():
                for i in range(n):
                    res[i].append(c)
            else:
                for i in range(n):
                    res.append(res[i][:])
                    res[i].append(c.lower())
                    res[i+n].append(c.upper())
        return ["".join(r) for r in res]