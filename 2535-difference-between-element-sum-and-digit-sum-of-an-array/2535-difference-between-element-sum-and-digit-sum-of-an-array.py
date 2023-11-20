class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit = 0
        for i in nums:
            for j in str(i):
                digit += int(j)
        return abs(sum(nums)-digit)