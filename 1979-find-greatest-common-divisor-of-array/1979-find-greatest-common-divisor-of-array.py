class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return max([i for i in range(1,min(nums)+1) if max(nums) % i == 0 and min(nums) % i == 0])