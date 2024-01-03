class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        answer = []
        if len(nums) < 2:
            return nums
        for i in nums:
            if i % 2 == 0:
                answer.append(i)
        for j in nums:
            if j % 2 == 1:
                answer.append(j)
        return answer