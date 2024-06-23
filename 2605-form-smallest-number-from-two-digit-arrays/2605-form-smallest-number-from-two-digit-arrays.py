class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = list(set(nums1) & set(nums2))
        if len(common) > 0:
            return min(common)
        else:
            a = min(nums1)
            b = min(nums2)
            if a > b:
                return int(str(b) + str(a))
            else:
                return int(str(a) + str(b))