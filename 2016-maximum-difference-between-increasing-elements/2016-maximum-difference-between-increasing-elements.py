class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] - nums[i] > answer:
                    answer = nums[j] - nums[i]
        return answer if answer else -1