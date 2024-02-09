class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = [-1]*len(nums1)
        for i,num in enumerate(nums1):
            x = nums2.index(num)
            for j in range(1,len(nums2)-x):
                if x + j < len(nums2) and nums2[x+j] > num:
                    answer[i] = nums2[x+j]
                    break
        return answer