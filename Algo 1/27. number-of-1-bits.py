class Solution:
    def hammingWeight(self, n: int) -> int:
        nb_ones = 0
        while n != 0:
            # if last bit is one, count it and shift to the right
            if n & 1:
                nb_ones += 1
            n >>= 1
        return nb_ones