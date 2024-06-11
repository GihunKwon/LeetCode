class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = list(set(nums1)&set(nums2))
        answer = []
        for i in common:
            a = nums1.count(i)
            b = nums2.count(i)
            cnt = min(a,b)
            for _ in range(cnt):
                answer.append(i)

        return answer