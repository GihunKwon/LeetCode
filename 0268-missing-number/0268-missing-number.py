class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in range(0,len(nums)+1):
            if i not in nums:
                answer = i
        return answer
        