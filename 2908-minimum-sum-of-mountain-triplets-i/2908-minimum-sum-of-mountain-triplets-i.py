class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        answer = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        answer.append(nums[i] + nums[j] + nums[k])
        return min(answer) if answer else -1