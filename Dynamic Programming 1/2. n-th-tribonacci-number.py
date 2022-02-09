class Solution:
    def tribonacciButtomUp(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        res = [0] * (n+1)
        res[1] = 1
        res[2] = 1
        for i in range(3, n+1):
            res[i] = res[i-1] + res[i-2] + res[i-3]
        return res[n]

    def tribonacciTopDown(self, n: int) -> int:
        res = [-1] * (n+1)
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        res[0] = 0
        res[1] = 1
        res[2] = 1
        def triboRec(i):
            if i < 0:
                return 0
            if res[i] >= 0:
                return res[i]
            res[i] = triboRec(i-1) + triboRec(i-2) + triboRec(i-3)
            return res[i]
        return triboRec(n)