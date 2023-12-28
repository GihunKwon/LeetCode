class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        answer = 0
        for i in set(nums):
            if nums.count(i) == 1:
                answer += i
        return answer