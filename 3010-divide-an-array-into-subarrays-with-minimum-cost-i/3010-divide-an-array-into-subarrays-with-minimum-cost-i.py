class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        answer = nums[0]
        num = sorted(nums[1:])
        answer += num[0] + num[1]
        return answer