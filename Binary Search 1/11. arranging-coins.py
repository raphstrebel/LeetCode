class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Using Maths:
        n = 1 + 2 + ... + m + eps, eps < m
        <-> n = m * (m + 1) / 2 + eps
        (eps < m, n = math.floor(m * (m + 1) / 2 + eps))
         -> n >= m * (m + 1) / 2
        <-> 2 * n >= m^2 + m
        <-> 2 * n >= m^2 + m + 1/4 - 1/4
        <-> 2 * n >= (m + 1/2)^2 - 1/4
        <-> sqrt(2 * n + 1/4) - 1/2 >= m
        <-> m <= sqrt(2 * n + 1/4) - 1/2
        -> m = math.floor(sqrt(2 * n + 1/4) - 1/2)
        """
        return int(math.sqrt(2 * n + 1/4) - 1/2)
