class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = 0
        b = 0
        for i in nums1:
            if i in nums2:
                a += 1
        for j in nums2:
            if j in nums1:
                b += 1
        return [a,b]