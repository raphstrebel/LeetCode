class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # keep array of ugly numbers
        r = [1] * n
        # keep indices of numbers multiplied by 2,3,5
        i_2 = 0
        i_3 = 0
        i_5 = 0
        for i in range(1, n):
            # at each index i, r[i] is the min of multiplying the previous ugly number at each index i_j by j (j = 2, 3, 5)
            r_2 = r[i_2]*2
            r_3 = r[i_3]*3
            r_5 = r[i_5]*5
            r[i] = min(r_2, r_3, r_5)
            if r[i] == r_2:
                i_2 += 1
            if r[i] == r_3:
                i_3 += 1
            if r[i] == r_5:
                i_5 += 1
        return r[n-1]