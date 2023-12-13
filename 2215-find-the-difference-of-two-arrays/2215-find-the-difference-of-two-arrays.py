class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        com = set(nums1) & set(nums2)
        nums1 = list(set(nums1) - com)
        nums2 = list(set(nums2) - com)
        return [nums1,nums2]