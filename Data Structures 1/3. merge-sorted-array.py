class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:m]
        idx_2 = 0
        idx_3 = 0
        for i in range(n+m):
            if idx_2 == n:
                nums1[i:] = nums3[idx_3:]
                return
            elif idx_3 == m:
                nums1[i:] = nums2[idx_2:]
                return
            if nums2[idx_2] <= nums3[idx_3]:
                nums1[i] = nums2[idx_2]
                idx_2 += 1
            else:
                nums1[i] = nums3[idx_3]
                idx_3 += 1