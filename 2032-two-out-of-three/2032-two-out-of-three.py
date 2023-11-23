class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        num1 = set(nums1)
        num2 = set(nums2)
        num3 = set(nums3)

        num_all = num1|num2|num3
        answer=[]
        for i in num_all:
            if (i in num1 and i in num2) or (i in num3 and i in num2) or (i in num1 and i in num3):
                answer.append(i)
        return answer