class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        answer = 1
        increase = 1
        decrease = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                increase += 1
                decrease = 1
            elif nums[i] < nums[i-1]:
                increase = 1
                decrease += 1
            else:
                increase = 1
                decrease = 1
            
            answer = max(answer, max(increase,decrease))
        
        return answer