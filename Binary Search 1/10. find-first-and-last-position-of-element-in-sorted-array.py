class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Runtime: O(log(N))"""
        n = len(nums)
        first, second = -1, -1

        # find first target
        start, stop = 0, n-1
        while start <= stop:
            mid = (start + stop) // 2
            if nums[mid] == target:
                # save position of mid and set new "stop"
                if mid == start or nums[mid - 1] < target:
                    first = mid
                stop = mid - 1
            elif nums[mid] > target:
                stop = mid - 1
            else:
                start = mid + 1
        # there is no target
        if first == -1:
            return (-1, -1)
        
        # find second (start at index of first)
        start, stop = first, n-1
        while start <= stop:
            mid = (start + stop) // 2
            if nums[mid] == target:
                # save position of mid and set new "start"
                if mid == stop or nums[mid + 1] > target:
                    second = mid
                start = mid + 1
            elif nums[mid] > target:
                stop = mid - 1
            else:
                start = mid + 1
        return (first, second)
        
    