class Solution:
    def longestCommonSubsequenceTopDownNaive(self, text1: str, text2: str) -> int:
        """Time O(N*M^2): iterate over text2 (length M) for N*M suproblems, Space O(N*M) to store all subproblems"""
        n1 = len(text1)
        n2 = len(text2)
        
        @lru_cache(maxsize=None)
        def lcs_rec(i1, i2):
            if i1 == n1 or i2 == n2:
                return 0

            # take first char of text1, compare with all chars of text2
            c1 = text1[i1]
            found = False
            for i in range(i2, n2):
                if c1 == text2[i]:
                    found = True
                    break
            if not found:
                # c1 was not found, move to next letter of text1
                return lcs_rec(i1+1, i2)
            # either we take the letter in the opt. solution (1 + remaining parts of text1 and text2)
            # or we don't (ignore c1 in text1)
            return max(1+lcs_rec(i1+1, i+1),
                       lcs_rec(i1+1, i2))
        return lcs_rec(0,0)

    def longestCommonSubsequenceTopDown(self, text1: str, text2: str) -> int:
        """Improvement on first solution: Time O(N*M), Space O(N*M)"""
        n1 = len(text1)
        n2 = len(text2)
        
        @lru_cache(maxsize=None)
        def lcs_rec(i1, i2):
            if i1 == n1 or i2 == n2:
                return 0

            if text1[i1] == text2[i2]:
                # first letters are the same, so move to next letters in text1 and text2
                return 1 + lcs_rec(i1+1, i2+1)

            # either we take the first letter of text1 in the opt. solution and keep text2 as is
            # or we don't take the first letter of text1 and move to the next letter of text2
            return max(lcs_rec(i1+1, i2),
                       lcs_rec(i1, i2+1))
        return lcs_rec(0,0)


    def longestCommonSubsequenceBottomUp(self, text1: str, text2: str) -> int:
        """Time O(N*M), Space O(N*M)"""
        n1 = len(text1)
        n2 = len(text2)
        if n1 == 0 or n2 == 0:
            return 0
        
        # r(i,j) keeps the max common subseq. until index i-1 of text1 and index j-1 of text2
        r = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]:
                    r[i][j] = 1 + r[i-1][j-1]
                else:
                    r[i][j] = max(r[i-1][j], r[i][j-1])
        return r[n1][n2]