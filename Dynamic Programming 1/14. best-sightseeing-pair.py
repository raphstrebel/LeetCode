class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        When we consider index i in the array, all values at indices j < i are 
        decreased by i-j (the distance between the two indices). 
        Now at index i, we must only consider the maximum of all previous 
        values minus their distance to i. We keep track of this value as 'left_max'. 
        At every new index, this value decreases by one. Then we update 'max_' 
        if the new value + the previous maximum (left_max) is greater.
        """
        max_ = 0
        left_max = 1
        for i, v in enumerate(values):
            # previous maximum distance is increased
            left_max -= 1
            max_ = max(max_, v + left_max)
            left_max = max(left_max, v)
        return max_