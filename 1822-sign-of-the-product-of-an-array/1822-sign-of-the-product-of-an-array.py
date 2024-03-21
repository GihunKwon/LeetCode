class Solution:
    def arraySign(self, nums: List[int]) -> int:
        answer = 1
        for i in nums:
            answer *= i
        if answer > 0:
            return 1
        elif answer == 0:
            return 0
        else:
            return -1