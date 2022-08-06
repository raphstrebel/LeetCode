class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        start, stop = 0, n-1
        while start <= stop:
            mid = (start + stop) // 2
            # arr[mid] - mid - 1 is nb missing numbers at "mid"
            if arr[mid] - mid - 1 < k:
                start = mid + 1
            else:
                stop = mid - 1     
        return start + k