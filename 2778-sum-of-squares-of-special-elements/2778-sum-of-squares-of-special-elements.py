class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # answer = 0
        # n = len(nums)
        # for i in range(1,n+1):
        #     if n % i == 0:
        #         answer += nums[i-1]**2
        # return answer
        answer = 0
        n = len(nums)
        for i,num in enumerate(nums):
            if n % (i+1) == 0:
                answer += num**2
        return answer