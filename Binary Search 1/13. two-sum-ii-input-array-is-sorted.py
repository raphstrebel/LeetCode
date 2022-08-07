class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        If there are two numbers in (sorted) list 'numbers' 
        that sum up to 'target', return them.
        Runtime: O(N)
        """
        start, stop = 0, len(numbers)-1
        while start < stop:
            s = numbers[start] + numbers[stop]
            if s == target:
                # indices start at 1
                return start+1, stop+1
            elif s < target:
                start += 1
            else:
                stop -= 1
        # no twoSum for target
        return -1, -1