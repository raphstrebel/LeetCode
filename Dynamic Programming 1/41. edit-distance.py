class Solution:
    def minDistanceBottomUp(self, word1: str, word2: str) -> int:
        """Bottom-up DP with table"""
        n1 = len(word1)
        n2 = len(word2)
        
        # if either word has length 0, need to build other word
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1
        # constraint: max word length is 500 so dist is at most 500
        # r(i1, i2) contains dist between i1'th char of word1 and i2'th char of word2
        r = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        
        # fill first row/col with length of other word (which is min distance)
        for i1 in range(n1+1):
            r[i1][0] = i1
        for i2 in range(n2+1):
            r[0][i2] = i2
            
        # compute dist between any two indices of words
        for i1 in range(1, n1+1):
            for i2 in range(1, n2+1):
                if word1[i1-1] == word2[i2-1]:
                    # chars are the same, move to the next
                    r[i1][i2] = r[i1-1][i2-1]
                else:
                    # r(i1, i2) is min of 1+"delete prev char in word1",
                    # 1+"delete prev char in word2", 1 + "replace char in word1"
                    r[i1][i2] = 1 + min(r[i1-1][i2], r[i1][i2-1], r[i1-1][i2-1])
        return r[n1][n2]


    def minDistanceRecCachingNaive(self, word1: str, word2: str) -> int:
        """Naive Recursive with caching"""
        n1 = len(word1)
        n2 = len(word2)
        
        # if either word has length 0, need to build other word
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1
        
        @lru_cache(maxsize=None)
        def minDistRec(w1, w2):
            n1 = len(w1)
            n2 = len(w2)
            if n1 == 0:
                return n2
            if n2 == 0:
                return n1
        
            # while words are equal, keep going foward
            i = 0
            n = min(n1, n2)
            while i < n and w1[i] == w2[i]:
                i += 1
            # check if end of a word is reached
            if i == n1:
                return n2 - n1
            if i == n2:
                return n1 - n2

            # now word1[i] != word2[i], so we need min between 
            # 1. deleting i'th char of word1,
            # 2. deleting i'th char of word2
            # 3. insert new char in position i+1 of word1
            # 4. insert new char in position i+1 of word2
            # 3. replacing i'th char in any of the words
            return 1 + min(minDistRec(w1[i+1:], w2[i:]), minDistRec(w1[i:], w2[i+1:]), minDistRec(w2[i] + w1[i+1:], w2[i:]), minDistRec(w1[i:], w1[i] + w2[i+1:]), minDistRec(w1[i+1:], w2[i+1:])) 
        
        return minDistRec(word1, word2)

    def minDistanceRecCachingOpt(self, word1: str, word2: str) -> int:
        """Nicer recursion with caching"""
        n = len(word1)
        m = len(word2)
        
        # if either word has length 0, need to build other word
        if n == 0:
            return m
        if m == 0:
            return n

        @lru_cache(maxsize=None)
        def minDistRec(i, j):
            # iterate from right to left
            if i < 0 or j < 0: 
                return j + i + 2
            if word1[i] == word2[j]:
                # same chars, move to the left in both words
                return minDistRec(i - 1, j - 1)
            else:
                # 1 + min between:
                # replace the char in word1
                # delete char in word1
                # delete char in word2
                return 1 + min(minDistRec(i - 1, j - 1), 
                               minDistRec(i - 1, j), 
                               minDistRec(i, j - 1))
        return minDistRec(n - 1, m - 1)