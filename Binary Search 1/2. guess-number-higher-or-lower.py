# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start, stop = 0, n
        while True:
            mid = int((start + stop) / 2)
            ans = guess(mid)
            if ans == 0:
                return mid
            if ans == 1:
                start = mid + 1
            else:
                stop = mid - 1