class Solution:
    def reverseBits(self, n: int) -> int:
        rev, power = 0, 31
        while n != 0:
            # take right-most bit, shift it by current power and add it to "rev"
            rev += (n & 1) << power
            n = n >> 1
            power -= 1
        return rev