class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        answer = 1
        cnt = nums[0]+nums[0+1]
        for i in range(2,len(nums)-1,2):
            if nums[i] + nums[i+1] == cnt:
                answer += 1
            else:
                break
        return answer