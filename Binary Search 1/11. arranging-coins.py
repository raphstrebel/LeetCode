class Solution:
    def arrangeCoinsBS(self, n: int) -> int:
        """
        Using BS:
        Call number of stairs as m, then 0 <= m <= n
        (there cannot be more stairs than coins)
        """
        
        start, stop = 0, n
        while start <= stop:
            m = (start + stop) // 2
            m_stairs = m * (m + 1) // 2
            if m_stairs == n:
                return m
            if m_stairs < n:
                start = m + 1
            else:
                stop = m - 1
        return stop

    def arrangeCoinsMath(self, n: int) -> int:
        """
        Using Math:
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
