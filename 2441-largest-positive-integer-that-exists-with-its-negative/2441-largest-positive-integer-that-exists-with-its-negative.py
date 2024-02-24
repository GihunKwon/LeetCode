class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        answer = -1
        for i in sorted(nums,reverse=True):
            if -i in nums:
                return i
        return answer