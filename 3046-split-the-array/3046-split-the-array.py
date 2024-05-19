class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        for i in set(nums):
            if nums.count(i) > 2:
                return False
        return True