class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        answer = set(nums[0])
        for i in nums:
            answer &= set(i)
        return sorted(answer)