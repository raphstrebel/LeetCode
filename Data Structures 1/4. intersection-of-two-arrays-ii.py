class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        for n in nums1:
            if n in hashmap.keys():
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        res = []
        for n in nums2:
            if n in hashmap.keys():
                if hashmap[n] > 0:
                    hashmap[n] -= 1
                    res.append(n)
        return res