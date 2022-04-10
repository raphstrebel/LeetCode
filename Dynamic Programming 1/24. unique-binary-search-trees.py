class Solution:
    def numTrees(self, n: int) -> int:
        # keep number of trees for each index i
        r = [0] * (n+1)
        r[0] = 1  # if n = 0 only empty tree
        r[1] = 1  # if n = 1 there is only one possible tree
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                # num trees at i is the sum on j of:
                #     num trees on the left of j (r[j-1])
                #     + num trees from j until i (r[i-j])
                r[i] += r[i - j] * r[j - 1]
        return r[n]