class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        if n == 3:
            return 2
        
        # max-min concept: product is maximized when n is broken into 3's
        # and padded with 2's if needed
        mod_3 = n % 3
        div_3 = n//3
        if mod_3 == 0:
            # n is broken only into "div_3" 3's
            return 3**div_3
        elif mod_3 == 1:
            # n is broken into "div_3" 3's and two 2's
            return 3**(div_3-1)*4
        else:
            # n is broken into "div_3" 3's and one 2
            return 3**(div_3)*2