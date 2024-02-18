class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        big = max(nums) - k
        small = min(nums) + k

        return max(0, (big-small))