class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Keep 2 arrays left_max and right_max. At each index i, left_max[i] contains the maximum on the left of i (same for right_max).
        For each i, the amount of water contributed is the minimum of the left and right peaks around i.
        """
        n = len(height)
        left_max = [height[0]] * n
        right_max = [height[n-1]] * n
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])
            right_max[n-i-1] = max(height[n-i-1], right_max[n-i])
        filled = 0
        for i in range(n):
            filled += min(left_max[i], right_max[i]) - height[i]
        return filled