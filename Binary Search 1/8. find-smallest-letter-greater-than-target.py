class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Using Binary Search:
        Time: O(log(N))
        Space: O(1)
        """
        if len(letters) == 1:
            return letters[0]
        # if target is smaller than first letter or larger than last,
        # smallest letter is the next greatest letter
        if target < letters[0] or letters[-1] <= target:
            return letters[0]
        start, stop = 0, len(letters)-1
        while start <= stop:
            mid = (start + stop) // 2
            l1 = letters[mid]
            l2 = letters[mid + 1]
            if l1 <= target and target < l2:
                return l2
            if target < l2:
                stop = mid
            else:
                start = mid + 1
        return l2