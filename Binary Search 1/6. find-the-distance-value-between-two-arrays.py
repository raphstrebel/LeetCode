class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        """
        Number of elements of array 1 for which all elements in array 2
        are at distance at least d.

        Runtime: O(N*log(N) + M*log(M) + N * M)
            - sorting both arrays: O(N*log(N)) O (M*log(M))
            - iterate over first array: O(N * M)
               - find closest element in array2: at most (M - start_idx) for start_idx between 0 and M.
                 in the worst case, M > N and min(N) = min(M) and max(N) = max(M). Then we get
                 a runtime of O(M) in total (as start_idx is incremented at every iteration of arr1).
                 If N > M, then find_closest will be called N times, but start_idx will not always be
                 incremented.
                -> O(N * M)
        """
        
        # sort arrays
        arr1 = sorted(arr1)
        arr2 = sorted(arr2)
        
        def find_closest(start_idx, elem1):
            """
            Find closest element in array2 starting from 'start_idx' 
            since both arrays are sorted.
            """
            diff = abs(arr2[start_idx] - elem1)
            for i, e in enumerate(arr2[start_idx:]):
                new_diff = abs(e - elem1)
                if new_diff > diff:
                    # return previous index and diff 
                    return start_idx + i - 1, diff
                diff = new_diff
            return start_idx + i, diff
        
        
        # for all elements in array 1, find closest element in array 2
        # if it is > d, increment result
        res = 0
        start_idx = 0
        for elem1 in arr1:
            start_idx, diff = find_closest(start_idx, elem1)
            if diff > d:
                res += 1
        return res